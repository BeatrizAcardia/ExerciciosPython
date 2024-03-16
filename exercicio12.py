nota1 = (float(input("Digite a primeira nota: ")))
nota2 = (float(input("Digite a segunda nota: ")))

A = 9.0 <= nota1, nota2 <= 10.0
B = 7.5 <= nota1, nota2 <= 8.9
C = 6.0 <= nota1, nota2 <= 7.4
D = 4.0 <= nota1, nota2 <= 5.9
E = 4.0 > nota1, nota2
media = (nota1+nota2)/2

print(nota1, nota2)
print(media)
if(media == A, B, C,):
    print("O aluno está em APROVADO.")
else:
    print("O  aluno está REPROVADO.")