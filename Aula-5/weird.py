def list_operation(list_of_numbers, func):
    """
        Recebe uma lista e uma função que recebe uma lista. Aplica a função
        A lista.
    """
    result = func(list_of_numbers)
    return result

def weird_proud(list_of_numbers : list[int]) -> int:
    """
        Faz a multiplicação de uma lista l de n elementos da seguinte forma:
            p = l[0] * (l[1]**2) * (l[2] ** 3) ** ... (l[n] ** *(n + 1))

        ARGS:
            list_of_numbers: lista de numeros
        
        RETURNS:
            valor de p como definido antes
    """
    result : int = 1

    for i, number in enumerate(list_of_numbers):
        result = result * number ** (i + 1)
    
    return result