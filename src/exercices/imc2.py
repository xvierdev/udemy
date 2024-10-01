# Calculo do imc
# formula = peso / altura ** 2

peso = float(input('Digite o peso em quilos: '))
altura = float(input('Digite a altura em metros: '))
imc = peso / altura ** altura

print(f'O imc é de {imc:.2f}')