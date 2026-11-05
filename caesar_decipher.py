def main():
    print("1 for encryption\n2 for decryption")
    choice = input("choice: ")
    match choice:
        case "1":
            sentence = input("enter sentence to encrypt: ")
            key = input("key to encrypt with: ")
            char_list = list(sentence)
            new_char_list = []
            for char in char_list:
                if(int(key)>0):
                    for i in range(0,int(key),1):
                        if char != " " and char != "z" and char != "Z":
                            char = chr(ord(char) + 1)
                        elif char == " ":
                            char
                        elif char == "z":
                            char = "a"
                        elif char == "Z":
                            char = "A"
                        else:
                            continue
                    new_char_list.append(char)
                else:
                    for i in range(0,int(key),-1):
                        if char != " " and char != "a" and char != "A":
                            char = chr(ord(char) + 1)
                        elif char == " ":
                            char
                        elif char == "a":
                            char = "z"
                        elif char == "A":
                          char = "Z"
                        else:
                            continue
                    new_char_list.append(char)
            sentence = "".join(new_char_list)
            print(sentence)
        case "2":
            sentence = input("enter sentence to decrypt: ")
            key = input("key used to encrypt: ")
            char_list = list(sentence)
            new_char_list = []
            for char in char_list:
                if(int(key)>0):
                    for i in range(0,int(key),1):
                        if char != " " and char != "z" and char != "Z":
                            char = chr(ord(char) - 1)
                        elif char == " ":
                            char
                        elif char == "z":
                            char = "a"
                        elif char == "Z":
                            char = "A"
                        else:
                            continue
                    new_char_list.append(char)
                else:
                    for i in range(0,int(key),-1):
                        if char != " " and char != "a" and char != "A":
                            char = chr(ord(char) - 1)
                        elif char == " ":
                            char
                        elif char == "a":
                            char = "z"
                        elif char == "A":
                            char = "Z"
                        else:
                            continue
                    new_char_list.append(char)
            sentence = "".join(new_char_list)
            print(sentence)
        case _: 
            print("invalid input")



if __name__ == "__main__":
    main()