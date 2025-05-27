interesse = input("Qual é o seu interesse principal? (tecnologia/artes/ciências): ").lower()
experiencia = input("Qual é o seu nível de experiência? (iniciante/intermediario/avancado): ").lower()

if interesse == "tecnologia":
    if experiencia == "iniciante":
        curso_recomendado = "Introdução à programação"
    elif experiencia == "intermediario":
        curso_recomendado = "Desenvolvimento Web"
    else:
        curso_recomendado = "Inteligência Artificial avançada"
elif interesse == "artes":
    if experiencia == "iniciante":
        curso_recomendado = "Fundamentos do desenho"
    elif experiencia == "intermediario":
        curso_recomendado = "Técnicas de pintura"
    else:
        curso_recomendado = "História da Arte Moderna"
else:  # ciências
    if experiencia == "iniciante":
        curso_recomendado = "Ciências para todos"
    elif experiencia == "intermediario":
        curso_recomendado = "Química experimental"
    else:
        curso_recomendado = "Física teórica"

print(f"Curso recomendado: {curso_recomendado}")
