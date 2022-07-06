testCases = [
    ('IV', 4),
    ('IX', 9),
    ('XL',40),
    ('XC',90),
    ('CD',400),
    ('CM',900),    
    ('CMVIII',908),
    ('DCXXVI',626),
    ('DCXXXIII',633),
    ('CCXLVII',247),
    ('CDLXXIII',473),
    ('CXCVI',196),
    ('CCXLI',241),
    ('DCCCXXVII',827),
    ('CDXIV',414),
    ('LXXIX',79),
    ('MMMMMMXXXIII',6033),
    ('MMMMCML',4950),
    ('MMMMMMMMMDCCCXLIX',9849),
    ('MMMMMMMCCCLXXXI',7381),
    ('MMMMMMMCMXLII',7942),
    ('MMMMMMMMDCCCXIII',8813),
    ('MMMMDCCCLXXXIII',4883),
    ('MMMMMMCCXXVIII',6228),
    ('MMCMXC',2990),
    ('MMMMMMMDLXXXVII',7587)
]

decoder = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

"""
Special Cases
IV
IX
XL
XC
CD
CM
"""

def decode_roman(cases):
    for index, item in enumerate(cases):
        (roman, answer) = item
        values = [] # keep track of decoded values
        length=len(roman)
        letters = list(reversed(roman))
        
        for index2, letter in enumerate(letters):
            value = decoder[letter]
            if index2>0:
                if letter == 'I':
                    if letters[index2-1] in ['V','X']:
                        values.append(-1)
                    else:                    
                        values.append(value)
                elif letter == 'X':
                    if letters[index2-1] in ['L','C']:
                        values.append(-10)
                    else:                    
                        values.append(value)                    
                elif letter == 'C':
                    if letters[index2-1] in ['D','M']:
                        values.append(-100)
                    else:                    
                        values.append(value)
                else:                    
                    values.append(value)
            else:
                values.append(value)

        total = sum(values)

        if total == answer:
            print(f"Correct {roman} equals {answer}")
        else:
            print(f"Error {roman} equals {answer} not {total}")



def decode_roman_v2(cases):
    for index, item in enumerate(cases):
        (roman, answer) = item
        values = [] # keep track of decoded values
        length=len(roman)
        letters = list(reversed(roman))
        
        for index2, letter in enumerate(letters):
            value = decoder[letter]
            if index2>0:
                value2 = decoder[letters[index2-1]]
                if value2 > value:
                    values.append(-value)
                else:                    
                    values.append(value)
            else:
                values.append(value)

        total = sum(values)

        if total == answer:
            print(f"Correct {roman} equals {answer}")
        else:
            print(f"Error {roman} equals {answer} not {total}")


#decode_roman(testCases)
decode_roman_v2(testCases)