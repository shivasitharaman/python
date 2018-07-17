def startEndVowels(word):
    vowels = "aeiou"
    x = word[0]
    y = word[-1]
    z = len(word)
    if z >1:
       if x in vowels:
          if y in vowels:
             return True
       else:
            return False
    elif z == 1:
         if word in vowels:
            return True
         elif x == " ":
              return False
print startEndVowels("apple")
print startEndVowels("goole")
print startEndVowels("A")