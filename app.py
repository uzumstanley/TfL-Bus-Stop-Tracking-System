from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load dataset
df = pd.read_csv("/Users/mac/Desktop/TRAFFIC/Bus Stops/TfL-App/cleaned_Bus_Stops.csv")

@app.route("/")
def home():
    return "Welcome to the TfL Smart Bus API!"

@app.route("/stops", methods=["GET"])
def get_stops():
    """Returns all bus stops"""
    return jsonify(df.to_dict(orient="records"))

@app.route("/stops/search", methods=["GET"])
def search_stops():
    """Search for a bus stop by name"""
    query = request.args.get("name", "").lower()
    results = df[df["STOP_NAME"].str.lower().str.contains(query, na=False)]
    return jsonify(results.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
