import math
import re

def get_operation(operator, X, Y):
    valid_operation = ["addition", "subtraction", "multiplication"]
    if operator in valid_operation:
        if math.isnan(X) or math.isnan(Y):
            return None, operator
        else:
            if operator == "addition":
                return X + Y, operator
            elif operator == "subtraction":
                return X - Y, operator
            else:
                return X * Y, operator
    else:
        # perform the regular expression:
        get_expression = perform_reg(operator)
        if len(get_expression) != 0:
            get_X = X
            get_Y = Y
            return get_operation(get_expression, get_X, get_Y)
        return None, operator
        
def perform_reg(opr):
    new_operation = ''
    splitted_word = opr.split()
    regex = '(add)|(sub)|(mul)|(take)|(plus)|(product)|(sum)|(minus)|(times)|[+]|[-]|[*]'
    for i in splitted_word:
        mat = re.search(regex, i.strip())
        if mat is not None:
            new_operation = rephrase_operation(mat.group())
            break
    return new_operation

def rephrase_operation(opera) -> str:
    if opera in ["add","sum","plus","+"]:
        return "addition"
    elif opera in ["minus", "sub","take", "-"]:
        return "subtraction"
    elif opera in ["mul", "product", "times", "*"]:
        return "multiplication"
    else:
        return ""