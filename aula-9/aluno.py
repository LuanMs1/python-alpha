# pegar informações

situation : dict = {}
while True:
    name : str = input('Digite o nome do aluno: ')
    grade : str = input("digite a nota do aluno: ")
    if int(grade) >= 7:
        situation[name] = 'aprovado'
    else:
        situation[name] = 'reprovado'    
    cont : str = input('digite 0 para parar o input')
    if int(cont) == 0:
        break

print(situation)