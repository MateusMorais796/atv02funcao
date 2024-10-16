# Crie uma função chamada verificar_paridade que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.
def verificar_paridade(n):
    if n %2==0:
        return "par"
    else:
        return "ímpar"
    
numero = int(input("Digite um número inteiro "))
resultado = verificar_paridade(numero)
print(f'{numero} é {resultado}')