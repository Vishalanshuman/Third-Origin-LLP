import argparse

def count_words(file_path: str) -> int:
    """
    Count the total number of words in the text file.

    Parameters:
        file_path (str): The path to the input text file.

    Returns:
        int: The total number of words in the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return len(text.split())

def count_characters(file_path: str) -> int:
    """
    Count the total number of characters in the text file.

    Parameters:
        file_path (str): The path to the input text file.

    Returns:
        int: The total number of characters in the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return len(text)

def count_lines(file_path: str) -> int:
    """
    Count the total number of lines in the text file.

    Parameters:
        file_path (str): The path to the input text file.

    Returns:
        int: The total number of lines in the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return sum(1 for line in file)

def find_word(file_path: str, word: str) -> int:
    """
    Search for a specific word in the text file and display its frequency.

    Parameters:
        file_path (str): The path to the input text file.
        word (str): The word to search for.

    Returns:
        int: The frequency of the word in the text file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text.lower().split().count(word.lower())

def replace_word(file_path: str, old_word: str, new_word: str) -> str:
    """
    Replace a word in the text file with another word and save it as a new file.

    Parameters:
        file_path (str): The path to the input text file.
        old_word (str): The word to be replaced.
        new_word (str): The word to replace with.

    Returns:
        str: The path to the modified file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    modified_text = text.replace(old_word, new_word)
    new_file_path = file_path.replace('.txt', '_modified.txt')
    with open(new_file_path, 'w', encoding='utf-8') as new_file:
        new_file.write(modified_text)
    return new_file_path

def main():
    parser = argparse.ArgumentParser(description="Process a text file with various operations.")
    parser.add_argument('-f', '--file', required=True, help="Path to the input text file.")
    parser.add_argument('-wc', '--word-count', action='store_true', help="Display the total word count.")
    parser.add_argument('-cc', '--char-count', action='store_true', help="Display the total character count.")
    parser.add_argument('-lc', '--line-count', action='store_true', help="Display the total line count.")
    parser.add_argument('-find', '--find', help="Search for a specific word in the text file.")
    parser.add_argument('-r', '--replace', nargs=2, metavar=('old_word', 'new_word'), help="Replace a word in the text file with another word.")

    args = parser.parse_args()

    try:
        if args.word_count:
            word_count = count_words(args.file)
            print(f"Total word count: {word_count}")

        if args.char_count:
            char_count = count_characters(args.file)
            print(f"Total character count: {char_count}")

        if args.line_count:
            line_count = count_lines(args.file)
            print(f"Total line count: {line_count}")

        if args.find:
            word_frequency = find_word(args.file, args.find)
            print(f"The word '{args.find}' appears {word_frequency} times in the file.")

        if args.replace:
            old_word, new_word = args.replace
            new_file_path = replace_word(args.file, old_word, new_word)
            print(f"Replaced '{old_word}' with '{new_word}'. Modified file saved as: {new_file_path}")

    except FileNotFoundError:
        print(f"Error: The file '{args.file}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
