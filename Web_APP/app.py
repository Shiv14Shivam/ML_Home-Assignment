from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and scaler
model = joblib.load("classification_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values
        MedInc = float(request.form['MedInc'])
        HouseAge = float(request.form['HouseAge'])
        AveRooms = float(request.form['AveRooms'])
        AveBedrms = float(request.form['AveBedrms'])
        Population = float(request.form['Population'])
        AveOccup = float(request.form['AveOccup'])
        Latitude = float(request.form['Latitude'])
        Longitude = float(request.form['Longitude'])

        # Create dataframe
        new_input = pd.DataFrame([{
            "MedInc": MedInc,
            "HouseAge": HouseAge,
            "AveRooms": AveRooms,
            "AveBedrms": AveBedrms,
            "Population": Population,
            "AveOccup": AveOccup,
            "Latitude": Latitude,
            "Longitude": Longitude
        }])

        # Scale input
        new_input_scaled = scaler.transform(new_input)

        # Predict
        prediction = model.predict(new_input_scaled)[0]

        # Convert numeric output to label
        if prediction == 0:
            result = "Low Value Area"
        elif prediction == 1:
            result = "Medium Value Area"
        else:
            result = "High Value Area"

        return render_template("index.html", prediction_text=result)

    except:
        return render_template("index.html", prediction_text="Error in input values")

if __name__ == "__main__":
    app.run()