/**
 * Get list of students.
 *
 * @returns {Promise<string[]>}
 */
const getStudents = () => {
  return new Promise((resolve) => {
    console.log("Getting students...");

    // some processing...
    const students = ["Alice", "Bob", "Carol", "Dave"];

    resolve(students);
  });
};

/**
 * Generate grades for students.
 *
 * @param {string[]} students
 * @returns {Promise<Object[]>}
 */
const getGrades = (students) => {
  return new Promise((resolve) => {
    console.log("Generating grades...");

    // some processing...
    const grades = students.map((student) => {
      return {
        name: student,
        grade: Math.max(2, Math.min(5, student.length)),
      };
    });

    resolve(grades);
  });
};

/**
 * Save report.
 *
 * @param {Object[]} grades
 * @returns {Promise<void>}
 */
const saveReport = (grades) => {
  return new Promise((resolve) => {
    console.log("Saving report...");

    // some processing...
    console.log("\tReport:");

    for (const student of grades) {
      console.log(`\t\t${student.name}: ${student.grade}`);
    }

    resolve();
  });
};

getStudents()
  .then((students) => {
    return getGrades(students);
  })
  .then((grades) => {
    return saveReport(grades);
  })
  .then(() => {
    console.log("Report on grades of the students produced!");
  })
  .catch((error) => {
    console.error("Something went wrong:", error);
  });
