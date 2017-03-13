sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}
#write your code here!
s = sentence
c = count_letters
s = s.replace(' ', '')
for i in range(len(s)): 
    letter = s[i]
    c[letter] = s.count(letter)
    
print(c)
