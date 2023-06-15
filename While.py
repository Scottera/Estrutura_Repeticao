#Informar números até que a soma seja maior que 100

soma = 0

while soma <= 100:
    num = int(input('Informe um número: '))
    soma += num

print(f'A soma é {soma}')