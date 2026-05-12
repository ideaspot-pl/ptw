/**
 * Get list of students and pass to callback.
 *
 * @param {function(string[]): void} callback
 * @returns {void}
 */
const getStudents = (callback) => {
  console.log("Getting students...");

  // some processing...
  const students = ["Alice", "Bob", "Carol", "Dave"];

  callback(students);
};

/**
 * Generate grades for students.
 *
 * @param {string[]} students
 * @param {function(Object[]): void} callback
 * @returns {void}
 */
const getGrades = (students, callback) => {
  console.log("Generating grades...");

  // some processing...
  const grades = students.map((student) => {
    return {
      name: student,
      grade: Math.max(2, Math.min(5, student.length)),
    };
  });

  callback(grades);
};

/**
 * Save report and execute callback when done.
 *
 * @param {Object[]} grades
 * @param {function(): void} callback
 * @returns {void}
 */
const saveReport = (grades, callback) => {
  console.log("Saving report...");

  // some processing...
  console.log("\tReport:");

  for (const student of grades) {
    console.log(`\t\t${student.name}: ${student.grade}`);
  }

  callback();
};

// Callback Hell example
getStudents((students) => {
  getGrades(students, (grades) => {
    saveReport(grades, () => {
      console.log("Report on grades of the students produced!");
    });
  });
});
