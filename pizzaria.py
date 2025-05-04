import os
from time import sleep

print('-=-=-=-=-=-=-=- PIZZARIA SANTO MOLHO -=-=-=-=-=-=-=-')
print('')
#cadastro de usuario ou loin
print('CADASTRO')
print('Para dar continuidade precisamos fazer um cadastro.')
email = input('Digite seu e-mail: ')
nome = input('Digite seu primeiro nomme: ')
telefone = int(input('Digite o seu núemero de telefone: '))
cidade = input('Digite sua cidade: ')

sleep(2)
os.system('cls')
#apresentar um menu
print('Olá {}, confira o nosso menu.'.format(nome))
print('''------ MENU ------
1. Pizzas
2. Bebidas
      Nosso menu é organizado por números para melhorar o atendimento.''')

#fazer com que o usuario escolhha o menu
menu = int(input('Digite o número do menu para visualizar as opções: '))

sleep(1.5)
os.system('cls')

while menu != 1 and menu != 2:
    menu = int(input('Menu desconhecido. Digite um menu válido: '))
if menu == 1:
    sabor1 = 'MUSSARELA - (Mussarela, Orégano, Azeitona)'
    sabor2 = 'CALABRESA - (Mussarela, Calabresa, Cebola, Tomate)'
    sabor3 = 'FRANGO - (Mussarela, Frango)'
    sabor4 = '4. FRANGO COM CATUPIRY - (Mussarela, Frango, Catupiry, Tomate)'
    sabor5 = 'PORTUGUESA - (Mussarela, Presunto, Ervilha, Palmito, Calabresa, Cebola, Ovo, Bacon, Tomate)'
    print('''MENU PIZZAS
1. MUSSARELA - (Mussarela, Orégano, Azeitona)
2. CALABRESA - (Mussarela, Calabresa, Cebola, Tomate)
3. FRANGO - (Mussarela, Frango)
4. FRANGO COM CATUPIRY - (Mussarela, Frango, Catupiry, Tomate)
5. PORTUGUESA - (Mussarela, Presunto, Ervilha, Palmito, Calabresa, Cebola, Ovo, Bacon, Tomate)
6. DOIS SABORES''')
    escolha = int(input('Digite a sua escolha do menu: '))
    while escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4 and escolha != 5 and escolha != 6:
        print('''MENU PIZZAS
1. MUSSARELA - (Mussarela, Orégano, Azeitona)
2. CALABRESA - (Mussarela, Calabresa, Cebola, Tomate)
3. FRANGO - (Mussarela, Frango)
4. FRANGO COM CATUPIRY - (Mussarela, Frango, Catupiry, Tomate)
5. PORTUGUESA - (Mussarela, Presunto, Ervilha, Palmito, Calabresa, Cebola, Ovo, Bacon, Tomate)
6. DOIS SABORES''')
        escolha = int(input('Escolha Inválida. Por favor, digite uma escolha que esteja dentro do nosso menu: '))

    sleep(1)

    if escolha == 1:
        print(f'Você escolheu o sabor: {sabor1}')
    elif escolha == 2:
        print(f'Você escolheu o sabor: {sabor2}')
    elif escolha == 3:
        print(f'Você escolheu o sabor: {sabor3}')
    elif escolha == 4:
        print(f'Você escolheu o sabor: {sabor4}')
    elif escolha == 5:
        print(f'Você escolheu o sabor: {sabor5}')
    else:
        primeiro_sabor = int(input('Escolha o primerio sabor: '))
        segundo_sabor = int(input('Escolha o segundo sabor: '))
        sabor1 = 'MUSSARELA'
        sabor2 = 'CALABRESA'
        sabor3 = 'FRANGO'
        sabor4 = 'FRANGO COM CATUPIRY'
        sabor5 =  'PORTUGUESA'

        sleep(1)

        if primeiro_sabor == 1:
            if segundo_sabor == 2:
                print(f'Você escolheu os sabores {sabor1} e {sabor2}')
            elif segundo_sabor == 3:
                print(f'Você escolheu os sabores {sabor1} e {sabor3}')
            elif segundo_sabor == 4:
                print(f'Você escolheu os sabores {sabor1} e {sabor4}')
            else:  
                print(f'Você escolheu os sabores {sabor1} e {sabor5}')
        elif primeiro_sabor == 2:
            if segundo_sabor == 1:
                print(f'Você escolheu os sabores {sabor2} e {sabor1}')
            elif segundo_sabor == 3:
                print(f'Você escolheu os sabores {sabor2} e {sabor3}')
            elif segundo_sabor == 4:
                print(f'Você escolheu os sabores {sabor2} e {sabor4}')
            else:
                print(f'Você escolheu os sabores {sabor2} e {sabor5}')
        elif primeiro_sabor == 3:
            if segundo_sabor == 1:
                print(f'Você escolheu os sabores {sabor3} e {sabor1}')
            elif segundo_sabor == 2:
                print(f'Você escolheu os sabores {sabor3} e {sabor2}')
            elif segundo_sabor == 4:
                print(f'Você escolheu os sabores {sabor3} e {sabor4}')
            else:
                print(f'Você esolheu os sabores {sabor3} e {sabor5}')
        elif primeiro_sabor == 4:
            if segundo_sabor == 1:
                print(f'Você escolheu os sabores {sabor4} e {sabor1}')
            elif segundo_sabor == 2:
                print(f'Você escolheu os sabores {sabor4} e {sabor2}')
            elif segundo_sabor == 3:
                print(f'Você escolheu os sabores {sabor4} e {sabor3}')
            else:
                print(f'Você escolheu os sabores {sabor4} e {sabor5}')
        else:
            if segundo_sabor == 1:
                print(f'Você escolheu os sabores {sabor5} e {sabor1}')
            elif segundo_sabor == 2:
                print(f'Você escolheu os sabores {sabor5} e {sabor2}')
            elif segundo_sabor == 3:
                print(f'Você escolheu os sabores {sabor5} e {sabor3}')
            else:
                print(f'Você escolheu os sabores {sabor5} e {sabor4}')
# Usuario escolhe o tamanho e vaores
    valor1 = 50
    valor2 = 60
    valor3 = 70
    valor4 = 80
    tam1 = 'P'
    tam2 = 'M'
    tam3 = 'G'
    tam4 = 'GG'
    print(f'''-=-=-=- TAMANHOS E VALORES -=-=-=-
    {tam1} -------------------- R${valor1},00
    {tam2} -------------------- R${valor2},00
    {tam3} -------------------- R${valor3},00
    {tam4} -------------------- R${valor4},00''')

    tamanho = input('Digite o tamanho da pizza: ').strip().upper()
    if tamanho == tam1:
        print(f'Você escolheu o tamanho {tam1}.')
    elif tamanho == tam2:
        print(f'Você esscolheu o tamanho {tam2}.')
    elif tamanho == tam3:
        print(f'Você escolheu o tamamnho {tam3}.')
    else:
        print(f'Você escolheu o tamanho {tam4}.')
    continuar = input('Você deseja algo para beber?\nDigite SIM para prosseguir e NÃO para finalizar o pedido.\n').strip().upper()
    if continuar == 'SIM':
        coca1 = 'Coca-Cola 2L'
        fanta1 = 'Fanta 2L'
        kuat1 = 'Kuat 2L'
        coca2 = 'Coca-Cola Lata'
        fanta2 = 'Fanta Lata'
        kuat2 = 'Kuat Lata'
        hinecken = 'Hinecken 600ml'
        skol = 'Skol 600ml'
        brhama = 'Brahma 600ml'
        coca1_valor = 15
        fanta1_valor = 10
        kuat1_valor = 10
        coca2_valor = 8
        fanta2_valor = 5
        kuat2_valor = 5
        hinecken_valor = 17
        skol_valor = 12
        brhama_valor = 12
        print(f'''MENU BEBIDAS
    1. {coca1}
    2. {fanta1}
    3. {kuat1}
    4. {coca2}
    5. {fanta2}
    6. {kuat2}
    7. {hinecken}
    8. {skol}
    9. {brhama}
    ''')
        escolha_bebida = int(input('Digite a sua escolha do menu: '))
        while escolha_bebida != 1 and escolha_bebida != 2 and escolha_bebida != 3 and escolha_bebida != 4 and escolha_bebida != 5 and escolha_bebida != 6 and escolha_bebida != 7 and escolha_bebida != 8 and escolha_bebida != 9:
            print(f'''MENU BEBIDAS
    1. {coca1}
    2. {fanta1}
    3. {kuat1}
    4. {coca2}
    5. {fanta2}
    6. {kuat2}
    7. {hinecken}
    8. {skol}
    9. {brhama}
    ''')
            escolha_bebida = int(input('Escolha Inválida. Por favor, digite uma escolha que esteja dentro do nosso menu: '))
            if escolha_bebida == 1:
                print(f'Você escolheu a bebida: {coca1}')
            elif escolha_bebida == 2:
                print(f'Você escolheu a bebida: {fanta1}')
            elif escolha_bebida == 3:
                print(f'Você escolheu a bebida: {kuat1}')
            elif escolha_bebida == 4:
                print(f'Você escolheu a bebida: {coca2}')
            elif escolha_bebida == 5:
                print(f'Você escolheu a bebida: {fanta2}')
            elif escolha_bebida == 6:
                print(f'Você escolheu a bebida: {kuat2}')
            elif escolha_bebida == 7:
                print(f'Você escolheu a bebida: {hinecken}')
            elif escolha_bebida == 8:
                print(f'Você escolheu a bebida: {skol}')
            else:
                print(f'Você escolheu a bebida: {brhama}')
        print(f'O seu pedido foi:\nPizza: N° {escolha}     TAM: {tamanho}\nBebida: {escolha_bebida}')
    else:
        print(f'O seu pedido foi:\nPizza: N° {escolha}     TAM: {tamanho}')
else:
    coca1 = 'Coca-Cola 2L'
    fanta1 = 'Fanta 2L'
    kuat1 = 'Kuat 2L'
    coca2 = 'Coca-Cola Lata'
    fanta2 = 'Fanta Lata'
    kuat2 = 'Kuat Lata'
    hinecken = 'Hinecken 600ml'
    skol = 'Skol 600ml'
    brhama = 'Brahma 600ml'
    coca1_valor = 15
    fanta1_valor = 10
    kuat1_valor = 10
    coca2_valor = 8
    fanta2_valor = 5
    kuat2_valor = 5
    hinecken_valor = 17
    skol_valor = 12
    brhama_valor = 12
    print(f'''MENU BEBIDAS
1. {coca1}
2. {fanta1}
3. {kuat1}
4. {coca2}
5. {fanta2}
6. {kuat2}
7. {hinecken}
8. {skol}
9. {brhama}
''')
    escolha_bebida = int(input('Digite a sua escolha do menu: '))
    while escolha_bebida != 1 and escolha_bebida != 2 and escolha_bebida != 3 and escolha_bebida != 4 and escolha_bebida != 5 and escolha_bebida != 6 and escolha_bebida != 7 and escolha_bebida != 8 and escolha_bebida != 9:
            print(f'''MENU BEBIDAS
    1. {coca1}
    2. {fanta1}
    3. {kuat1}
    4. {coca2}
    5. {fanta2}
    6. {kuat2}
    7. {hinecken}
    8. {skol}
    9. {brhama}
    ''')
            escolha_bebida = int(input('Escolha Inválida. Por favor, digite uma escolha que esteja dentro do nosso menu: '))
    if escolha_bebida == 1:
        print(f'Você escolheu a bebida: {coca1}')
    elif escolha_bebida == 2:
        print(f'Você escolheu a bebida: {fanta1}')
    elif escolha_bebida == 3:
        print(f'Você escolheu a bebida: {kuat1}')
    elif escolha_bebida == 4:
        print(f'Você escolheu a bebida: {coca2}')
    elif escolha_bebida == 5:
        print(f'Você escolheu a bebida: {fanta2}')
    elif escolha_bebida == 6:
        print(f'Você escolheu a bebida: {kuat2}')
    elif escolha_bebida == 7:
        print(f'Você escolheu a bebida: {hinecken}')
    elif escolha_bebida == 8:
        print(f'Você escolheu a bebida: {skol}')
    else:
        print(f'Você escolheu a bebida: {brhama}')
    escolha = input('Você deseja algo para comer?\nDigite SIM para prosseguir e NÃO para finalizar o pedido.\n').strip().upper()
    if escolha == 'SIM':
        sabor1 = 'MUSSARELA - (Mussarela, Orégano, Azeitona)'
        sabor2 = 'CALABRESA - (Mussarela, Calabresa, Cebola, Tomate)'
        sabor3 = 'FRANGO - (Mussarela, Frango)'
        sabor4 = '4. FRANGO COM CATUPIRY - (Mussarela, Frango, Catupiry, Tomate)'
        sabor5 = 'PORTUGUESA - (Mussarela, Presunto, Ervilha, Palmito, Calabresa, Cebola, Ovo, Bacon, Tomate)'
        print('''MENU PIZZAS
    1. MUSSARELA - (Mussarela, Orégano, Azeitona)
    2. CALABRESA - (Mussarela, Calabresa, Cebola, Tomate)
    3. FRANGO - (Mussarela, Frango)
    4. FRANGO COM CATUPIRY - (Mussarela, Frango, Catupiry, Tomate)
    5. PORTUGUESA - (Mussarela, Presunto, Ervilha, Palmito, Calabresa, Cebola, Ovo, Bacon, Tomate)
    6. DOIS SABORES''')
        escolha = int(input('Digite a sua escolha do menu: '))
        while escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4 and escolha != 5 and escolha != 6:
            print('''MENU PIZZAS
    1. MUSSARELA - (Mussarela, Orégano, Azeitona)
    2. CALABRESA - (Mussarela, Calabresa, Cebola, Tomate)
    3. FRANGO - (Mussarela, Frango)
    4. FRANGO COM CATUPIRY - (Mussarela, Frango, Catupiry, Tomate)
    5. PORTUGUESA - (Mussarela, Presunto, Ervilha, Palmito, Calabresa, Cebola, Ovo, Bacon, Tomate)
    6. DOIS SABORES''')
            escolha = int(input('Escolha Inválida. Por favor, digite uma escolha que esteja dentro do nosso menu: '))
        if escolha == 1:
            print(f'Você escolheu o sabor: {sabor1}')
        elif escolha == 2:
            print(f'Você escolheu o sabor: {sabor2}')
        elif escolha == 3:
            print(f'Você escolheu o sabor: {sabor3}')
        elif escolha == 4:
            print(f'Você escolheu o sabor: {sabor4}')
        elif escolha == 5:
            print(f'Você escolheu o sabor: {sabor5}')
        else:
            primeiro_sabor = int(input('Escolha o primerio sabor: '))
            segundo_sabor = int(input('Escolha o segundo sabor: '))
            sabor1 = 'MUSSARELA'
            sabor2 = 'CALABRESA'
            sabor3 = 'FRANGO'
            sabor4 = 'FRANGO COM CATUPIRY'
            sabor5 =  'PORTUGUESA'
            if primeiro_sabor == 1:
                if segundo_sabor == 2:
                    print(f'Você escolheu os sabores {sabor1} e {sabor2}')
                elif segundo_sabor == 3:
                    print(f'Você escolheu os sabores {sabor1} e {sabor3}')
                elif segundo_sabor == 4:
                    print(f'Você escolheu os sabores {sabor1} e {sabor4}')
                else:  
                    print(f'Você escolheu os sabores {sabor1} e {sabor5}')
            elif primeiro_sabor == 2:
                if segundo_sabor == 1:
                    print(f'Você escolheu os sabores {sabor2} e {sabor1}')
                elif segundo_sabor == 3:
                    print(f'Você escolheu os sabores {sabor2} e {sabor3}')
                elif segundo_sabor == 4:
                    print(f'Você escolheu os sabores {sabor2} e {sabor4}')
                else:
                    print(f'Você escolheu os sabores {sabor2} e {sabor5}')
            elif primeiro_sabor == 3:
                if segundo_sabor == 1:
                    print(f'Você escolheu os sabores {sabor3} e {sabor1}')
                elif segundo_sabor == 2:
                    print(f'Você escolheu os sabores {sabor3} e {sabor2}')
                elif segundo_sabor == 4:
                    print(f'Você escolheu os sabores {sabor3} e {sabor4}')
                else:
                    print(f'Você esolheu os sabores {sabor3} e {sabor5}')
            elif primeiro_sabor == 4:
                if segundo_sabor == 1:
                    print(f'Você escolheu os sabores {sabor4} e {sabor1}')
                elif segundo_sabor == 2:
                    print(f'Você escolheu os sabores {sabor4} e {sabor2}')
                elif segundo_sabor == 3:
                    print(f'Você escolheu os sabores {sabor4} e {sabor3}')
                else:
                    print(f'Você escolheu os sabores {sabor4} e {sabor5}')
            else:
                if segundo_sabor == 1:
                    print(f'Você escolheu os sabores {sabor5} e {sabor1}')
                elif segundo_sabor == 2:
                    print(f'Você escolheu os sabores {sabor5} e {sabor2}')
                elif segundo_sabor == 3:
                    print(f'Você escolheu os sabores {sabor5} e {sabor3}')
                else:
                    print(f'Você escolheu os sabores {sabor5} e {sabor4}')
    # Usuario escolhe o tamanho e vaores
        valor1 = 50
        valor2 = 60
        valor3 = 70
        valor4 = 80
        tam1 = 'P'
        tam2 = 'M'
        tam3 = 'G'
        tam4 = 'GG'
        print(f'''-=-=-=- TAMANHOS E VALORES -=-=-=-
        {tam1} -------------------- R${valor1},00
        {tam2} -------------------- R${valor2},00
        {tam3} -------------------- R${valor3},00
        {tam4} -------------------- R${valor4},00''')
        tamanho = input('Digite o tamanho da pizza: ').strip().upper()
        if tamanho == tam1:
            print(f'Você escolheu o tamanho {tam1}.')
        elif tamanho == tam2:
            print(f'Você esscolheu o tamanho {tam2}.')
        elif tamanho == tam3:
            print(f'Você escolheu o tamamnho {tam3}.')
        else:
            print(f'Você escolheu o tamanho {tam4}.')
        print(f'O seu pedido foi:\nBebida N° {escolha_bebida}\nPizza: N° {escolha}     TAM: {tamanho}')
    else:
        print(f'O seu pedido foi:\nBebida N° {escolha_bebida}')

#peruntar se vai retirar nno local ou entrega
retirada = input('Entrega ou Retirada no local?\n Digite sua esolha: ').strip().upper()
#para a entrega, informar o endereço
if retirada == 'ENTREGA':
    rua = input('Digite o nome de sua Rua: ')
    bairro = input('Digite o nome de seu bairro: ')
    numero = input('Digite o número da casa: ')
    print(f'O pedido será entregue no seguinte endereço: {rua}, {bairro}, {numero}')
else:
    print('O seu pedido ficou para a retirada aqui na pizzaria.')
