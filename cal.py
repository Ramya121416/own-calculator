import sys
class Cal:
    @staticmethod
    def val(d):
        if d == '*' or d == '/':
            return 4
        elif d == '+' or d == '-':
            return 3
        elif d == '(':
            return 1
        return 0

    @staticmethod
    def evaluate_expression(d):
        s1 = []  # Stack for numbers
        s2 = []  # Stack for operators
        i = 0  # Index to traverse the string

        while i < len(d):
            if d[i] == ' ':  
                i += 1
                continue
            if '0' <= d[i] <= '9': 
                num = 0
                while i < len(d) and '0' <= d[i] <= '9':  # Handle multi-digit numbers
                    num = num * 10 + int(d[i])
                    i += 1
                s1.append(num)  
                continue  
            elif d[i] == '(':  
                s2.append(d[i])
            elif d[i] == ')':  
              while s2 and s2[-1] != '(':
                    a = s1.pop()
                    b = s1.pop()
                    op = s2.pop()
                    f = Cal.apply_operation(b, a, op)
                    s1.append(f)
                s2.pop()  
            else:  
                while s2 and Cal.val(s2[-1]) >= Cal.val(d[i]):
                    a = s1.pop()
                    b = s1.pop()
                    op = s2.pop()
                    f = Cal.apply_operation(b, a, op)
                    s1.append(f)
                s2.append(d[i])
            i += 1  

        
        while s2:
            a = s1.pop()
            b = s1.pop()
            op = s2.pop()
            f = Cal.apply_operation(b, a, op)
            s1.append(f)

        
        print(s1.pop())

    @staticmethod
    def apply_operation(b, a, op):
        if op == '*':
            return b * a
        elif op == '/':
            return b // a  
        elif op == '+':
            return b + a
        elif op == '-':
            return b - a

f = sys.argv[1]
Cal.evaluate_expression(f)
# python3 cal.py  "example" 
