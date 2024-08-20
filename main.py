def main():
    with open("books/frankenstein.txt") as f:
        filecontents = f.read()
    def word_count(text):
        text_len = len(text.split())
        return(text_len)
    #print(word_count(filecontents))
    def char_count(text):
        words = text.split()
        chars = {}
        for word in words:
            for char in word:
                char = char.lower()
                if char in chars:
                    chars[char] += 1
                else:
                    chars[char] = 1
        return(chars)
    def report(dict):
        char_list = []
        w_count = word_count(filecontents)
        
        header = "--- Begin report of books/frankenstein.txt ---\r"
        sub_header = f" {w_count} words found in document \n \n"
        footer = "--- End report ---"

        for item in dict:
            if item.isalpha():
                char_list.append(item)
        char_list.sort()

        list_len = len(char_list)
        print(header)
        print(sub_header)
        for i in range(0, list_len):
            letter = char_list[i]
            count = dict[letter]
            print(f"The '{letter}' character was found {count} times\r")
        print(footer)
    
    character_list = char_count(filecontents)
    report(character_list)
    




main()
