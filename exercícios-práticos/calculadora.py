num1 = int(input("Entre com o numero 1:"))
num2 = int(input("Entre com o numero 2:"))
op = int(input("Entre com a operação: \n 1 - Soma \n 2 - Subtração \n 3 - multiplicação \n 4 - Divisão \n"))
def switch_case(op):
    if op == 1:
        return num1 + num2
    elif op == 2:
        return num1 - num2
    elif op == 3:
        return num1 * num2
    elif op == 4:
        return num1 / num2
    else:
        return "Invalid option"

resultado = switch_case(op)
print(f"Resultado: {resultado}")

# Example usage
#print(switch_case(1))  # Output: Option 1
#print(switch_case(4))  # Output: Invalid option

