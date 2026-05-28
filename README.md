# Word Count

## Premise

Write a function that takes a sentence as a string and returns a dictionary (object in JS) where each **key** is a word and each **value** is how many times that word appears in the sentence.

This exercise is about practicing two things together: **iterating over a collection** and **building up a dictionary** as you go.

## Rules

- Words should be matched case-insensitively (`"The"` and `"the"` count as the same word).
- Punctuation should not be part of the word. `"hello,"` and `"hello"` count as the same word.
- The returned dictionary's keys should all be lowercase.

## Examples

```python
word_count("the cat sat on the mat")
# -> {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}

word_count("Hello, hello! HELLO?")
# -> {"hello": 3}

word_count("")
# -> {}
```

## Test Your Code

Run the test file in each language folder:
- Python: `python word_count_tests.py`
- JS: `node wordCountTests.js`

## Stretch

Once your tests pass, extend it: write a second function `most_common(sentence)` (Python) / `mostCommon(sentence)` (JS) that returns the single most-used word. If there's a tie, return any one of them.
