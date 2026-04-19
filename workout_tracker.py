print("Welcome to your Workout Tracker 💪")

while True:
    exercise = input("\nEnter exercise (or press q to quit): ")
    
    if exercise == 'q':
        print("Exiting Workout Tracker. Goodbye!")
        break
    
    weight = input("Enter weight: ")
    reps = input("Enter reps: ")

print("\nWorkout Saved!")
print("Exercise:", exercise)
print("Weight:", weight)
print("Reps:", reps)