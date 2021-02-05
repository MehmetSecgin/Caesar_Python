# Variables
c =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','','','','','','','','','','','','','','','','','','','','','','','','','','']
c1 = [0] * 26
result = ['']*1000
# The Input Sections
userInput = (input('Enter the message you want to Encrypt/Decrypt:')).upper()
choise = int(input('Press 0 to Encrypt, 1 to Decrypt:'))
key = int(input('Give the key you want to Encrypt or Decrypt: '))
# Functions
def makeSub(sub):
    for x in range(sub):
        c[x+26] = c[x]
    for y in range(26):
        c1[y] = c[sub+y]

def listToString(s):  
    str1 = ""   
    return (str1.join(s)) 
    
def encrypt():
    if(choise == 0):
        for x in range(len(userInput)):
            a = userInput[x]
            if(a == ' '):
                result[x] = a
            else:
                result[x]= c1[c.index(a)]
        print(listToString(result)) 
    else:
        for x in range(len(userInput)):
            a = userInput[x]
            if(a == ' '):
                result[x] = a
            else:
                result[x]= c[c1.index(a)]
        print(listToString(result))

# Main
makeSub(key)
encrypt()