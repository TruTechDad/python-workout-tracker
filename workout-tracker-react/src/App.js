import { useEffect, useState } from "react";

function App() {
  const [workouts, setWorkouts] = useState([]);
  const [exercise, setExercise] = useState("");
  const [weight, setWeight] = useState("");
  const [reps, setReps] = useState("");

  const loadWorkouts = async () => {
    const res = await fetch("http://127.0.0.1:5000/workouts");
    const data = await res.json();
    setWorkouts(data);
  };

  useEffect(() => {
    loadWorkouts();
  }, []);

  const addWorkout = async () => {
    await fetch("http://127.0.0.1:5000/workouts", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ exercise, weight, reps }),
    });

    setExercise("");
    setWeight("");
    setReps("");

    loadWorkouts();
  };

  const deleteWorkout = async (index) => {
    await fetch(`http://127.0.0.1:5000/workouts/${index}`, {
      method: "DELETE",
    });

    loadWorkouts();
  };

  return (
    <div
      style={{
        maxWidth: "600px",
        margin: "40px auto",
        fontFamily: "Arial",
        textAlign: "center",
      }}
    >
      <h1>Workout Tracker 💪</h1>

      <div style={{ marginBottom: "20px" }}>
        <input
          value={exercise}
          onChange={(e) => setExercise(e.target.value)}
          placeholder="Exercise"
          style={{ margin: "5px", padding: "8px" }}
        />
        <input
          value={weight}
          onChange={(e) => setWeight(e.target.value)}
          placeholder="Weight"
          style={{ margin: "5px", padding: "8px" }}
        />
        <input
          value={reps}
          onChange={(e) => setReps(e.target.value)}
          placeholder="Reps"
          style={{ margin: "5px", padding: "8px" }}
        />
        <br />
        <button
          onClick={addWorkout}
          style={{ padding: "8px 16px", marginTop: "10px" }}
        >
          Add Workout
        </button>
      </div>

      <h2>Your Workouts</h2>

      <ul style={{ listStyle: "none", padding: 0 }}>
        {workouts.map((w, index) => (
          <li
            key={index}
            style={{
              background: "#f4f4f4",
              margin: "10px 0",
              padding: "10px",
              borderRadius: "8px",
              display: "flex",
              justifyContent: "space-between",
            }}
          >
            <span>
              {w.exercise} - {w.weight} lbs x {w.reps}
              <br />
              <small style={{ color: "gray" }}>
                {w.date ? w.date : "No date"}
              </small>
            </span>
            <button onClick={() => deleteWorkout(index)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
