t = int(input())
for _ in range(t):
   strs = input()
   stack = []
   for s in strs:
       if len(stack) == 0:
           stack.append(s)
       else:
           if stack[-1] == '(' and s == ')':
               stack.pop()
               continue
           else:
               stack.append(s)
   if len(stack) == 0:
       print("YES")
   else:
       print("NO")
