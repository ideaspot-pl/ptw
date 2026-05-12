// index-parameters.js
import express from "express";
const app = express();
const port = 3000;
app.set("view engine", "ejs");

// express 4: "/hello/:name?"
app.get("/hello/{:name}", (req, res) => {
  res.render("index", {
    username: req.params.name ?? "Guest",
  });
});
app.listen(port, () => {
  console.log(`Hello app listening on port ${port}`);
});
