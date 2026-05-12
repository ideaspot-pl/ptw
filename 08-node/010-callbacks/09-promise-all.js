/**
 * Get random student (takes time!)
 *
 * @returns {Promise<string>}
 */
const getRandomStudent = () => {
  return new Promise((resolve) => {
    const students = ["Alice", "Bob", "Carol", "Dave", "Eve"];

    // random delay
    const delay = Math.round(Math.random() * 5 * 1000);

    setTimeout(() => {
      const randomStudent =
        students[Math.floor(Math.random() * students.length)];

      console.log(`Student ${randomStudent} retrieved after ${delay}ms`);

      resolve(randomStudent);
    }, delay);
  });
};

console.log("Run all at once and wait for all to resolve...");
Promise.race([ // todo replace with any() and race() !
  getRandomStudent(),
  getRandomStudent(),
  getRandomStudent(),
  getRandomStudent(),
  getRandomStudent(),
]).then((results) => {
  console.log("\nRandomly selected students:");
  console.log(results);
});

console.log('The main thread has ended already...');
