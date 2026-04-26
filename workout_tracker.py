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
    print("3. Delete Workout")
    print("4. Quit")

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
        print("\nSelect a workout to delete:")

        if len(workouts) == 0:
            print("No workout to delete.")
        else:
            for i, w in enumerate(workouts, start=1):
                date = w.get('date', 'No date')
                print(f"{i}. {w['exercise']} - {w['weight']} lbs x {w['reps']} reps ({date})")

                try:
                    delete_index = int(input("Enter the number of the workout to delete: ")) - 1
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                if 0 <= delete_index < len(workouts):
                    removed = workouts.pop(delete_index)
                    print(f"Deleted: {removed['exercise']}")
                else:
                    print("Invalid number.")
    elif choice == "4":
        with open('workouts.json', 'w') as file:
            json.dump(workouts, file)

            print("💾 Workouts saved. Goodbye 👋")
            break

    else:
        print("❌ Invalid choice. Try again.")

    

    

    
   