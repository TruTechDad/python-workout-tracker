import json
from datetime import datetime

print("Welcome to your Workout Tracker 💪")

# Initialize an empty list to store workouts
try:
    with open('workouts.json', 'r') as file:
        workouts = json.load(file)
except FileNotFoundError:
    workouts = []

while True:
    print("\nWhat would you like to do?")
    print("1. Add Workout")
    print("2. View Workouts")
    print("3. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        exercise = input("Enter exercise: ")
        weight = input("Enter weight: ")
        reps = input("Enter reps: ")

        workout = {
            "exercise": exercise,
            "weight": weight,
            "reps": reps,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        workouts.append(workout)
        print("\nWorkout added:")

    elif choice == "2":
        print("\nYour Workouts:")

        if len(workouts) == 0:
            print("No workout saved.")
        else:
            for i, w in enumerate(workouts, start=1):
                date = w.get('date', 'No date')
            print(f"{i}. {w['exercise']} - {w['weight']} lbs x {w['reps']} reps ({date})")

    elif choice == "3":
        with open("workouts.json", "w") as file:
            json.dump(workouts, file)

        print("Workouts saved. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

    
   