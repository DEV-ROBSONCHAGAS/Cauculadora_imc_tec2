def obter_sugestoes(imc):
    if imc < 18.5:
        return "Baixo peso", "Foco em musculação para ganho de massa e dieta hipercalórica."
    elif 18.5 <= imc < 25:
        return "Peso Ideal", "Manutenção: Caminhadas, natação ou ciclismo 3.5x por semana."
    elif 25 <= imc < 30:
        return "Sobrepeso", "Cardio moderado (corrida leve) e treinos de resistência."
    else:
        return "Obesidade", "Atividades de baixo impacto: Hidroginástica ou caminhadas leves."
