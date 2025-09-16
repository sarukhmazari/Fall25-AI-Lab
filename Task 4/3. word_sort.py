def sort_sentence(sentence: str) -> str:
    words = sentence.split()
    words.sort()  # sort function to sort the words alphabetically 
    return " ".join(words)


# Sentence
sentence = "we are leaning artificial intelligence"
print("Sorted Sentence:", sort_sentence(sentence))
