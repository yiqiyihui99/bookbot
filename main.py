import sys
from stats import get_num_words, get_num_chars, get_sorted_chars

def get_book_text(file):
    with open(file) as f:
        return f.read()

def main():
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    print("============ BOOKBOT ============")
    print("Analyzing book found at ${path}")
    print("----------- Word Count ----------")
    print(get_num_words(text))
    print("--------- Character Count -------")
    sorted_chars = get_sorted_chars(get_num_chars(text))
    for char in sorted_chars:
        if (char["char"].isalpha()):
            print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

main()