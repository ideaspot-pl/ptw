/**
 * Get list of students and pass to callback.
 *
 * @param {function(string[]): void} callback - Function to be called with the students array.
 * @returns {void}
 */
const getStudents = (callback) => {
  console.log("Getting students...");

  // some processing...
  const students = ["Alice", "Bob", "Carol", "Dave"];

  callback(students);
};

/**
 * Print each name in upper case.
 *
 * @param {string[]} names - Array of names to print.
 * @returns {void}
 */
const printUpperCase = (names) => {
  for (const name of names) {
    console.log(name.toUpperCase());
  }
};

getStudents(printUpperCase);
