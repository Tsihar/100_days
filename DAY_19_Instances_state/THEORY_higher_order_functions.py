#  ФУНКЦИИ ВЫСШЕГО ПОРЯДКА

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculator(n1, n2, fun):
    return fun(n1, n2)
# calculator - функция высшего порядка, т к обращается к другой функции
# fun в параметре без скобок, так как нам не надо чтобы она там вызвалась
# а сам вызов нужной ф-ции идет уже в return
result = calculator(2, 3, add)  #  в аргументе обращаемся к нужной функции, вызовется которая в return низшей ф-ции
print(result)
