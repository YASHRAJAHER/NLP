import spacy

nlp = spacy.load("en_core_web_sm")

example_string = "My name is Yashraj. I am clever student. I am in final year."
doc = nlp(example_string)

print("Sentence Tokenization:")
for sent in doc.sents:
    print(sent.text)

print("\nWord Tokenization:")
for token in doc:
    print(token.text)

print("\nFiltered Words (without stopwords and punctuation):")
filtered_tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
print(filtered_tokens)

print("\nLemmatization:")
lemmatized_tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
print(lemmatized_tokens)

print("\nNamed Entities:")
for ent in doc.ents:
    print(f"{ent.text} ({ent.label_})")

print("\nPart-of-Speech Tags:")
for token in doc:
    print(f"{token.text} --> {token.pos_}")
