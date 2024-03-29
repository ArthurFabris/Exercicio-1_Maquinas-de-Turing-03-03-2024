# Exercicio 1: Maquinas de turing.
# Autores: Arthur Fabris, Ketholly, Mateus Silva, Vitor, Matheus Gomes
# Ultima atualização: 04/03/2024 gmt-0300

import os

tabela_ascii_byte = {
    'a': '01100001',
    'b': '01100010',
    'c': '01100011',
    'd': '01100100',
    'e': '01100101',
    'f': '01100110',
    'g': '01100111',
    'h': '01101000',
    'i': '01101001',
    'j': '01101010',
    'k': '01101011',
    'l': '01101100',
    'm': '01101101',
    'n': '01101110',
    'o': '01101111',
    'p': '01110000',
    'q': '01110001',
    'r': '01110010',
    's': '01110011',
    't': '01110100',
    'u': '01110101',
    'v': '01110110',
    'w': '01110111',
    'x': '01111000',
    'y': '01111001',
    'z': '01111010',
    'A': '01000001',
    'B': '01000010',
    'C': '01000011',
    'D': '01000100',
    'E': '01000101',
    'F': '01000110',
    'G': '01000111',
    'H': '01001000',
    'I': '01001001',
    'J': '01001010',
    'K': '01001011',
    'L': '01001100',
    'M': '01001101',
    'N': '01001110',
    'O': '01001111',
    'P': '01010000',
    'Q': '01010001',
    'R': '01010010',
    'S': '01010011',
    'T': '01010100',
    'U': '01010101',
    'V': '01010110',
    'W': '01010111',
    'X': '01011000',
    'Y': '01011001',
    'Z': '01011010',
    '$': '00100100',
    '%': '00100101'
}

# Para facilitar ainda, será usado o caractere $ no lugar do espaço convencional para indicar fim de
# uma palavra/expressão e início de outra palavra e expressão. Neste caso, para fins didáticos, o
# primeiro caractere da mensagem será $ e para indicar fim da mensagem usaremos %.
dicionario_conhecido_sem_sinais = {
    'anmeineVerwandten': 'para os meus parentes',
    'ankommen': 'chegar',
    'bleibe': 'permaneça',
    'DavidgingzuAhimelechsHaus': 'Davi foi à casa de Aimeleque',
    'DavidalserinderHohlewar': 'Davi, quando ele estava na caverna',
    'deinname': 'seu nome',
    'deinRuhm': 'a sua fama',
    'duwirstfreisein': 'você estará livre',
    'furimme': 'para sempre',
    'gefangene': 'prisioneiros',
    'hierbinich': 'aqui estou',
    'Jetzt': 'agora',
    'luftangriff': 'ataque aéreo',
    'rettedenKaiser': 'salve o imperador',
    'rufenwirdasjungeMadchenanundsehenwassiesagt': 'vamos chamar a jovem e ver o que ela diz',
    'startensiedenangriff': 'iniciar o ataque',
    'stehen': 'de pé',
    'treueundfreundlichkeit': 'fidelidade e bondade',
    'undheilen': 'e cure',
    'vordieserquelle': 'diante desta fonte',
    'wahrenddieSonnescheint': 'enquanto o sol brilhar',
}


# listar todos os arquivos que terminarm em .txt no diretorio atual do programa
def list_txt_files():
    current_dir = os.getcwd()
    txt_files = [file for file in os.listdir(current_dir) if file.endswith('.txt')]
    return txt_files

# converte ascii para byte
def gerar_mensagem(phrase,name):
    sequence_of_numbers = []
    for char in phrase:
        sequence_of_numbers.append(tabela_ascii_byte[char]) # adiciona o valor da tabela_ascii correspondente da letra escrita em binario.
    sequence_as_string = ''.join(sequence_of_numbers) # cria a string de sequencia de numeros
    with open(f"{name}.txt","a+") as fh:
        fh.write(sequence_as_string) # escreve a string de sequencia de numeros em um arquivo


# lê a string de numeros binario de 8 em 8, pois são bytes.
def read_string_in_chunks(string, chunk_size=8):
    for i in range(0, len(string), chunk_size): # para i no intervalo 0 até o tamanho da string de numeros binarios
        yield string[i:i+chunk_size] # devolve a string com o buffer de tamanho 8

# converte os arquivos com as strings em bytes para texto.
def byte_para_alemao(arquivo):
    letras = []
    palavras = []
    frases = []
    mensagem_em_chunks = []
    chunk_size = 8


    # abre a mensagem do arquivo de texto
    with open(f"{arquivo}","r") as fh:
        mensagem = fh.read(-1)

    # separa a mensagem em numeros binarios em formato de bytes (tamanho=8)
    for chunk in read_string_in_chunks(mensagem):
        mensagem_em_chunks.append(chunk)

    #verifica se a lista de chunks de bytes tem o caractere \n no final e se tiver retira ele da lista
    if mensagem_em_chunks[(len(mensagem_em_chunks)-1)] == "\n":
        mensagem_em_chunks.remove("\n")

    # converte byte para letra
    for chunk in mensagem_em_chunks:
        for letra,byte in tabela_ascii_byte.items():
            if chunk == byte:
                letras.append(letra)

    # separa as letras em frases
    for letra in letras:
        print(letra,end='')
    temp = ""
    for lta in letras:
        if lta == "$": # se a letra for $ substituir por " "
            temp +=" "
        elif lta == "%": # se for final da frase a string temp q está sendo modificada a cada iteração do loop vira uma frase que é armazenada na lista de frases
            frases.append(temp)
            temp = "" # reseta a string da frase temporaria para ser vazia
        else:
            temp += lta


    # separa as frases em palavras
    for frase in frases:
        palavras.append(frase.split())

    # cria um dicionario com as letras,palavras e frases do arquivo selecionado.
    byte_para_alemao_dict = {
        "letras":letras,
        "palavras":palavras,
        "frases":frases}

    return byte_para_alemao_dict

def ui():
    lista_de_mensagens = list_txt_files()
    print("_______________________________NOVA-SESSAO______________________________")
    print(f"Mensagens:{lista_de_mensagens}")
    arquivo = input("Qual eh o nome do arquivo que contem a mensagem (lembre-se de colocar .txt no final.) ? > ")
    if os.path.exists(arquivo):
        print(f"\nUsando a mensagem:",end='')
        texto_em_alemao = byte_para_alemao(arquivo)
        print('\n')
        print("Palavras do dicionario:",end="")
        for text_alem,text_port in dicionario_conhecido_sem_sinais.items(): # carregue todas as frases da tabela
                    for palavra in text_alem.split(): # separe as palavras de cada frase
                        print(palavra,end=';')
        print("\n\nPalavras e expressoes recuperadas:")
        for word_list in texto_em_alemao['palavras']:
            print("-->",end=" ")
            for word in word_list:
                print(word,end=";")
            print("")

        print("__________________________________________________________________")
        for word_list in texto_em_alemao["palavras"]: # para cada lista de palavras encontrada no arquivo
            for word in word_list: # carregue uma palavra da lista
                for text_alem,text_port in dicionario_conhecido_sem_sinais.items(): # carregue todas as frases da tabela
                    for palavra in text_alem.split(): # separe as palavras de cada frase
                        if word == palavra: # usa a palavra carregada da lista e compara com todas as palavras da tabela
                            print(f'''-> "{word}" Traducao: {text_port}\n''') # caso encontre imprima a traduçao


        print("_______________________________FIM-DA-SESSAO______________________________")

# loop principal do progama
def main():
    os.system("clear") # linux
    #os.system("cls")  # windows
    choice = input("Decodificar ou codificar mensagem (1|2)? >")

    if choice == "1":
        ui()
    elif choice == "2":
        print("Para facilitar ainda, será usado o caractere $ no lugar do espaço convencional para indicar fim de\numa palavra/expressão e início de outra palavra e expressão. Neste caso, para fins didáticos, o\nprimeiro caractere da mensagem será $ e para indicar fim da mensagem usaremos %.\n")
        print("EXEMPLO: 'was für ein schoner Tag' >> '$was$fur$ein$schoner$Tag%'\n")
        mensagem = input("Digite a Mensagem >")
        nome_mensagem = input("Digite o nome da mensagem >")
        gerar_mensagem(mensagem,nome_mensagem)
        print("Mensagem gerada.")
    else:
        print("Input invalido.")

    input("Aperte enter para continuar. . .")
    main()

if __name__ == "__main__":
    main()
