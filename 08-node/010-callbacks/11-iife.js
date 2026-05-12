/**
 * Get list of students.
 *
 * @returns {Promise<string[]>}
 */
const getStudents = () => {
  return new Promise((resolve, reject) => {
    console.log("Getting students...");

    // randomly simulate an error
    if (Math.random() < 0.5) {
      return reject(new Error("Failed to retrieve students"));
    }

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
  return new Promise((resolve, reject) => {
    console.log("Generating grades...");

    // randomly simulate an error
    if (Math.random() < 0.5) {
      return reject(new Error("Failed to generate grades"));
    }

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

(async () => {
  try {
    const students = await getStudents();
    const grades = await getGrades(students);
    await saveReport(grades);

    console.log("Report on grades of the students produced!");
  } catch (error) {
    console.error("Something went wrong:", error.message);
    console.debug("Stack trace:", error.stack);
  }
})();
