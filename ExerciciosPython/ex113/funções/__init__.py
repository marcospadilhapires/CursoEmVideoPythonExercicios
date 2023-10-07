def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))
        except KeyboardInterrupt:
            print("\n\33[0:31mO usuário preferiu não digitar uma valor inteiro, interrompendo a execução\33[m")
            return 0
        except (ValueError,TypeError):
            print("\33[0:31mERRO! Digite um numero inteiro válido.\33[m")
            continue
        else:
            return numero


def leiaFloat(msg):
    while True:
        try:
            numero = float(input(msg))
        except KeyboardInterrupt:
            print("\n\33[0:31mO usuário preferiu não digitar uma valor real, interrompendo a execução\33[m")
            return 0
        except (ValueError, TypeError):
            print("\33[0:31mERRO! Digite um numero real válido.\33[m")
            continue
        else:
            return numero

