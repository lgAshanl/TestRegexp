import AutomateForThisTask
import Automate
import BadRegexp
import sys


def build_automate(s):
    stack = []
    if len(s) == 0:
        raise BadRegexp.BadRegexp("empty regexp")

    for item in s:
        # simple items
        if item == '1':
            stack.append(Automate.Automate("#"))
        elif item in ['a', 'b', 'c']:
            stack.append(Automate.Automate(item))

        # operations
        elif item == '.':
            if len(stack) < 2:
                raise BadRegexp.BadRegexp("concatenation error")
            b = stack.pop()
            a = stack.pop()
            stack.append(a.merge(b))

        elif item == '+':
            if len(stack) < 2:
                raise BadRegexp.BadRegexp("addition error")
            b = stack.pop()
            a = stack.pop()
            stack.append(a.add(b))

        elif item == '*':
            if len(stack) < 1:
                raise BadRegexp.BadRegexp("star error")
            a = stack.pop()
            stack.append(a.star())
        else:
            raise BadRegexp.BadRegexp("invalid symbol")

    if len(stack) != 1:
        raise BadRegexp.BadRegexp("few operations")

    return stack[0]


def __main__():
    s = input()
    x = input()
    k = input()
    automate = build_automate(s)
    if x not in ['a', 'b', 'c', '1']:
        sys.stdout.write("NO")
        return 0
    good_automate = AutomateForThisTask.AutomateForThisTask(automate, x)
    if x == '1':
        k = 0
    if good_automate.search(int(k)):
        sys.stdout.write("YES")
    else:
        sys.stdout.write("NO")


__main__()
