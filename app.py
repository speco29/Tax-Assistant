from flask import Flask, render_template, request
from tax_engine import calculate_tax_old_regime, calculate_tax_new_regime 
from deduction_rule import identify_deductions
   
app = Flask(__name__)  

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            # Step 1: Get User Inputs
            income = float(request.form["income"])
            investments = float(request.form["investments"])
            insurance = float(request.form["insurance"])
            home_interest = float(request.form["home_interest"])

            # Step 2: Build and sanitize user data
            user_data = {
                "investments": max(0, investments),
                "health_insurance": max(0, insurance),
                "home_loan_interest": max(0, home_interest)
            }

            # Step 3: Apply deduction rules
            deductions = identify_deductions(user_data)
            taxable_income = income - sum(deductions.values())
            tax_old = calculate_tax_old_regime(income, deductions)
            tax_new = calculate_tax_new_regime(income)
            recommended = "New Regime 🟢" if tax_new < tax_old else "Old Regime 🟡"

            # Step 4: Suggestion based on how well deductions are used
            max_claim = {
                "80C": 150000,
                "80D": 25000,
                "24(b)": 200000
            }
            utilization_score = sum(
                1 for k, v in deductions.items() if v >= 0.8 * max_claim.get(k, 0)
            )

            if utilization_score >= 2:
                regime_comment = "📦 You're using deductions well—Old Regime likely benefits you more."
            else:
                regime_comment = "⚡ Deductions seem underutilized—New Regime might offer better savings."

            # Step 5: Compile all results
            result = {
                "income": income,
                "deductions": deductions,
                "taxable_income": taxable_income,
                "tax_old": tax_old,
                "tax_new": tax_new,
                "recommended": recommended,
                "regime_comment": regime_comment
            }

        except ValueError:
            result = {"error": "Please enter valid numbers!"}

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
