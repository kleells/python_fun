# Use a dictionary comprehension to count the length of
# each word in a sentence.

    # Input: "The quick brown fox jumped over the fence."

sentence = "The quick brown fox jumped over the fence."

# use String split() method to do this
print({word:len(word) for word in sentence.split()})