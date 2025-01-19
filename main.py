#!/usr/bin/env python3
def read_file(file):
    with open(file, 'r') as f:
        content = f.read()
    return content


def get_chars_dict(content):
    characters = {}
    for char in content.lower():
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    # sorted_list.sort(reverse=True, key=sort_on)
    sorted_list.sort(reverse=True, key=lambda x: x["num"])
    return sorted_list


def main():
    print("--- Begin report of books/frankenstein.txt ---")
    file = 'books/frankenstein.txt'
    content = read_file(file)
    words = content.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")
    chars_dict = get_chars_dict(content)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    for item in chars_sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times")


main()
