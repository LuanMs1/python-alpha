"""typing module"""
from typing import Union

def test_kargs(nome = 'test', idade = 18, **kargs : Union[int, float, str]) -> None:
    """
        Testando kargs
    """

    print("nome: ", nome)
    print('Idade: ', idade)

    for key, value in kargs.items():
        print(key, ": ", value)

test_kargs(a = 1, b = 3 )
    