def is_paired(input_string):
    stack = []
    brackets = {']': '[', '}': '{', ')': '('}
    
    for i in input_string:
        if i in brackets.values():
            stack.append(i)
        elif i in brackets.keys():
            if not stack or stack.pop() != brackets[i]:
                return False

    return not stack
        
