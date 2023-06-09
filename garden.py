

import spacy # Import the spaCy module

nlp = spacy.load('en_core_web_md') # I used md instead of sm to get a larger named entity recognition

# Create a list of sentences and store in the variable named gardenpathSentences
gardenpathSentences = ["The horse raced past the barn fell.",
                       "The complex houses married and single soldiers and their families.",
                       "Mary gave the child a Band-Aid","That Jill is never here hurts",
                       "The cotton clothing is made of grows in Mississippi"]

# Iterate through the list to extracte strings from the lists   
for sentence in gardenpathSentences:
    nlp_sentence = nlp(sentence)
    print([token.orth_ for token in nlp(sentence)])    # Tokenise the sentences
    print([(i, i.label_, i.label) for i in nlp_sentence.ents])    # Perform the named entity recognition                 

# Print the explaination of two entities resulting from the named entity recognition        
print(spacy.explain("GPE"))
print(spacy.explain("ORG"))



