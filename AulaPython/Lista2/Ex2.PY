frase = input("Digite uma frase: ")
print(frase)

palavras = frase.split()
numeroPalavras = len(palavras)
print(numeroPalavras)

palavrasInvertidas = palavras[::-1]
fraseInvertida = ' '.join(palavrasInvertidas)
print(fraseInvertida)

