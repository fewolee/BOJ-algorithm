while True:
    strs = input()
    if strs == '.':
        break
    stack = []
    for s in strs:
        if s == '(' or s == ')' or s == '[' or s == ']':
            if len(stack) ==0:
                stack.append(s)
                continue
            else:
                if stack[-1] == '(' and s ==')' or stack[-1] == '[' and s ==']':
                    stack.pop()
                else:
                    stack.append(s)

    if len(stack) == 0:
        print('yes')
    else:
        print('no')