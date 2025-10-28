def main():
    word = input("Enter word to check: ")
    print(is_palindrome(word))

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

if __name__ == "__main__":
    main()