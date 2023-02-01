
"""Math library for math operations"""

#-*- coding: utf-8 -*-




import math
from math import sqrt

class Random:

    def rnums(int, char, secondint):

        rint = (int)
        secondint = (int)
        cys = (char)
        seint = (secondint)

        sqrt = "√"

        mult = "*"

        potencia = "^"

        div = "÷"

        if cys == sqrt:
            raiz = math.sqrt(rint+seint)
            print(f"√{rint}+{seint} = ", raiz)

        elif cys == mult:
            multip = rint*seint
            print(f"{rint}*{seint} = ", multip)

        elif cys == potencia:
            up = rint^seint
            print(f"{rint}^{seint} = ", up)
        
        elif cys == div:
            divide = rint/seint
            print(f"{rint}÷{seint} = ", divide)