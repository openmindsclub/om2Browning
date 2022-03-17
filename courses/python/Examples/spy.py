'''
    the SPY life
'''

speakOfTheDevil = input("gimme encrypted sentence ")
sentenceWithNoSpecialChar = ""
'''
    removing special characters from the file
'''
for i in speakOfTheDevil:
    if (i>='a' and i <='z') or (i >='0' and i<='9') or i==' ' or (i>='A' and i <='Z'):
        sentenceWithNoSpecialChar = sentenceWithNoSpecialChar + i
'''
    reversing the word
'''
sentenceWithNoSpecialChar = sentenceWithNoSpecialChar[::-1]
'''
    printing out the output
'''
print(sentenceWithNoSpecialChar)