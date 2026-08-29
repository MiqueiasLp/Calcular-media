def calcular_notas(qtd_notas):
    total = 0
    contador = 0
    
    while(contador < qtd_notas):
        nota = float(input(f"Digite a nota {contador + 1}: "))
        total += nota
        contador += 1
    return total / qtd_notas

def verificar_aprovacao(media, faltas):
    if media >= 7 and faltas <= 5:
        return "Aprovado"
    elif media >= 5 and faltas <= 5:
        return "Em Recuperação"
    else:
        return "Reprovado"

n = input("Digite o nome do aluno: ")
f = int(input("Digite a quantidade de faltas: "))
qtd = int(input("Digite a quantidade de notas: "))

media = calcular_notas(qtd)
status = verificar_aprovacao(media, f)

print(f"\nO aluno {n} teve a média {media:.2f} e o resultado: {status}")
