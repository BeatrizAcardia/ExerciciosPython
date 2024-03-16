turno = (input("Qual seu periodo da faculdade? (Digite M para MATUTINO, V para VESPERTINO e N para NOTURNO.)"))
if(turno == "V"):
    print("Afirmativo, tenha uma BOA TARDE. ")
elif(turno  == "N"):
    print("Afirmativo, tenha uma BOA NOITE. ")
elif(turno == "M"):
    print("Afirmativo, tenha um BOM DIA.")
else:
    print("Turno Inválido!")
