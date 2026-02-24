from nutri import Nutri

def iniciar_calculadora():

    print("=" * 50)
    print(" 🍎 SISTEMA PRO DE AVALIAÇÃO NUTRICIONAL 🍎 ")
    print("=" * 50)

    paciente = Nutri()

    print("\n📋 --- PASSO 1: DADOS PESSOAIS ---")
    peso = float(input("▸ Digite seu peso (kg): "))
    altura = float(input("▸ Digite sua altura (ex: 1.70): "))
    idade = int(input("▸ Digite sua idade: "))
    genero = input("▸ Gênero (M ou F): ").strip().upper()
    dias_treino = int(input("▸ Dias de treino na semana (0 a 7): "))
    tempo_treino = int(input("▸ Duração média do seu treino (minutos): "))
    
    print("\n📏 --- PASSO 2: MEDIDAS CORPORAIS ---")
    cintura = float(input("▸ Circunferência da cintura (cm): "))
    pescoco = float(input("▸ Circunferência do pescoço (cm): "))
    quadril = float(input("▸ Circunferência do quadril (cm): "))

    print("\n" + "=" * 50)
    print(" 📊 PROCESSANDO SEU RELATÓRIO COMPLETO... 📊 ")
    print("=" * 50)

    resultado_imc = paciente.IMC(peso, altura)
    print(f"\n🩺 [SAÚDE BÁSICA]")
    print(f"   ▸ IMC: {resultado_imc['imc']:.1f} ({resultado_imc['classificação']})")
    
    agua = paciente.AGUA(peso)
    print(f"   ▸ Meta de Água: {agua:.1f} Litros/dia")

    tmb = paciente.TMB(peso, altura, idade, genero)
    get = paciente.GET(tmb, dias_treino)
    print(f"\n🔥 [METABOLISMO E ENERGIA]")
    print(f"   ▸ Taxa Metabólica Basal (Repouso): {tmb:.1f} kcal")
    print(f"   ▸ Gasto Energético Total (Diário): {get:.1f} kcal")

    gce = paciente.GCE(tempo_treino, peso)
    print(f"   ▸ Gasto calórico em {tempo_treino} min de exercício:")
    for exercicio, kcal in gce.items():
        print(f"     🏃 {exercicio}: {kcal:.1f} kcal")

    por = paciente.PORGORD(cintura, pescoco, altura, quadril, genero)
    massa = paciente.MASSCORP(peso, por)
    
    print(f"\n⚖️  [COMPOSIÇÃO CORPORAL]")
    print(f"   ▸ Gordura Corporal: {por:.1f}%")
    print(f"   ▸ Massa Magra:      {massa['massa_magra']:.1f} kg")
    print(f"   ▸ Massa Gorda:      {massa['massa_gorda']:.1f} kg")
    print("   ⚠️  Nota: A fórmula da Marinha é excelente para medir \n       seu progresso mês a mês, mas pode ter variações \n       em relação ao número absoluto.")

    dieta = paciente.DIETA(get)
    print("\n" + "-" * 50)
    print(" 🥗 SUGESTÃO DE DIETA PADRÃO (MACRONUTRIENTES) 🥗")
    print("-" * 50)
    
    print(f"\n🔸 OBJETIVO: SECAR / EMAGRECER (Déficit: {dieta['kcal_deficit']:.1f} kcal)")
    print(f"   🍚 Carboidratos: {dieta['carbo_deficit']:.1f}g")
    print(f"   🥩 Proteínas:    {dieta['pro_deficit']:.1f}g")
    print(f"   🥑 Gorduras:     {dieta['gord_deficit']:.1f}g")

    print(f"\n🔹 OBJETIVO: CRESCER / HIPERTROFIA (Superávit: {dieta['kcal_superavit']:.1f} kcal)")
    print(f"   🍚 Carboidratos: {dieta['carbo_superavit']:.1f}g")
    print(f"   🥩 Proteínas:    {dieta['pro_superavit']:.1f}g")
    print(f"   🥑 Gorduras:     {dieta['gord_superavit']:.1f}g")
    
    print("\n" + "=" * 50)
    input("\n[Pressione ENTER para encerrar o sistema]")

if __name__ == "__main__":
    iniciar_calculadora()