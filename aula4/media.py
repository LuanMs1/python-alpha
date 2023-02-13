def get_user_words() -> list[str]:
    """
        Função impura pois não tem nenhum imput, mas pode retornar diferentes 
        valores. Retorna uma lista das palavras digitadas pelo usuários

        RETURNS:
            Lista com palavras digitadas pelo usuário
    """
    wrds : list = []
    while True:
        word = input("Digite uma palavra, digite zero quando acabar: ")
        if word == '0':
            break
        wrds.append(word)
    return wrds

def count_x_occurrences(word : str) -> int:
    """
        Função pura sempre retornará o mesmo valor para o mesmo input.
        Retorna a quantidade de vezes que o x aparece na palavra

        ARGS:
            word: palavra
        RETURNS:
            Numero de aparições da letra x
    """
    x : int = 0
    for char in word:
        if char == 'x':
            x += 1
    return x

def inform_average(average: float) -> None:
    """
        Função pura sempre retornará o mesmo valor para o mesmo imput. Retorna
        nada, printa a média de X.

        ARGS:
            average: valor para se printar
    """
    print("A média é : ", average)
    return

def main() -> None:
    list_of_words : list[str] = get_user_words()
    count : int = count_x_occurrences(list_of_words[0])
    avg = 0.
    for word in list_of_words:
        avg += count_x_occurrences(word)
    
    avg = avg / len(list_of_words)
    inform_average(avg)



if __name__ == "__main__":
    main()