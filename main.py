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

def sort_on(dictionary):
    return dictionary["num"]


def sort_dict_to_list(dictionary):
    sorted_list = []
    for c in dictionary:
        sorted_list.append({"char": c, "num": dictionary[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list    

def main():
    book_name = "books/frankenstein.txt"
    string = read_book(book_name)
    word_count = count_words(string)
    print(f"{word_count} words were found in the book.")
    characters = count_characters(string)
    print(characters)
    report = sort_dict_to_list(characters)
    
    print(f"Beginning report for {book_name}")
    print(f"{word_count} words were found in the document.")
    print()

    for item in report:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times.")
    
    print("End report")

main()