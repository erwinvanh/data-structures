# python2
import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []

    error = False

    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            x = Bracket(next, i + 1)
            opening_brackets_stack.append(x)

        if next == ')' or next == ']' or next == '}':
            # If stack is empty this is a unmatched closing tag
            if len (opening_brackets_stack) == 0:
                error = True
                error_position = i + 1
                break
            x = opening_brackets_stack.pop()
            if not x.Match(next):
                error = True
                error_position = i + 1
                break

    # list should now be empty
    if not error:
        if len (opening_brackets_stack) != 0:
            x = opening_brackets_stack.pop()
            error = True
            error_position = x.position

    # Printing answer, write your code here
    if error:
        print error_position
    else:
        print "Success"
