# if else elif 

email = 'samutigrao@gmail.com'
email_digitado = input('Digite seu email: ')
email_digitado = email_digitado.lower()
senha = 'Samu123'
senha_digitada = input('Digite sua senha: ')

'''OPERADORES DE COMPARAÇÃO
== -> IGUAL
< -> MENOR
> -> MAIOR
<= -> MENOR OU IGUAL
>= MAIOR OU IGUAL
!= -> DIFERENTE
'''

'''OPERADORES BOOLEANOS
E = && = AND
OU = || = OR
NAO = ! = NOT 
'''

if email_digitado == email and senha_digitada == senha:
    print('Logado com sucesso!')
elif senha_digitada != senha:
    print('Senha invalida')
else:
    print('Credenciais invalidas')