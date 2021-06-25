import os
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__, template_folder="./templates")

MODEL_PATH = os.path.join(os.path.dirname(__file__), "models/model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/healthcheck")
def healthcheck():
    return "The API is running smoothly"


@app.route("/predict", methods=["POST"])
def predict():
    """
    For rendering results on HTML GUI
    """
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    model = pickle.load(open(MODEL_PATH, "rb"))
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template(
        "index.html", prediction_text="Employee Salary should be $ {}".format(output)
    )


@app.route("/predict_api/v1", methods=["POST"])
def predict_api():
    """
    Testing the api service through the request
    """
    data = request.get_json(force=True)
    model = pickle.load(open(MODEL_PATH, "rb"))
    prediction = model.predict([np.array(list(data.values()))])
    output = prediction[0]
    return jsonify(f"The estimated salary is : {output}")


if __name__ == "__main__":
    app.run(debug=True)
