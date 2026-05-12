// index.js
import express from "express";
const app = express();
const port = 3000;
app.set("view engine", "ejs");
app.get("/", (req, res) => {
  res.render("index", {
    username: "Artur",
  });
});
app.listen(port, () => {
  console.log(`Hello app listening on port ${port}`);
});
