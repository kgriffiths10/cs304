class ArrayStack:
    """LIFO Stack implementation"""
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self._data[-1]


class Expression:
    def __init__(self, input_str, direction):
        self._infix = ''
        self._postfix = ''
        self._stack = ArrayStack()
        if direction == 0:
            self._infix = input_str
        elif direction == 1:
            self._postfix = input_str

    def in_to_post(self):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        output = ''
        for token in self._infix.split():
            if token.isalnum():
                output += token + ' '
            elif token == '(':
                self._stack.push(token)
            elif token == ')':
                while self._stack.top() != '(':
                    output += self._stack.pop() + ' '
                self._stack.pop()  # Discard '('
            else:
                while (not self._stack.is_empty() and
                       precedence.get(self._stack.top(), 0) >= precedence.get(token, 0)):
                    output += self._stack.pop() + ' '
                self._stack.push(token)
        while not self._stack.is_empty():
            output += self._stack.pop() + ' '
        self._postfix = output.strip()
        return self._postfix

    def post_to_in(self):
        for token in self._postfix.split():
            if token.isalnum():
                self._stack.push(token)
            else:
                operand2 = self._stack.pop()
                operand1 = self._stack.pop()
                self._stack.push(f'({operand1} {token} {operand2})')
        self._infix = self._stack.pop()
        return self._infix

    def evaluate(self):
        operands = {'+': lambda x, y: x + y,
                    '-': lambda x, y: x - y,
                    '*': lambda x, y: x * y,
                    '/': lambda x, y: x / y,
                    '^': lambda x, y: x ** y}
        for token in self._postfix.split():
            if token.isalnum():
                self._stack.push(int(token))
            else:
                operand2 = self._stack.pop()
                operand1 = self._stack.pop()
                result = operands[token](operand1, operand2)
                self._stack.push(result)
        return self._stack.pop()


def main():
    print("Convert and solve infix and postfix expressions!")
    while True:
        expression_str = input("Enter the expression (leave spaces around operators): ")
        direction = int(input("Enter the direction (0 for infix, 1 for postfix): "))
        expression = Expression(expression_str, direction)

        if direction == 0:
            postfix_expression = expression.in_to_post()
            print("Postfix expression:", postfix_expression)
            result = expression.evaluate()
            print("Result of evaluation:", result)
        elif direction == 1:
            infix_expression = expression.post_to_in()
            print("Infix expression:", infix_expression)
            result = expression.evaluate()
            print("Result of evaluation:", result)

        another_conversion = input("Do you want to perform another conversion? (y/n): ")
        if another_conversion.lower() != "y":
            break
        
if __name__ == "__main__":
    main()