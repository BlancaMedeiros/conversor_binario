def ConverterTextoParaBinario(texto):
    Textoconvertido = '' 
    for letra in texto:
        Letra_ASCII = ord(letra)
        Letra_binário = bin(Letra_ASCII)[2:]
        Textoconvertido = Textoconvertido + Letra_binário
    return Textoconvertido

print('OPÇÕES')
print('1 = converter texto para binário')

OpcaoEscolhida = input("Digite a opção desejada: ")
print("Opção escolhida: ", OpcaoEscolhida)
if OpcaoEscolhida == '1': 
    TextoUsuario = input('degite o texto a ser convertido: ')
    print("Resultado da conversão: ", ConverterTextoParaBinario(TextoUsuario))
else:
    print('Essa opção não existe')