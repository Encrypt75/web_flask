from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route("/contact") 
def contact(): 
    return render_template("contacts.html") 
    
@app.route('/areaofcircle', methods=['GET', 'POST'])
def circle():
    result = None
    if request.method == 'POST':
        radius_str = request.form.get('radius', '0')
        try:
            radius = float(radius_str)
            result = math.pi * radius ** 2
        except ValueError:
            result = "Please enter a valid number"
    
    return render_template('circle.html', result=result) 

@app.route('/areaoftriangle', methods=['GET', 'POST'])
def triangle():
    result = None
    if request.method == 'POST':
        width = request.form.get('width', '0')
        height = request.form.get('height', '0')
        try:
            w_flt = float(width)
            l_flt = float(height)
            result = (w_flt * l_flt) * 0.5
        except ValueError:
            result = "Please enter a valid number"
    
    return render_template('triangle.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)