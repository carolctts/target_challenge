#inverter caracteres de string 

frase = [str(x) for x in (input("Digite uma palavra ou frase para ser invertida: ").rstrip("\n"))]
frase_invertida = []
for i in range(len(frase) - 1, -1, -1):
	frase_invertida.append(frase[i])

print("".join(frase_invertida))
