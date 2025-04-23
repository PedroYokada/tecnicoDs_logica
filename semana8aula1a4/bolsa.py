gpa = float(input('Qual o seu GPA?: '))

top = input('Você esta no top 10 da turma? (S = Sim/ N= Não): ').lower()

trabalho = int(input('Quantas horas de trabalho voluntario você realizou?: '))

if gpa >= 3.5  or top == 's' or trabalho >= 100:
    print('Elegível para uma bolsa de estudos.')
else:
    print('Não elegível para uma bolsa de estudos.')