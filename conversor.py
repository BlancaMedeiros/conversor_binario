def ConverterTextoParaBinario(texto):
    Textoconvertido = '' 
    for letra in texto:
        Letra_ASCII = ord(letra)
        Letra_binário = bin(Letra_ASCII)[2:]
        Textoconvertido = Textoconvertido + Letra_binário
    return Textoconvertido

def ConverterBinarioParaTexto(TextoBinario):
    Textoconvertido = '' 
    quantidadeLetra = len(TextoBinario)
    for i in range(0, int(quantidadeLetra), 7):
        letraBinario = TextoBinario[i:i+7]
        codigo_ascii = int(letraBinario, 2)
        letra = chr(codigo_ascii)
        Textoconvertido = Textoconvertido + letra
    return Textoconvertido


print('OPÇÕES')
print('1 = converter texto para binário')
print('2 = converter binário para texto')

OpcaoEscolhida = input("Digite a opção desejada: ")
print("Opção escolhida: ", OpcaoEscolhida)
if OpcaoEscolhida == '1': 
    TextoUsuario = input('degite o texto a ser convertido: ')
    print("Resultado da conversão: ", ConverterTextoParaBinario(TextoUsuario))
elif OpcaoEscolhida == '2':
    TextoUsuario = input('degite o texto a ser convertido: ')
    print("Resultado da conversão: ", ConverterBinarioParaTexto(TextoUsuario))
else:
    print('Essa opção não existe')