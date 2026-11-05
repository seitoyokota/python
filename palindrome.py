def main():
    while(1):
        word = input("word: ")
        if(len(word)%2==0):
            word1 = word[:len(word)//2]
            word2 = word[len(word)//2:len(word)]
            if(word1==word2[::-1]):
                print("palindrome")
            else:
                print("not palindrome")
        else:
            word1 = word[:len(word)//2]
            word2 = word[(len(word)//2)+1:len(word)]
            if(word1==word2[::-1]):
                print("palindrome")
            else:
                print("not palindrome")
        choice = input("1 to again, 0 to stop: ")
        if(choice==0):
            break

if __name__ == "__main__":
    main()