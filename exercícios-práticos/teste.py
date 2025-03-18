idade = int(input("Entre com a idade:"))
if idade < 12:
    print("crianca")
elif idade < 18:
    print("adolescente")
elif idade < 60:
    print("adulto")
else:
    print("idoso")