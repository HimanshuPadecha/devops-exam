def calculator(a,b, operaion):

    if operaion not in ["+", "-", "*", "/"]:
        return None

    if operaion == "+":
        return a + b
    elif operaion == "-":
        return a - b
    elif operaion == "*":
        return a * b
    elif operaion == "/":
        return a / b

    return None
    