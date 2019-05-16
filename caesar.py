#This is a tutorial from the book Invent Your
#Own Computer Games with Python

#Caesar cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' #defines array with all possible characters
MAX_KEY_SIZE = len(SYMBOLS) #defines as length of variable SYMBOLS, range of 1-52

def getMode(): #function prompts user for encrypt or decrypt mode
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower() #makes all inputs lowercase
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            return mode
        else: #reprompt if wrong input
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage(): #function to get inputted msg from user
    print('Enter your message: ')
    return input()
    #message = input('Enter your message: ')

def getKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE)) #ask user for print input
        key = int(input()) #Converts typed string number into integer number
        if (key >= 1 and key <= MAX_KEY_SIZE): #if not in range, reprompt user
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key #if mode is decrypt, subtracts inputted key number
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: #Symbol not found in SYMBOLS
            #Just add this symbol without any change
            translated += symbol
        else:
            #Encrypt or decrypt
            symbolIndex += key
        if symbolIndex >= len(SYMBOLS):
            symbolIndex -= len(SYMBOLS)
        elif symbolIndex < 0:
            symbolIndex += len(SYMBOLS)

        translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode()
message = getMessage()
key = getKey()
print('Your translated text is: ')
print(getTranslatedMessage(mode, message, key)) #prints arguements