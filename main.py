

# ---- YOUR APP STARTS HERE ----

# -- Import section --
from flask import Flask
from flask import render_template
from flask import request


# -- Initialization section --
app = Flask(__name__)

# -- Routes section --

# INDEX
@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')



@app.route('/calc')
def calc():
  return render_template('calc.html')



@app.route('/results', methods=['POST'])
def results():


  return_statement = f"With a monthly income of ${income}, you should spend ${needs_suggestion} on your monthly needs, ${wants_suggestion} on your monthly wants, and ${savings_suggestion} for your monthly savings. As it is, you spend ${sum_of_needs} on your monthly needs, ${sum_of_wants} on your monthly wants, and ${sum_of_savings} on your monthly savings. "

  

  if sum_of_needs > needs_suggestion:
    return_statement += "\nCongratulations, you're off to a great start. Due to your financial circumstances, we recommend you rethink your spending choices, prioritize paying your needs, and earning more money. \nOn the social good page, you should check out options to contribute that don't require income!"

  if sum_of_needs < needs_suggestion:
    extra = needs_suggestion - sum_of_needs
    return_statement += f"Congratulations! You have an extra ${extra}. Consider putting it towards your savings or debt. If not, look at ways you can do social good by checking out ways to contribute monetarily to a cause of your choice!"
    

  
  if sum_of_needs == needs_suggestion:
    return_statement += "\nCongratulations! Your budget is perfectly balanced. \n\nLook at ways you can do social good by checking out ways to contribute to a cause of your choice without disrupting your income!"

  
  return render_template('results.html', return_statement = return_statement, needs_suggestion = needs_suggestion, wants_suggestion = wants_suggestion, savings_suggestion = savings_suggestion, sum_of_needs = sum_of_needs, sum_of_wants = sum_of_wants, sum_of_savings = sum_of_savings)



@app.route('/socialgood')
def socialgood():

  if sum_of_needs > needs_suggestion:
    socgood = "We suggest: With Disposable Income!"

  if sum_of_needs < needs_suggestion:
    socgood = "We suggest: No Money Required!"
  
  if sum_of_needs == needs_suggestion:
    socgood = "We suggest: W/O Disposable Income!"
  
  return render_template('socialgood.html', socgood = socgood)

@app.route('/about')
def about():
  return render_template('about.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
