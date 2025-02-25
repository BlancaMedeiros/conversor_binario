print('OPÇÕES')
print('1 = converter texto para binário')

OpcaoEscolhida = input("Digite a opção desejada: ")
print("Opção escolhida: ", OpcaoEscolhida)

TextoUsuario = input('degite o texto a ser convertido: ')
print(TextoUsuario)

Textoconvertido = '' 

for letra in TextoUsuario:
    Textoconvertido = Textoconvertido + letra
    print(letra, Textoconvertido)
