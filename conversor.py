print('==' * 10)
print('CONVERSOR DE MEDIDAS')
print('==' * 10)

options = ('1', '2', '3')
print('''ESCOLHA UMA OPÇÃO:
[1] - CONVERSOR DE METROS
[2] - CONVERSOR DE QUILOS
[3] - CONVERSOR DE LITROS''')
print('==' * 10)

escolha = int(input('ESCOLHA SUA OPÇÃO: '))

if escolha == 1:
    print('==' * 10)
    print('CONVERSOR DE METROS')
    print('--' * 10)

    medida = int(input('DIGITE A DISTÂNCIA EM METROS: '))
    print('--' * 10)

    cm = medida * 100
    mm = medida * 1000

    print('A medida {}M corresponde a {:.0f}CM ou {:.0f}MM'.format(medida, cm, mm))

elif escolha == 2:
    print('==' * 10)
    print('CONVERSOR DE QUILOS')
    print('--' * 10)

    quilos = int(input('DIGITE O PESO EM QUILOS: '))
    print('--' * 10)

    g = quilos * 1000
    mg = quilos * 1000000

    print('O peso {}KG corresponde a {:.0f}G ou {:.0f}MG'.format(quilos, g, mg))

elif escolha == 3:
    print('==' * 10)
    print('CONVERSOR DE LITROS')
    print('--' * 10)

    litros = int(input('DIGITE A QUANTIDADE EM LITROS: '))
    print('--' * 10)

    dl = litros * 10
    cl = litros * 100

    print('A quantidade de {}L corresponde a {:.0f}DL ou {:.0f}CL'.format(litros, dl, cl))

else:
    print('ESCOLHA INVALIDA')