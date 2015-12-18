#?/usr/beqin/env python

#Base q representation

import math

def to_base_10(number,givenBase):
    strBase = str(number)
    base10 = 0
    for i in range(0, len(strBase)):
        base10 += int(strBase[i])*math.pow(givenBase,len(strBase) - (i+1))
    return int(base10)


def to_base_q(base10, baseQ):
    x = base10
    str_forward = ""
    while x != 0:
        str_append = str(x % baseQ)
        str_forward += str_append
        x = (x - int(str_append))/baseQ
        
    return int(str_forward[::-1])


number = int(raw_input("Number to convert: "))

originalBase = int(raw_input("What base is "+ str(number) + " in? "))


ConvertTo = int(raw_input("Convert " + str(number) + " base " +
                str(originalBase) + " to what base? "))

result = to_base_q(to_base_10(number, originalBase), ConvertTo)

print number, "in base", originalBase, " == ", result, "in base", ConvertTo