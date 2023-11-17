import spacy
import spacy.cli
spacy.cli.download("en_core_web_sm")
# Load the English language model in SpaCy
nlp = spacy.load("en_core_web_sm")

# Sample text for NER
text = "Apple Inc. is planning to open a new store in London next month."

# Process the text with SpaCy's NER
doc = nlp(text)

# Extract named entities
for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")
