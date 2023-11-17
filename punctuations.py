import string

def remove_punctuation(text):
    # Create a translation table to remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    
    # Remove punctuation using translate method
    text_without_punctuation = text.translate(translator)
    
    return text_without_punctuation

# Sample document
document = "This, is a sample text! It has punctuation marks: like commas, and periods."

# Remove punctuation from the document
cleaned_document = remove_punctuation(document)

# Print the document without punctuation
print("Document without punctuation:")
print(cleaned_document)