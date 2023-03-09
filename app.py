import numpy as np
from flask import Flask, render_template, url_for, request
import joblib


app= Flask(__name__)
rf_model= joblib.load(open('rfmodel.h5', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=np.array(data).reshape(1,-1)  
    print(final_input)
    output=rf_model.predict(final_input)[0]
    if output == 1:
        return render_template("index.html", prediction_text="The Loan status is yes ")
    else:
        return render_template("index.html", prediction_text="The Loan status is no ")


if __name__=="__main__":   # To start the app
    app.run(debug=True)    # Enabling debugging
