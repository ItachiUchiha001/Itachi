string=input("Enter Statement:")
vowels=0
consonants=0
lengthofwords=len(string)
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels=vowels+1
        consonants=lengthofwords-vowels
print("Number of vowels are:")
print(vowels)
print("Number of consonants are:")
print(consonants)
#program1
