def readBook(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def countWords(string):
    words = string.split()
    total_words = 0
    for word in words:
        total_words += 1
    print(total_words)

def main():
    string = readBook("books/frankenstein.txt")
    countWords(string)

main()