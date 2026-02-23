# 1. Importa a sua "fábrica" de cálculos do outro arquivo
from nutri import Nutri

def iniciar_calculadora():
    print("=" * 45)
    print("   🍎 SISTEMA DE AVALIAÇÃO NUTRICIONAL 🍎   ")
    print("=" * 45)

    paciente = Nutri()

    print("\n--- PASSO 1: DADOS PESSOAIS ---")
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (ex: 1.70): "))
    idade = int(input("Digite sua idade: "))
    genero = input("Gênero (M ou F): ").strip().upper()
    dias_treino = int(input("Dias de treino na semana (0 a 7): "))

    print("\n" + "=" * 45)
    print(" 📊 RELÁTORIO ABAIXO 📊 ")
    print("=" * 45)

    resultado_imc = paciente.IMC(peso, altura)
    print(f"\n[+] IMC: {resultado_imc['imc']:.1f} -> {resultado_imc['classificação']}")

    tmb = paciente.TMB(peso, altura, idade, genero)
    get = paciente.GET(tmb, dias_treino)
    print(f"[+] Taxa Metabólica Basal (Gasto natural do corpo): {tmb:.1f} kcal")
    print(f"[+] Gasto Energético Total (Gasto Total diário): {get:.1f} kcal")

    agua = paciente.AGUA(peso)
    print(f"[+] Meta diária de Água: {agua:.1f} Litros")

    dieta = paciente.DIETA(get)
    print("\n--- 🥗 SUGESTÃO DE DIETA PADRÃO ---")
    
    print(f"🔸 PARA EMAGRECER (Déficit: {dieta['kcal_deficit']:.1f} kcal):")
    print(f"    Carboidratos: {dieta['carbo_deficit']:.1f}g")
    print(f"    Proteínas:    {dieta['pro_deficit']:.1f}g")
    print(f"    Gorduras:     {dieta['gord_deficit']:.1f}g")

    print(f"\n🔹 PARA CRESCER (Superávit: {dieta['kcal_superavit']:.1f} kcal):")
    print(f"    Carboidratos: {dieta['carbo_superavit']:.1f}g")
    print(f"    Proteínas:    {dieta['pro_superavit']:.1f}g")
    print(f"    Gorduras:     {dieta['gord_superavit']:.1f}g")
    
    print("\n" + "=" * 45)

if __name__ == "__main__":
    iniciar_calculadora()