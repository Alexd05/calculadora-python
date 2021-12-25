print("""operadores 

**suma: suma dos números**

**resta: resta dos números** 

**multiplicación: multiplica dos números**

**división: divide dos números** 

**potencia: eleva un número a otro número**

**resto: muestra lo restante de una división**\n""")

sign = input("qué tipo de cuenta quiere hacer? ")

if "suma" in sign:
    print("calculadora: suma \n\n")
    x = input("ingrese el primer número ")
    y = input("ingrese el segundo número ")

    x2 = float(x)
    y2 = float(y)

    res = x2 + y2 

    print(f"el resultado de la suma es {res} \n\n")

elif "resta" in sign:
    pass
    print("calculadora: resta \n\n")
    x = input("ingrese el primer número ")
    y = input("ingrese el segundo número ")

    x2 = float(x)
    y2 = float(y)

    res = x2 - y2 

    print(f"el resultado de la resta es {res} \n\n")


elif "multiplicación" in sign:
    pass
    print("calculadora: multiplicación \n\n")
    x = input("ingrese el primer número ")
    y = input("ingrese el segundo número ")

    x2 = float(x)
    y2 = float(y)

    res = x2 * y2 

    print(f"el resultado de la multiplicación es {res} \n\n")


elif "división" in sign:
    pass
    print("calculadora: división \n\n")
    x = input("ingrese el primer número ")
    y = input("ingrese el segundo número ")

    x2 = float(x)
    y2 = float(y)

    res = x2 / y2 

    print(f"el resultado de la división es {res} \n\n")

elif "potencia" in sign:
    pass
    print("calculadora: potencia \n\n")
    x = input("ingrese el primer número ")
    y = input("ingrese la elevación ")

    x2 = float(x)
    y2 = float(y)

    res = x2 ** y2 

    print(f"el resultado de la potencia es {res} \n\n")

elif "resto" in sign:
    pass
    print("calculadora: resto \n\n")
    x = input("ingrese el primer número ")
    y = input("ingrese el segundo número ")

    x2 = float(x)
    y2 = float(y)

    res = x2 % y2 

    print(f"el resultado de la resto es {res} \n\n") 
