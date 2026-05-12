// index-with-errors.js
import express from "express";
const app = express();
const port = 3000;
app.get("/", (req, res) => {
  res.send("Hello from Express!");
});
app.listen(port, (error) => {
  if (error) {
    console.error("Error starting the server:", error);
    return;
  }
  console.log(`Hello app listening on port ${port}`);
});
