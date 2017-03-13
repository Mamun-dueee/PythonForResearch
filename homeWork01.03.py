def counter(input_string):
    counter_letters = {}
    s = input_string
    c = counter_letters
    s = s.replace(' ', '')
    for i in range(len(s)):
        letter = s[i]
        c[letter] = s.count(letter)

    return counter_letters

