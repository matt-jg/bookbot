from stats import number_of_words, count_each_character, create_sorted_list

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    raw_text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    num_words = number_of_words(raw_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    count_dict = count_each_character(raw_text)
    sorted_list = create_sorted_list(count_dict)

    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    

main()
