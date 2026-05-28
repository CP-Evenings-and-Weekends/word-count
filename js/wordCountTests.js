const wordCount = require("./wordCount");

function deepEqual(a, b) {
  return JSON.stringify(a) === JSON.stringify(b);
}

console.log(deepEqual(wordCount("the cat sat on the mat"), { the: 2, cat: 1, sat: 1, on: 1, mat: 1 }));
console.log(deepEqual(wordCount("Hello, hello! HELLO?"), { hello: 3 }));
console.log(deepEqual(wordCount(""), {}));
console.log(deepEqual(wordCount("one"), { one: 1 }));
console.log(deepEqual(wordCount("a a a a a"), { a: 5 }));
console.log(deepEqual(
  wordCount("The quick brown fox jumps over the lazy dog"),
  { the: 2, quick: 1, brown: 1, fox: 1, jumps: 1, over: 1, lazy: 1, dog: 1 }
));
