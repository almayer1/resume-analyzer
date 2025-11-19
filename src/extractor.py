#normalize data
def normalize(data: str) -> str:
    result = ""
    for char in data:
        if (char == "•" or char == "." or char == "," or char == "(" or char == ")" or char == ":"):
            continue
        result += char
    result = result.lower()
    return result

#convert string to list and clean up
def cleanup(data: str) -> list:
    JUNK = ["of", "in", "a", "the", "to", "and", "with", "for", "their", "that", "from", "help", "interested", "relevant", "coursework", "fundamentals", "expected", "or", "later", "built", "by", "–", "interest", "we", "our", "example", "what", "you", "will", "are", "how", "as", "used", "on", "at", "including", "related", "location", "involving", "clearly", "using", "join", "across", "understand", "concepts"]
    result = data.split()

    #remove junk words
    for word in JUNK:
        for i in range(result.count(word)):
            result.remove(word)

    #remove duplicates
    for word in result:
        for i in range(result.count(word)):
            if (i == 0):
                continue
            result.remove(word)
    return result




#sort?



