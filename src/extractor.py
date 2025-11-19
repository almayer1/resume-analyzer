#normalize data
def normalize(data: str) -> str:
    result = ""
    for char in data:
        if (char == "•" or char == "." or char == "," or char == "(" or char == ")" or char == ":"):
            continue
        result += char
    result = result.lower()
    return result

#convert string to list and remove junk words
def cleanup(data: str) -> list:
    JUNK = ["of", "in", "a", "the", "to", "and", "with", "for", "their", "that", "from", "help", "interested", "relevant", "coursework", "fundamentals", "expected"]
    result = data.split()
    for word in JUNK:
        for i in range(result.count(word)):
            result.remove(word)
    return result

#tokenize



#sort?



