def remove_punctuations(text: str) -> str:
    punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
    clean_text = ""

    for char in text:
        if char not in punctuations:
            clean_text += char
    return clean_text



sentence = "hello!!!, how are you?? I am Sarukh..."
print("Without Punctuations:", remove_punctuations(sentence))
