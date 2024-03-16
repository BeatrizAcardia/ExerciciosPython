peso = (float)(input("Joao, quantos quilos de peixe voce pegou?: "))
excesso = peso >= 50
multa = excesso * 4
if(peso <= 50):
	print("Ok, sem multas dessa vez Joao!")
elif(peso >= 50):
	print("Puts, havera uma multa de: ",multa)