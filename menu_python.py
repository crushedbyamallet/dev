# Import das bibliotecas
import time

# Opção 1
def vistoria_imagem():
    print()
    print("\033[0;31mSinto muito, essa opção não está disponível no momento.\033[0;31m")
    loopMenu()

# Opção 2
def vistoria_nota_fiscal():
    nota_fiscal_codigo = int(input("Código da nota fiscal do produto: "))
    nota_fiscal_numero = int(input("Número de série do produto: "))
    nota_fiscal_valor = float(input("Valor declarado do produto: "))
    nota_fiscal_marca = (input("Marca do produto: "))
    nota_fiscal_emissao = (input("Data de emissão da nota fiscal: "))
    nota_fiscal_danfe = int(input("Código DANFE: "))
    print("Dados registrados.")

    # Inserção das informações no resumo
    resumo['operacao'].append([['Opção 2: ', 'Vistoria de Nota Fiscal'],
                                ['Código da NF:', nota_fiscal_codigo],
                                ['Número de série do produto:', nota_fiscal_numero],
                                ['Valor declarado do produto:', nota_fiscal_valor],
                                ['Marca do produto:', nota_fiscal_marca],
                                ['Data de emissão da nota fiscal:', nota_fiscal_emissao],
                                ['Código DANFE:', nota_fiscal_danfe]])
    loopMenu()

# Opção 3
def vistoria_modificacoes():
    modificacao = (input ("Insira as modificações do seu produto: "))
    # Inserção das informações no resumo
    resumo['operacao'].append([['Opção 3:', 'Vistoria de Modificações'],
                                ['Modificações:', modificacao]])
    print()
    loopMenu()

# Opção 4
def exibe_resumo():
    print('===== Resumo da Operação =====')
    print('Informações sobre o cadastro: ')
    for info in resumo["cadastro"]:
        print(info[0], info[1])
    
    print()
    print('Informações sobre as operações realizadas:')
    if resumo["operacao"]:
        for operacao in resumo["operacao"]:
            for info in operacao:
                print(info[0], info[1])
            print('='*35)
    else:
        print('Não foi feita nenhuma operação.')

# Função para repetir o menu
def loopMenu(): 
    while True:
        print("Selecione uma das opções a seguir:")
        print("[1] = Iniciar Vistoria de Imagem")
        print("[2] = Iniciar Vistoria de Nota Fiscal")
        print("[3] = Iniciar Vistoria de Modificações (Apenas para bicicletas modificadas)")
        print("[4] = Encerrar atendimento")
        user_input = input("Opção: ")

        if user_input == "1":
            vistoria_imagem()

        elif user_input == "2":
            vistoria_nota_fiscal()
        
        elif user_input == "3":
            vistoria_modificacoes()

        elif user_input == "4":
            print()
            print("\033[1;32m Dados registrados com sucesso. Encerrando processo...\033[m")
            time.sleep(5)
            exibe_resumo()
            exit()

        else:
            print()
            print("\033[0;31mOpção inválida, selecione outra.\033[0;31m")

# Função inicial do programa
def main():
    # Variável global para reunir todas as informações cadastradas nas operaçãos
    global resumo
    resumo = {}
    resumo['operacao'] = []

    print("> PORTO SEGURO BIKE <")
    print("> Formulário de Cadastro <")

    # Cadastro inicial
    print("Realize seu cadastro abaixo:")
    nome = (input("Nome Completo: "))
    email = (input("E-mail: "))
    endereço = (input("Endereço: "))
    CPF = int (input("CPF (Somente números): "))
    print(f"\033[1;32mCadastro realizado com sucesso: {nome}\033[m")

    # Inserção das informações no resumo
    resumo['cadastro'] = [['Nome:', nome], ['Email:', email], ['Endereço:', endereço], ['CPF:', CPF]]

    # Repetição para escolher uma opção
    while True:
        print("Gostaria de acessar o menu?")
        print("[s] = Sim")
        print("[n] = Não, gostaria de encerrar o processo.")
        user_input = input("Opção: ")

        if user_input == "s":
            print("Processando...")
            time.sleep(5)
            loopMenu()

        elif user_input == "n":
            print()
            print("Entendido. Encerrando processo...")
            time.sleep(5)
            exit()

        else:
            print()
            print('\033[0;31mOpção inválida, selecione uma opção existente.\033[0;31m')

if __name__ == '__main__':
    main()