def main():
    # Open the file in read mode
    with open("books/frankenstein.txt") as f:
        # Read the file
        file_contents = f.read()
        print(print_report(file_contents))

def count_words(file_contents):
    # Split the file contents into words
    words = file_contents.split()
    # Count the number of words
    word_count = len(words)
    # Return the word count
    return word_count

def count_characters(file_contents):
    character_count = {}
    for character in file_contents:
        character = character.lower()
        if character.isalpha():
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1
    return character_count

def print_report(file_contents):
    word_count = count_words(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print("\n")
    print(f"{word_count} words found in the document")
    character_count = count_characters(file_contents)
    for character, count in character_count.items():
        print(f"The '{character}' character was found {count} times")
    print("\n")
    print("--- End report ---")

main()
