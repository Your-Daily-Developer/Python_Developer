from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)
inventory = [
]

@app.route('/')

def home():
    total=0
    for item in range(len(inventory)):
        total=total+inventory[item]['quantity'] * inventory[item]['price']

    return render_template('professional.html',inventory_html=inventory,total_html=total)
if "__main__" == __name__:
    app.run(debug=True)


