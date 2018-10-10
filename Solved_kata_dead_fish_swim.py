#https://www.codewars.com/kata/make-the-deadfish-swim/train/python


def parse(data):
    data = str(data)
    val = 0
    final = []
    for value in data:
        if value == 'i': val += 1
        elif value == 'd': val -= 1
        elif value == 's': val = val ** 2
        elif value == 'o': final.append(val)
    return final


print(parse('isoisoiso'))

#--------------success-------------------------