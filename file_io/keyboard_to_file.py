def keyboardfile():
    file = open("C:/io/keyboard.txt","w")
    text = input("enter your message = ")

    while(text !="quite"):
        file.write(text)
        file.write("\n")
        text = input('')
    file.close()
keyboardfile()