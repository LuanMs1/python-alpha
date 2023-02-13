def division(number : float) -> None:
    try:
        result = 1 / number
        print(result)
    except TypeError:
        print("Erro: apenas um número")
    except ZeroDivisionError:
        print('Erro: divisão por zero')
    
    except:
        print('Alguma coisa deu errado. Mas eu não sei porque')


division(['dada', 'bs', 2])
