
"""Math library for math operations"""

#-*- coding: utf-8 -*-




import math
from math import sqrt
from termcolor import colored

class Random:

    def rnums(int, char, secondint):

        """Chars: ^, *, √, ÷, +, -"""

        rint = (int)
        seint = (int)
        cys = (char)
        seint = (secondint)

        sqrt = "√"

        mult = "*"

        potencia = "^"

        div = "÷"

        plus = "+"

        rest = "-"

        if cys == sqrt:
            raiz = math.sqrt(rint+seint)
            print(colored(f"√{rint}+{seint} = {raiz}", "yellow"))

        elif cys == mult:
            multip = rint+seint
            print(colored(f"{rint}*{seint} = {multip}", "yellow"))

        elif cys == potencia:
            up = rint**seint
            print(colored(f"{rint}^{seint} = {up}", "yellow"))
        
        elif cys == div:
            divide = rint/seint
            print(colored(f"{rint}÷{seint} = {divide}", "yellow"))
        
        elif cys == plus:
            sume = rint+seint
            print(colored(f"{rint}+{seint} = {sume}", "yellow"))
        
        elif cys == rest:
            reste = rint-seint
            print(colored(f"{rint}-{seint} = {reste}", "yellow"))