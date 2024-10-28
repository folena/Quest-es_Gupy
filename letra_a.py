def conta_letra_a(frase):
  return frase.lower().count('a')

frase = input("Digite uma frase: ")

print(f"A frase possui {conta_letra_a(frase)} letras 'a'.")