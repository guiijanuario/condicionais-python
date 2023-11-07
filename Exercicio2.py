#Faça um programa que receba 2 notas (de 0 a 10) de um usuário e calcule a média.
#Se a média for maior que 6, ele está aprovado. Se for menor que 6, está reprovado e se for 10 recebe um "parabéns"

print('---- Bem vindo ----')
print('Vamos calcular a média do aluno!')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

if n1 < 0 or n1 > 10:
    print('A primeira nota inserida está fora do intervalo válido (0 a 10)')
elif n2 < 0 or n2 > 10:
    print('A segunda nota inserida está fora do intervalo válido (0 a 10)')
else:
    media = (n1 + n2) / 2

    if media == 10:
        print("Parabéns aluno nota 10!")
    elif media >= 6:
        print("Ele foi aprovado")
    else:
        print("Infelizmente o aluno foi reprovado")
