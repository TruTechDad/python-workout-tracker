import json

print("Welcome to your Workout Tracker 💪")

# Initialize an empty list to store workouts
try:
    with open('workouts.json', 'r') as file:
        workouts = json.load(file)
except FileNotFoundError:
    workouts = []

while True:
    exercise = input("\nEnter exercise (or type 'q' to quit): ")

    if exercise == 'q':
        # Save workouts to a JSON file before exiting
        with open('workouts.json', 'w') as file:
            json.dump(workouts, file, indent=4)

        print("\nWorkouts saved to file. Exiting...")
        print("Goodbye 👋")
        break

    weight = input("Enter weight: ")
    reps = input("Enter reps: ")

    workout = {
        "exercise": exercise,
        "weight": weight,
        "reps": reps
    }

    workouts.append(workout)

    print("\nWorkout Saved!")