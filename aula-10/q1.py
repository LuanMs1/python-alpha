"""module to typing"""
from typing import Union

def test_args(*args : Union[str,float,int]) -> None :
    """
        Function to test the *args
    """
    for element in args:
        print(element)

test_args('az', 10, 'test', 10213, 'ble', 213.4)
