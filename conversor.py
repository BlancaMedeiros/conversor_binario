print('OPÇÕES')
print('1 = converter texto para binário')

OpcaoEscolhida = input("Digite a opção desejada: ")
print("Opção escolhida: ", OpcaoEscolhida)

TextoUsuario = input('degite o texto a ser convertido: ')

Textoconvertido = '' 

for letra in TextoUsuario:
    Letra_ASCII = ord(letra)
    Letra_binário = bin(Letra_ASCII)[2:]
    Textoconvertido = Textoconvertido + Letra_binário
print("Resultado da conversão: ", Textoconvertido)