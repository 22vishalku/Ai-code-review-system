import React, { useState } from "react";

function App() {
  const [code, setCode] = useState("");
  const [review, setReview] = useState("");

  const handleSubmit = async () => {
    const res = await fetch("http://localhost:8000/review", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code }),
    });

    const data = await res.json();
    setReview(data.review);
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>AI Code Review System</h2>
      <textarea
        rows="10"
        cols="60"
        placeholder="Write your code here..."
        value={code}
        onChange={(e) => setCode(e.target.value)}
      />
      <br />
      <button onClick={handleSubmit}>Review Code</button>
      <h3>AI Review:</h3>
      <pre>{review}</pre>
    </div>
  );
}

export default App;
