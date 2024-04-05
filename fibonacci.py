#fibonacci

def fibonacci(number):
	sequence = []
	if (number == 0 or number == 1):
		return 0
	else:
		sequence = [0, 1]
		while sequence[-1] <= number:
			next = sequence[-1] + sequence[-2]
			if next <= number:
				sequence.append(next)
			else:
				break
		return (sequence.count(number) > 0)
		

is_fibonacci = int(input("Digite um número inteiro: "))
if fibonacci(is_fibonacci):
    print("Está na sequência")
else:
    print("Não está na sequência")
