import random as rand 
 
numero = rand.randint(1,10)
print(numero) 

tentativas = 0
escolha = 0
flag = 1
 
while (escolha != numero) and flag==1:
    escolha = int(input("[> Informe um número de 1 a 10: "))
    tentativas += 1
    if escolha < 1 or escolha > 10:
        print('Número inválido!')
    elif escolha > numero: 
        print('- Você digitou um número maior.')
        print('- A resposta era: ' + str(numero))
        flag = 0
    elif escolha < numero: 
        print('- Você digitou um número menor.')
        print('- A resposta era: ' + str(numero))
        flag = 0
    else: 
        print('[> Bingo! O numero era ' + str(escolha) + "!")
        flag = 0

if tentativas > 1:
    txt = " tentativas"
else: 
    txt = " tentativa"
    
print("** Você usou "+ str(tentativas) + txt + " **")



