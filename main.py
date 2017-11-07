import AutomateForThisTask
import Automate
import BadRegexp
import sys


def BuildAutomate(str):
    stack = []
    if len(str) == 0:
        raise BadRegexp.BadRegexp("empty regexp")

    for item in str:
        # simple items
        if item == '1':
            stack.append(Automate.Automate("#"))
        if item in ['a', 'b', 'c']:
            stack.append(Automate.Automate(item))

        # operations
        if item == '.':
            if len(stack) < 2:
                raise BadRegexp.BadRegexp("concatenation error")
            b = stack.pop()
            a = stack.pop()
            stack.append(a.merge(b))

        if item == '+':
            if len(stack) < 2:
                raise BadRegexp.BadRegexp("addition error")
            b = stack.pop()
            a = stack.pop()
            stack.append(a.add(b))

        if item == '*':
            if len(stack) < 1:
                raise BadRegexp.BadRegexp("star error")
            a = stack.pop()
            stack.append(a.star())

    if len(stack) != 1:
        raise BadRegexp.BadRegexp("few operations")

    return stack[0]


def __main__():
    str = input()
    x = input()
    k = input()
    automate = BuildAutomate(str)
    if x not in ['a', 'b', 'c', '1']:
        sys.stdout.write("NO")
        return 0
    good_automate = AutomateForThisTask.AutomateForThisTask(automate, x)
    if good_automate.search(x, int(k)):
        sys.stdout.write("YES")
    else:
        sys.stdout.write("NO")

__main__()