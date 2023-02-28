word1="abccba"
word2="dgjuiafja"
def palindrom(word):
    for i in range(0, len(word)):
            if(word[i] != word[len(word) - 1 - i]):
                  return False
            else:
                continue
    return True



if palindrom(word2) == True:
    print("To jest palindrom")
else:
    print("To nie jest palindrom")