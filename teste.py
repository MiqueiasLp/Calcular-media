def calcular_notas(qtd_notas):
    total = 0
    contador = 0
    
    while(contador < qtd_notas):
        nota = float(input(f"Digite a nota {contador + 1}: "))
        total += nota
        contador += 1
    return total / qtd_notas

def verificar_aprovacao(media, faltas, nome):
    if media >= 7 and faltas <= 5:
        print(f"{nome} foi aprovado com média {media} e {faltas} faltas.")
        return "Aprovado"
    elif media >= 5 and faltas <= 5:
        print(f"{nome} está em recuperação com média {media} e {faltas} faltas.") 
        return "Em Recuperação"
    else:
        print(f"{nome} está reprovado com média {media} e {faltas} faltas.")
        return "Reprovado"

n = input("Digite o nome do aluno: ")
f = int(input("Digite a quantidade de faltas: "))
qtd = int(input("Digite a quantidade de notas: "))
media = calcular_notas(qtd)
verificar_aprovacao(media, f, n)
