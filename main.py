def wordCount(text):
    return len(text.split())

def charFrequencies(text):
    f = {}
    for char in text:
        char = char.lower()
        if char >= 'a' and char <= 'z':
            f[char] = f.get(char,0) + 1

    sorted_dict = dict(sorted(f.items(), key=lambda x: x[1], reverse=True))
    return sorted_dict

def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        wc = wordCount(file_contents)
        
        freq = charFrequencies(file_contents)
        
        print(f"--- Begin report of {path} ---")
        print(f"{wc} words found in the document")
        for char, count in freq.items():
            print(f"'{char}' was found {count} times.")

main()
