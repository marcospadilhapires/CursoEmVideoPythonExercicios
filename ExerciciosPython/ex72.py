numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito',
           'nove', 'dês','onze','doze','treze','catorze','quinze','dezesseis',
           'dezesete','dezoito','dezenove','vinte')

continuar = ' '
#usuario = int(input('Digite um numero [0 a 20]: '))

#while usuario not in range(0,21):
    #usuario = int(input('Tente novamente. Digite um numero [0 a 20]: '))

while True:
    usuario = int(input('Digite um numero [0 a 20]: '))
    if 0 <= usuario <=20:
        print(f'Você digitou o número {numeros[usuario]}')
        while continuar not in 'NS':
            continuar = str(input("Quer Continuar? [S/N]")).strip().upper()[0]
        if continuar == 'N':
            break
    else:
        print('Tente Novamente!',end = "")
    continuar = ' '

print("Fim do programa...")
