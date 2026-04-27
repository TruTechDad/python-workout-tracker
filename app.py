from flask_cors import CORS
from flask import Flask, jsonify, request
import json

app = Flask(__name__)
CORS(app)

#Load workouts from file
def load_workouts():
    try:
        with open("workouts.json", "r") as file:
            return json.load(file)
    except: 
         return
    
#Save workouts to file
def save_workouts(workouts):
    with open("workouts.json", "w") as file:
        json.dump(workouts, file)

#Get all workouts
@app.route("/workouts", methods=["GET"])
def get_workouts():
    workouts = load_workouts()
    return jsonify(workouts)

#Post a new workout
@app.route("/workouts", methods=["POST"])

def add_workout():

    workouts = load_workouts()

    data = request.json

    workout = {
        "exercise": data["exercise"],
        "weight": data["weight"],
        "reps": data["reps"]
    }

    workouts.append(workout)
    save_workouts(workouts)

    return jsonify({"message": "Workout added!"})

if __name__ == "__main__":
    app.run(debug=True)