from flask import Flask, render_template, request, redirect, url_for, jsonify

# create the flask app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/success/<int:score>')
def success(score):
    return "The person has passed, and the score is " + str(score)


@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed, and the score is " + str(score)


@app.route('/calculate', methods=['POST', 'GET'])
def calculate():
    if request.method == 'GET':
        return render_template('calculate.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])

        average_marks = (maths + science + history) / 3
        average_marks = round(average_marks, 2)
        result = "success" if average_marks >= 50 else "fail"

        return render_template('result.html', results=average_marks)


if __name__ == '__main__':
    app.run(debug=True)
