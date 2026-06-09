# word count function
def word_count(sentence):
    # convert to lowercase
    sentence_case = sentence.lower()
    # break sentence down into words
    words = sentence_case.split()
    # create empty dictionary to store word counts
    word_dict = {}

    # loop through each word to count them
    for word in words:
        
        # empty string to store the cleaned word
        clean = ""
        
        # loop through each character in the word
        for char in word:
            # keep only alphabetic characters
            if char.isalpha():
                # add the char to the cleaned word
                clean += char
    
        if clean in word_dict:
            # increment count if word already exists in dict
            word_dict[clean] += 1
        else:
            # add new word to dict with count of 1
            word_dict[clean] = 1

    # return the dictionary of word counts
    return word_dict
    pass
