
# Solicita as duas notas do usuário
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

# Calcula a média das notas
media = (nota1 + nota2) / 2

# Verifica se o aluno foi aprovado
if media >= 5:
    print("Aprovado!")
else:
    print("Reprovado!")

# Exibe a média formatada com duas casas decimais
print(f"Média: {media:.2f}")


