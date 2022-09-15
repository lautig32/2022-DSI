from expression import *


class Context:
    output = 0  # salida es el numero decimal
    input = ""

    def __init__(self, inp):
        self.input = inp  # esta entrada es el numero romano


def interpRomano(romano):
    context = Context(romano)
    tree = [ThousandExpression(), HundredExpression(), TenExpression(), OneExpression()]
    for i in range(4):
        tree[i].interpret(context)
    return context.output



