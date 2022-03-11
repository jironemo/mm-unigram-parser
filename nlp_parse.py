import re


myanmar_character_sequence_matrix = [
    #c v m
    [1,1,1],#con
    [0,0,0],#vol
    [0,1,1],#medial
]
burmese_consonants = ['က','ခ','ဂ','ဃ','င',
                      'စ','ဆ','ဇ','ဈ','ည',
                      'ဋ','ဌ','ဍ','ဎ','ဏ',
                      'တ','ထ','ဒ','ဓ','န',
                      'ပ','ဖ','ဗ','ဘ','မ',
                      'ယ','ရ','လ','ဝ','သ',
                           'ဟ','ဠ','အ','ဦ']

burmese_vowels = ['ာ','ါ','ေ','ဲ','့','ိ','ီ','ံ','ု','ူ','း','ြ','ျ','ွ']
athat = ['က်','ခ်','င်','စ်','ဇ်','ည်','ဋ်','ဏ်','တ်','ဒ်','န်','ပ်','မ်','ယ်','ဠ်']
def isValid(prevchar,cha,nextchar):
    #if prevchar is empty and current char is a consonant, that's the start, hence still valid.
    if ((prevchar == '') and(cha in burmese_consonants)):
        return True
    #if prevchar is a consonant
    elif(prevchar in burmese_consonants):
        #if 2 consonants in a row, that's two seperate words, hence no more valid.
        if (cha in burmese_consonants):
            print(cha+nextchar)
            if(cha + nextchar in athat):
                return True
            else:
                return False
        #if consonant and vowel, it's still valid.
        if(cha in burmese_vowels):
            return True

    #if prevchar is a vowel
    elif(prev_char in burmese_vowels):
        #if the current character is a consonant, it's a separate word, hence not valid anymore.
        if(cha in burmese_consonants):
            return False
        #if the current character is one of ာ,ါ,‌ေ,ီ,ိ,ူ and the current character is း , it's still valid.
        elif ((prevchar == 'ာ' or prevchar == 'ါ' or prevchar == '‌ေ' or prevchar =='‌ီ'or prevchar =='‌ူ') and (cha == 'း')):
            return True
        elif(cha in burmese_vowels):
            return True
    elif((prevchar == 'ျ') and (cha == 'ူ')):
        return True

cin = (input("Enter a Myanmar text: "))
prev_char = cin[0]
print(cin[0])
combined = prev_char
for i in range(1,len(cin)):
    cur_char = cin[i]
    if(i < len(cin)-1):
        nextchar = cin[i+1]
        if(nextchar != '်'):
            nextchar = ''
    else:
        nextchar = ''
    if (isValid(prev_char,cur_char,nextchar) == True):
        open("Validity.txt",'a',encoding="UTF-8").write(prev_char+cur_char + " is still valid") 
        if(nextchar == ''):
            combined = combined + cur_char
            prev_char = cur_char
        else:
            combined = combined+cur_char+nextchar
            prev_char = ''
    else:
        open("Text.txt","a",encoding="UTF-8").write("{} ".format(combined))
        open("Validity.txt",'a',encoding="UTF-8").write(prev_char+cur_char + " is not valid")
        combined = cur_char