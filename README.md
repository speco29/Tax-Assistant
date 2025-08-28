# 🧾 Tax Assistant

A sleek and interactive Flask web app that helps users mpare incocome tax under **India's old and new tax regimes**. Based on deductions and total income, it calculates both tax outcomes and recommends the optimal regime—plus offers a **PDF export** for financial summaries!
   
---       
    
## ✨ Features
 
- 🔢 Input total income, eligible deductions (80C, 80D, home loan interest)
- 📊 Calculates tax under both Old and New regimes 
- 🧠 Suggests the more beneficial regime based on deduction usage
- 💬 Provides insights into deduction utilization and savings strategy
- 📥 Exports tax summary to PDF using `html2pdf.js`
- 🧪 Built with Flask and Jinja2 templates

---

## 🛠️ Technologies Used

| Tech          | Purpose                              |
|---------------|--------------------------------------|
| Flask         | Web app framework                    |
| Jinja2        | Templating for dynamic HTML          |
| html2pdf.js   | Frontend PDF export                  |
| Python        | Core tax logic and routing           |
| CSS (inline)  | Simple, clean UI styling             |

---

## 🚀 Getting Started

```bash
# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

# Install required packages
pip install flask

# Run the app
python app.py
```
Open your browser and visit: ```http://127.0.0.1:5000```


## PDF Export
After submitting your tax inputs, click the Download Summary as PDF button to export a beautifully styled summary. Perfect for record keeping, sharing, or showcasing your results.

## How It Works
- ```app.py```: Main Flask app with routes and form handling
- ```tax_engine.py```: Contains logic to calculate tax under both regimes
- ```deduction_rule.py```: Handles deduction parsing and rule enforcement
- ```index.html```: Styled template with form, summary section, and download capability
- ```html2pdf.js```: Converts result summary to downloadable PDF from browser

## Example Output

```
    Income: ₹1200000.00  
    Taxable Income: ₹990000.00  
    Deductions:  
        - 80C: ₹5000.00  
        - 80D: ₹5000.00  
        - 24(b): ₹200000.00  

    Old Regime Tax: ₹110500.00  
    New Regime Tax: ₹90000.00  
    Recommended: New Regime  
    💬 Deductions seem underutilized—New Regime might offer better savings.
```
**To see the result of assistant, you can visit the ```visuals``` folder as it contains the screenshots of example.**
