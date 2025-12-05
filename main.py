from stats import count_words
from stats import count_characters
from stats import sort_data
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    
    if not len(sys.argv) > 1:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file=sys.argv[1]
    file_contents = get_book_text(path_to_file)
    word_count = count_words(file_contents)
    
    character_count = count_characters(file_contents)
    
    print(f"Found {word_count} total words")

    s_chars = sort_data(character_count)

    for i in s_chars:
        a = i["char"]
        b = i["num"]

        if not a.isalpha():
            continue

        print(f"{a}: {b}")

main()
