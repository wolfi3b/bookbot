def count_words(text):
    return len(text.split())

def count_chars(text):
    dict = {};
    for char in text.lower():
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    
    return dict



def main():
    with open("./books/frankenstein.txt") as f:
        text = f.read()
        # print(text)
        print('--- Begin report of books/frankenstein.txt ---')
        print(f"{count_words(text)} words found in the document");
        ditct = count_chars(text)
        for key in ditct:
            if(key.isalpha()):
                print(f"The '{key}' character was found {ditct[key]} tiumes")
        print('--- End report ---')

main();