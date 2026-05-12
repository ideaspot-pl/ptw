const getStudents = (callback) => {
  console.log("Getting students...");

  // some processing...
  setTimeout(() => {
    const students = ["Alice", "Bob", "Carol", "Dave"];
    
    callback(students);
  }, 2000);
};

getStudents((names) => {
  for (const name of names) {
    console.log(name.toUpperCase());
  }
});
