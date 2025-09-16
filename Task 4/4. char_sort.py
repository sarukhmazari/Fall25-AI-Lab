def sort_by_chars(sentence: str) -> str:
    chars = list(sentence.replace(" ", ""))  
    chars.sort()                             
    return "".join(chars)


sentence = "we are leaning artificial intelligence"
print("Sorted by Characters:", sort_by_chars(sentence))
