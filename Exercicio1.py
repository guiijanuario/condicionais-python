# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print('---- Bem vindo ----')
print('1 - Manhã')
print('2 - Tarde')
print('3 - Noite')
turno = int(input('Digite qual turno você geralmente estuda?'))

if turno == 1:
    print("Você estuda de Manhã, você é do time que acorda animado!")
elif turno == 2:
    print("Você gosta de estudar tomando um cafézinho da tarde, que bacana!")
elif turno == 3:
    print("Provavelmente, você trabalha muito e só tem de noite para estudar!")
else:
    print("Valor Inválido!")

