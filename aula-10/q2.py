"""typing module"""
from typing import Union

def mult(*args: Union[int, float]) -> Union[int, float]:
    """
        Recebe valores e retorna a multiplicação entre eles

        ARGS:
            args: Tupla de valores       
        Return:
            result: valor da multiplicação
    """
    result = 1
    for number in args:
        result *= number
    return result

print(mult(2,4,0.5))
