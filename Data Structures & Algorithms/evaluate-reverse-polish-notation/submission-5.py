class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                second_val=stack.pop()
                first_val=stack.pop()
                x = int(first_val) + int(second_val)
                stack.append(x)
            elif token == "-":
                second_val=stack.pop()
                first_val=stack.pop()
                x = int(first_val) - int(second_val)
                stack.append(x)
            elif token == "*":
                second_val=stack.pop()
                first_val=stack.pop()
                x = int(first_val) * int(second_val)
                stack.append(x)
            elif token == "/":
                second_val=stack.pop()
                first_val=stack.pop()
                x = int(int(first_val) / int(second_val))
                stack.append(x)
            else:
                stack.append(token)
        val = stack.pop()
        return int(val)
        """
        you can pop to get an element off stack
        you can push to put an element onto stack
        you can peek to look at top element 

        [1,2+]

        so what im thinking right now is that i keep adding
        numbers onto the stack until i reach an operator

        once an operator is reached, then perform the operator on the 
        2 numbers and place the result back onto the stack

        then repeat the same process as we go on 

        so for example 

        [1]
        [1,2]
        [1,2,+] (reached a plus sign)

        so do 1+2 and append the result (3) back onto the stack 
        so now the stack is [3]

        keep going...

        [3]
        [3,3]
        [3,3,*]
        [9]
        [9,4]
        [9,4,-]
        [5] which is the expected output 

        When you pop two numbers, the second pop is actually the left number.


        stack = []

for token in tokens:
    if token is a number:
        put it on the stack
    else:
        take the last two numbers off the stack
        combine them using token
        put the result back

        """

        