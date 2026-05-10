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

    from datetime import datetime

    workout = {
    "exercise": data["exercise"],
    "weight": data["weight"],
    "reps": data["reps"],
    "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

    workouts.append(workout)
    save_workouts(workouts)

    return jsonify({"message": "Workout added!"})

#Delete all workouts
@app.route("/workouts/<int:index>", methods=["DELETE"])
def delete_workout(index):
    workout = load_workouts()

    if 0 <= index < len(workout):
        removed_workout = workout.pop(index)
        save_workouts(workout)
        return jsonify({"message": "Deleted workout", "workout": removed_workout})
    else:
        return jsonify({"error": "Invalid index"}), 400
    

@app.route("/generate", methods=["GET"])
def generate_workout():

    workout_plan = [
        {
            "exercise": "Bench Press",
            "sets": 4,
            "reps": 8
        },
        {
            "exercise": "Squats",
            "sets": 4,
            "reps": 10
        },
        {
            "exercise": "Pull Ups",
            "sets": 3,
            "reps": 12
        }
    ]

    return jsonify(workout_plan)


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


