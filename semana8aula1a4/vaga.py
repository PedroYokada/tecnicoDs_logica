python = int(input('Quantos anos de expêriencia em python você tem?: '))

machine = int(input('Quantos anos de expêriencia em  em Machine Learning você tem?: '))

diploma = input('Você tem diploma de mestrado em ciência da computação?(S = Sim/ N= Não): ').lower()

if (python >= 3 and machine >= 2) or diploma == 's':
    print('Elegivel para a vaga!!!')
else:
    print('Não elegivel para a vaga.')

