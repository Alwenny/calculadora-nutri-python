from nutri import Nutri

paciente = Nutri()

print("-"*32)
print("BEM VINDO AO SISTEMA NUTRICIONAL")
print("-"*52)
print("Vou pedir alguns dados necessários para os calculos")
print("-"*52)

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
idade = int(input("Digite a sua idade: "))
genero = input("Seu Genero (F/M): ")
dias = int(input("Quantas vezes por semana você se exercita? "))
tempo = int(input("Geralmente por quantos minitos? "))
cintura = float(input("Qual a circunferencia da Cintura? "))
pescoco = float(input("Qual a do Pescoço? "))
quadril = float(input("E o tamanho do Quadril? "))