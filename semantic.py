import spacy

nlp = spacy.load('en_core_web_md')

# Example 1:

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print("Given example outcome: ")
print("\n")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

'''It is interesting that the module finds the similarities
 between the monkey and specifically the banana. Which means it
 recognises the association we have developed culturally.
 On the next given example the monkey and the apple dont have
 the same recognition even though they are fundamentally similar
 in the same way that the bannana and monkey. '''

print("\n")
    
# Example 1.1:

print("Test example outcome: ")
print("\n")

word1 = nlp("dog")
word2 = nlp("bone")
word3 = nlp("cat")
word4 = nlp('mouse')

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print(word1.similarity(word4))
print(word3.similarity(word4))
print(word2.similarity(word4))

'''Judging from the previous example I was not that suprised that
 the cat vs mousse similarity was 0.5.  The cat vs dog was also
 obvious and scored an 0.8. I was suprised that the dog vs bone
 didnt have a higher score (0.25). '''

print("\n")

nlp1 = spacy.load('en_core_web_sm')

# Example 1.2:

print("Given example outcome (using 'en_core_web_sm' : ")
print("\n")

word1 = nlp1("cat")
word2 = nlp1("monkey")
word3 = nlp1("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

'''When running the function through the more simple model
 I recieved a error/ warning relating to the inefficency of
 the model for the action required. I noticed the function
 found the cat more similar to the moneky then the bannana.
 The relational similarity scores were also a lot higher
 then the more accurate model. '''

print("\n")
    


# Example 2:

tokens = nlp('cat apple monkey banana ')

print("Given example 2: ")
print("\n")

for token1 in tokens:
 
 for token2 in tokens:
      print(token1.text, token2.text, token1.similarity(token2))

print("\n")

# Example 3:

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

print("Given example 3: ")
print("\n")

for sentence in sentences:
    
      similarity = nlp(sentence).similarity(model_sentence)
      print(sentence + " - ", similarity)
