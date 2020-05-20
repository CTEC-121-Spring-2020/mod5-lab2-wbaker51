"""
CTEC 121
<your name>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""
# practice 1
def verse(name):
    print(name, "finger,", name, "finger, where are you?")

def refrain():    
    print("Here I am, here I am. How do you do?")
    print()

def singFamilySong():
    '''
    print()
    verse("Daddy")
    refrain()
    verse("Mommy")
    refrain()
    verse("Brother")
    refrain()
    verse("Sister")
    refrain()
    verse("Baby")
    refrain()
    '''
    print()
    for name in ["Daddy", "Mommy", "Brother", "Sister", "Baby"]:
        verse(name)
        refrain()

def main():
    singFamilySong()

#main()    

# practice 2

def AgeClassification(age):
    if age < 2:
        return 'I'
    elif age < 13:
        return 'C'
    elif age < 18:
        return 'T'
    elif age <= 125:
        return 'A'
    else:
        return 'U'

def testAgeClassification():
    print()
    print(AgeClassification(-1), "expect U: -1 input")
    print(AgeClassification(0), "expect I: 0 input")
    print(AgeClassification(1), "expect I: 1 input")
    print(AgeClassification(2), "expect C: 2 input")
    print(AgeClassification(12), "expect C: 12 input")
    print(AgeClassification(13), "expect T: 13 input")
    print(AgeClassification(17), "expect T: 17 input")
    print(AgeClassification(18), "expect A: 18 input")
    print(AgeClassification(100), "expect A: 100 input")
    print(AgeClassification(125), "expect A: 125 input")
    print(AgeClassification(126), "expect U: 126 input")

    print()

testAgeClassification()