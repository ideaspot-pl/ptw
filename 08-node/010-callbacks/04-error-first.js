/**
 * Get list of students and pass to callback.
 *
 * @param {function(Error|null, string[]|null): void} callback 
 * @returns {void}
 */
const getStudents = (callback) => {
  console.log("Getting students...");
  
  // randomly simulate an error
  if (Math.random() < 0.5) {
    return callback(new Error("Failed to retrieve students"), null);
  }

  // some processing...
  setTimeout(() => {
    const students = ["Alice", "Bob", "Carol", "Dave"];
    
    callback(null, students);
  }, 2000);
};

getStudents((error, names) => {
  if (error) {
    return console.error(error.message);
  }

  for (const name of names) {
    console.log(name.toUpperCase());
  }
});
