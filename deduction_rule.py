 
def identify_deductions(user_data):
    deductions = {}  
    
    # Basic example: Section 80C (e.g., PPF, ELSS) 
    investments = user_data.get("investments", 0)
    deductions["80C"] = min(investments, 150000)


    # Section 80D: Health insurance
    insurance = max(0, user_data.get("health_insurance", 0))
    deductions["80D"] = min(insurance, 25000)  # Could vary based on age

    # Section 24(b): Home loan interest
    home_interest = max(0, user_data.get("home_loan_interest", 0))
    deductions["24(b)"] = min(home_interest, 200000)
    
    
    
    return deductions
