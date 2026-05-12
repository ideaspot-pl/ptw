const path = require("node:path");

const data = {};

// put a debugger breakpoint here!
data.filePath = path.join("files", "cupcake.txt");
data.extension = path.extname(data.filePath);
data.fileName = path.basename(data.filePath);
data.directory = path.dirname(data.filePath);
data.absolutePath = path.resolve(data.filePath);

console.log(JSON.stringify(data, null, 2));
