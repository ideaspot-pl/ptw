const getStudents = (callback) => {
  console.log("Getting students...");

  // some processing...
  const students = ["Alice", "Bob", "Carol", "Dave"];

  callback(students);
};

getStudents((names) => {
  for (const name of names) {
    console.log(name.toUpperCase());
  }
});
