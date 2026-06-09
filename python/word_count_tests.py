from word_count import word_count

print(word_count("the cat sat on the mat")) #== {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1})
print(word_count("Hello, hello! HELLO?")) #== {"hello": 3})
print(word_count("")) #== {})
print(word_count("one") )#== {"one": 1})
print(word_count("a a a a a")) #== {"a": 5})
print(word_count("The quick brown fox jumps over the lazy dog"))# == {
   # "the": 2, "quick": 1, "brown": 1, "fox": 1,
  #  "jumps": 1, "over": 1, "lazy": 1, "dog": 1
#})
