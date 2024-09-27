def answer(question):
    equation = question.removeprefix("What is").removesuffix("?").strip()
    
    if not equation:
        raise ValueError("syntax error")
    if equation.isnumeric():
        return int(equation)

    equation = equation.replace("plus", "+").replace("minus", "-").replace("multiplied by", "*").replace("divided by", "/").split()
    
    for i in equation:
        if i.isalpha():
            raise ValueError("unknown operation")

    equation.insert(0, "(")
    equation.insert(4, ")")
    
    try:
        int(equation[1])
        return eval("".join(equation))
    except:
       raise ValueError("syntax error")
