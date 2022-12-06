# Importuokite reikiamus modulius, kad veiktų žemiau nurodytos funkcijos
from modules.numbers.numbers import one
from modules.numbers.numbers import two
from modules.numbers.numbers import three
from modules.numbers.numbers import four
from modules.numbers.numbers import five
from modules.math.subtraction import substraction
from modules.math.multiplication import multiplication
from modules.math.division import division
from modules.math.composition import composition as addition

# Kitų failų ir žemiau esančio kodo nekeiskite
a = addition(one, four)
b = division(four, two)
c = substraction(three, two)
d = multiplication(five, two)

print(a)
print(b)
print(c)
print(d)
