class InFixPost:
    def __init__(self):
        #initialize
        self.ops = []
        self.output = []

    def check_precedence(self, op):
        #checks for the order of the ops
        if op in ("+", "-"):
            return 1
        elif op in ("*", "/"):
            return 2
        elif op == "^":
            return 3
        return 0

    def right_associative(self, op):
        return op == "^"
    
    def checker(self, infix):
        self.ops = []
        self.output = []

        for char in infix:
            if char.isalnum():
                self.output.append(char)

            elif char == "(":
                self.ops.append(char)

            elif char == ")":
                while self.ops and self.ops[-1] != "(":
                    self.output.append(self.ops.pop())
                self.ops.pop()

            else:
                while (self.ops and self.ops[-1] != '(' and
                       (self.check_precedence(self.ops[-1]) > self.check_precedence(char) or
                        (self.check_precedence(self.ops[-1]) == self.check_precedence(char)
                         and not self.is_right_associative(char)))):
                    self.output.append(self.ops.pop())
                self.ops.append(char)

        while self.ops:
            self.output.append(self.ops.pop())

        print("Output:", "".join(self.output))

IP = InFixPost()

IP.checker("B+C*A")
IP.checker("(A+B)*C")
IP.checker("A*B+C*D")