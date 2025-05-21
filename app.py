# ~/joshidata/ml_app/src/app.py

from flask import Flask, request, render_template
from model_utils import predict_tallness

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            height = float(request.form['height'])
            prediction = predict_tallness(height)
        except ValueError:
            prediction = "Invalid input. Please enter a number."
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

