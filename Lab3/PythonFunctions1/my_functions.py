def histogramm(list):
    for i in list:
        print("*"*i)

def palindrome(word):
    word = list(word)
    if word == word[::-1]:
        return True
    return False

def unique_list(list):
    uniquelist=[]
    for i in list:
        if i not in uniquelist:
            uniquelist.append(i)
    return uniquelist