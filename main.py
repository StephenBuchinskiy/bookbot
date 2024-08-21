def readBook(file):
    with open(file) as f:
        return f.read()

def countWords(string):
    words = string.split()
    return len(words)

def main():
    string = readBook("books/frankenstein.txt")
    word_count = countWords(string)
    print(f"{word_count} words were found in the book.")

main()