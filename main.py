def main():
    path = "books/frankenstein.txt"
    text = get_file_contents(path)
    word_count = count_words(text)
    character_count = count_characters(text)
    create_report(path, word_count, character_count)
def sorton(dict):
    return dict[1]
def get_file_contents(path):
    with open(path) as f:
        return f.read()
def count_words(text):
    words = text.split()
    return len(words)
def count_characters(text):
    character_dict = {}
    for char in text:
        if not char.isalpha():
            continue
        lowered = char.lower()
        if lowered in character_dict:
            character_dict[lowered] += 1
        else:
            character_dict[lowered] = 1
    return character_dict
def create_report(path, word_count, char_dict):
    char_list = []
    for key in char_dict:
        char_list.append((key, char_dict[key]))
    char_list.sort(reverse=True, key=sorton)
    print(f"-- Begin report of {path} --")
    print(f"{word_count} words found in the document.\n")
    for char, count in char_list:
        print(f"The '{char}' character was found {count} times.")
    print("\n-- End of report --")
main()