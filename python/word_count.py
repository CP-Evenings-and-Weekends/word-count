# count the quantity of each word in the sentence, repetition is good

def word_count(sentence):
    counts = {}
    sentence = sentence.lower()
    

    for word in sentence.split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


