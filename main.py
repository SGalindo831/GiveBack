from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chapters')
def chapters():
    chapters = [
        {"title": "Chapter 1", "summary": "Summary of chapter 1..."},
        {"title": "Chapter 2", "summary": "Summary of chapter 2..."},
        # Add more chapters as needed
    ]
    return render_template('chapters.html', chapters=chapters)

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        monthly_investment = float(request.form['monthly_investment'])
        years = int(request.form['years'])
        annual_return = 0.07  # Assumed 7% annual return

        # Calculate compound interest
        months = years * 12
        total = monthly_investment * ((1 + annual_return/12) ** months - 1) / (annual_return/12)
        total = round(total, 2)
        result = f"If you invest ${monthly_investment} monthly for {years} years, you could have ${total:,} in your IRA."

    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)