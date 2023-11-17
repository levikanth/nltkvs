import spacy
import spacy.cli
# spacy.cli.download("en_core_web_sm")


sp_sm = spacy.load('en_core_web_sm')
# Load spaCy large English language model
sp_lg = spacy.load('en_core_web_sm')


def spacy_large_ner(document):
    # Process the document with spaCy large model
    doc = sp_lg(document)

    # Extract named entities
    entities = {(ent.text.strip(), ent.label_) for ent in doc.ents}

    return entities


# Example document
example_document = "Apple Inc. is a technology company based in Cupertino, California."

# Call the function with the example document
result = spacy_large_ner(example_document)

# Print the result
print(result)
