import PySimpleGUI as sg
from random import randint


def cpf():
	n1 = randint(100,999)
	n2 = randint(100,999)
	n3 = randint(100,999)
	n4 = randint(10,99)

	cpf = f'{n1}.{n2}.{n3}-{n4}'
	return cpf

def menu():
	sg.change_look_and_feel('DarkPurple2')
	layout = [
	    [sg.Button('Gerar CPF')],
	    [sg.Output(size=(14,8))]

	]
	janela = sg.Window('Dados do usuario').layout(layout)
	while True:
		Button, values = janela.Read()
		if Button == None:
			break
		print(cpf())

menu()
