# simple API that exports an Excel file
# navigate to http://127.0.0.1:5000/report to download the Excel file.

from flask import Flask, send_file
import pandas as pd

app = Flask(__name__)

@app.route("/report")

def report():
    data = {"Product": ["Mouse", "Keyboard", "Monitor"],
            "Sales": [150, 200, 50]}
    df = pd.DataFrame(data)
    file = "api_report.xlsx"
    df.to_excel(file, index=False)
    return send_file(file, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
    
