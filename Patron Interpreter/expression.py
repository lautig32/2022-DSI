class Expression:  # Expresion Abstracta
    one = " "
    four = " "
    five = " "
    nine = " "
    multiplier = 1

    def interpret(self, context):

        if len(context.input) == 0:
            return ""

        if context.input.startswith(self.nine):
            context.output += (9 * self.multiplier)
            context.input = context.input[2:]

        elif context.input.startswith(self.four):
            context.output += (4 * self.multiplier)
            context.input = context.input[2:]

        elif context.input.startswith(self.five):
            context.output += (5 * self.multiplier)
            context.input = context.input[1:]

        while context.input.startswith(self.one):
            context.output += self.multiplier
            context.input = context.input[1:]


class OneExpression(Expression):
    one = "I"
    four = "IV"
    five = "V"
    nine = "IX"
    multiplier = 1


class TenExpression(Expression):
    one = "X"
    four = "XL"
    five = "L"
    nine = "XC"
    multiplier = 10


class HundredExpression(Expression):
    one = "C"
    four = "CD"
    five = "D"
    nine = "CM"
    multiplier = 100


class ThousandExpression(Expression):
    one = "M"
    multiplier = 1000
