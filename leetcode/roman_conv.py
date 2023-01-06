
# %%
"""
TODO:
* type check - int_to_roman -> int
* try - catch error handling
"""


def roman_to_integer(roman):

    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    inputlist = list(str(roman))
    out = 0
    prev = 1000
    while len(inputlist) > 0:
        
        if inputlist[0] in values.keys():
            curr = values[inputlist.pop(0)]
            if curr > prev:
                out -= prev * 2
            
            out += curr

            prev = curr
            
        else:
            raise ValueError

    return out


def int_to_roman(i):

    # input csekk - ha az int(i) elhasal, rossz volt az input.
    i = int(i)


    # 1000-es helyiérték feltöltése 'M'-ekkel
    out = 'M' * (i // 1000)

    # 100-as helyiérték feltöltése
    r = {
        1: 'C',
        2: 'CC',
        3: 'CCC',
        4: 'CD',
        5: 'D',
        6: 'DC',
        7: 'DCC',
        8: 'DCCC',
        9: 'CM',
        0: ''
    }
    out += r[i // 100 % 10]

    # 10-es helyiérték feltöltése
    r = {
        1: 'X',
        2: 'XX',
        3: 'XXX',
        4: 'XL',
        5: 'L',
        6: 'LX',
        7: 'LXX',
        8: 'LXXX',
        9: 'XC',
        0: ''
    }
    out += r[i // 10 % 10]

    # 1-es helyiérték feltöltése
    r = {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII',
        9: 'IX',
        0: ''
    }
    out += r[ i % 10 ]

    return out


    

# load sample roman numbers from file
romanlist = []
with open('roman_sample.txt', 'r', encoding='UTF-8') as file:
    while (line := file.readline().rstrip()):
        l = line.split()
        if len(l) == 3:
            romanlist.append((int(l[0]),l[2]))


# test int to roman conversion
for l in romanlist:
    r = int_to_roman(l[0])
    if r != l[1]:
        print(l,r)

# test roman to int conversion
for l in romanlist:
    i = roman_to_integer(l[1])
    if i != l[0]:
        print(l,i)


