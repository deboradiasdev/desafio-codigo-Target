#Questão 1
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

#Questão 2
def fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero

numero_informado = int(input("Digite um número: "))

if fibonacci(numero_informado):
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")

'''
Questão 3

    a) 9
    b) 128
    c) 49
    d) 100
    e) 13
    f)
'''
'''
Questão 4

Para descobrir o interruptor de cada lâmpada vou ligar o primeiro interruptor e deixar por alguns minutos,
após isso desligo o primeiro e ligo o segundo e deixo aceso.
Vou até duas das salas e percebo, se a lâmpada estiver apagada e um pouco aquecida ela pertence ao interruptor 1,
se estiver acesa pertence ao interruptor 2 e se estiver apagada e fria pertence ao interruptor 3.
Depois de analisar as lâmpadas dessas duas salas encontro a resposta da terceira apenas descartando as opções.
'''
#Questão 5
def inverter_string(string):
    string_invertida = ""
    tamanho = len(string)  

    
    for i in range(tamanho - 1, -1, -1):
        string_invertida += string[i]
    
    return string_invertida  

minha_string = input("Digite uma string: ")

print("String original:", minha_string)
print("String invertida:", inverter_string(minha_string))