def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    # print(f"{num_letters} details of count of letters.")
    print_report(book_path, num_words, num_letters)


def print_report(file_path, words_count, data):
    print(f"--- Begin of {file_path} ---")
    print(f"{words_count} words found in the document.\n\n")
    for key, value in sorted(data.items(), key=lambda item: item[1], reverse=True):
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")



def get_num_letters(text):
    words = text.split()
    count_letters = {}
    for word in words:
        for letter in word.lower():
            if letter not in count_letters:
                count_letters[letter] = 0
            count_letters[letter] += 1
    return count_letters



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as file:
        return file.read()


if __name__ == "__main__":
    main()
