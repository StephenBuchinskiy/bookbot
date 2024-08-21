def read_book(file):
    with open(file) as f:
        return f.read()

def count_words(string):
    words = string.split()
    return len(words)

def count_characters(string):
    lowered_string = string.lower()
    dictionary = dict()
    for character in lowered_string:
        if character not in dictionary:
            dictionary[character] = 1
        else:
            dictionary[character] += 1
    
    return dictionary

def main():
    string = read_book("books/frankenstein.txt")
    word_count = count_words(string)
    print(f"{word_count} words were found in the book.")
    characters = count_characters(string)
    print(characters)

main()