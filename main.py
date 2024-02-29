import os
# Exercicio 1: Maquinas de turing.
'''
2.1 Nível 0
Implementação de uma conversão se números binários para caracteres da tabela ASCII, no filme
era em código morse. O código será passado em bytes e será convertido em um conjunto de
caracteres que formará um texto em alemão.
NOTA: praticamente todos os alunos fizeram a disciplina de AED, uma olhadinha nos
trabalhos que foram feitos naquela disciplina vai ajudar bastante.
2.2 Nível 1
Implementação de uma conversão de alemão para português, porém, para facilitar a conversão
será criado um dicionário de conversão direta de palavras ou expressões que pode ser criada
diretamente no programa não necessitando de um arquivo externo, por exemplo, condicionais if-
else para tal conversão.
2.3 Nível 2
Com a conversão do código para português, tentar descobrir o local do ataque.
'''

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
    ' an meine Verwandten ': 'para os meus parentes',
    ' ankommen ': 'chegar',
    ' bleibe ': 'permaneça',
    ' David ging zu Ahimelechs Haus ': 'Davi foi à casa de Aimeleque',
    ' David, als er in der Höhle war ': 'Davi, quando ele estava na caverna',
    ' dein name ': 'seu nome',
    ' dein Ruhm ': 'a sua fama',
    ' du wirst frei sein ': 'você estará livre',
    ' für immer ': 'para sempre',
    ' gefangene ': 'prisioneiros',
    ' hier bin ich ': 'aqui estou',
    ' Jetzt ': 'agora',
    ' luftangriff ': 'ataque aéreo',
    ' rette den Kaiser ': 'salve o imperador',
    ' rufen wir das junge Mädchen an und sehen, was sie sagt ': 'vamos chamar a jovem e ver o que ela diz',
    ' starten sie den angriff ': 'iniciar o ataque',
    ' stehen ': 'de pé',
    ' treue und freundlichkeit ': 'fidelidade e bondade',
    ' und heilen ': 'e cure',
    ' vor dieser quelle ': 'diante desta fonte',
    ' wahrend die Sonne scheint ': 'enquanto o sol brilhar',
    ' ': 'fim da mensagem'
}


def gerar_mensagem(phrase):
    # converte ascii para byte
    sequence_of_numbers = []
    for char in phrase:
        sequence_of_numbers.append(tabela_ascii_byte[char])
    sequence_as_string = ''.join(sequence_of_numbers)
    files_and_directories = os.listdir()
    # Get the number of files
    number_of_files = len(files_and_directories)
    with open(f"mensagem{number_of_files}.txt","a+") as fh:
        fh.write(sequence_as_string)
    return sequence_as_string

def read_string_in_chunks(string, chunk_size=8):
    for i in range(0, len(string), chunk_size):
        yield string[i:i+chunk_size]

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
    temp = ""
    #print(letras)
    for lta in letras:
        #print(lta,end="")
        if lta == "$":
            temp +=" "
        elif lta == "%":
            frases.append(temp)
            temp = ""
        else:
            temp += lta
        #print(temp)


    # separa as frases em palavras
    for frase in frases:
        palavras.append(frase.split())

    byte_para_alemao_dict = {
        "letras":letras,
        "palavras":palavras,
        "frases":frases}

    return byte_para_alemao_dict

def test():

    #print(gerar_mensagem("$wahrend$die$Sonne$scheint$%")) # mensagem3.txt
    #print("-"*50)
    #print(gerar_mensagem("$vor$dieser$quelle$%")) # mensagem4.txt
    #print("-"*50)
    #print(gerar_mensagem("$vor$dieser$quelle$%$wahrend$die$Sonne$scheint$%")) # mensagem5.txt

    texto_em_alemao = byte_para_alemao("mensagem3.txt")
    texto_em_alemao1 = byte_para_alemao("mensagem4.txt")
    texto_em_alemao2 = byte_para_alemao("mensagem5.txt")

    print("\n")
    print("#"*100)
    print("Tabela de tradução dos arquivos [mensagem3.txt,mensagem4.txt,mensagem5.txt]")
    print("#"*100)
    print("\n")
    print("·"*100)
    print()
    for phrase in texto_em_alemao["frases"]:
        for phrase_known,traducao in dicionario_conhecido_sem_sinais.items():
            if phrase == phrase_known:
                print(f"Mensagem:mensagem3.txt\nFrase em Alemao: '{phrase}'\n\nTraducao:{traducao}\n")
                print("·"*100)
                print()
    for phrase in texto_em_alemao1["frases"]:
        for phrase_known,traducao in dicionario_conhecido_sem_sinais.items():
            if phrase == phrase_known:
                print(f"Mensagem:mensagem4.txt\nFrase em Alemao: '{phrase}'\n\nTraducao:{traducao}\n")
                print("·"*100)
                print()
    for phrase in texto_em_alemao2["frases"]:
        for phrase_known,traducao in dicionario_conhecido_sem_sinais.items():
            if phrase == phrase_known:
                print(f"Mensagem:mensagem5.txt\nFrase em Alemao: '{phrase}'\n\nTraducao:{traducao}\n")
                print("·"*100)
                print()
def ui():
    arquivo = input("Qual eh o nome do arquivo que contem a mensagem ? > ")
#'''
    if os.path.exists(arquivo):
        print("_______________________________NOVA-SESSAO______________________________")
        print(f"Usando a mensagem: {arquivo}")
        texto_em_alemao = byte_para_alemao(arquivo)
        print("____________________________TABELA-DE-FRASES____________________________")
        print("Compara as frases obtidas nas mensagens com as frases da tabela fornecida.")
        print("________________________________________________________________________")
        for phrase in texto_em_alemao["frases"]:
            for phrase_known,traducao in dicionario_conhecido_sem_sinais.items():
                if phrase == phrase_known:
                    print(f"Frase em Alemao: '{phrase}'\ntraducao: {traducao}\n")
        print("_________________________FIM-DA-TABELA-DE-FRASES________________________\n")

    # separar palavra por palavra
    print("____________________________WORD-TABLE____________________________")
    print("Tabela utilizada para encontrar palavras em frases alemãs e a tr-\nadução dessas frases.Utilizado quando uma mensagem NÃO contem fra-\nses coerentes que possam ser utilizadas de forma integra na tabela\nde traducao.")
    print("__________________________________________________________________")
    for word_list in texto_em_alemao["palavras"]:
        for word in word_list:
            for text_alem,text_port in dicionario_conhecido_sem_sinais.items():
                for palavra in text_alem.split():
                    if word == palavra:
                        print(f'''A palavra: -> "{word}" <- está presente na frase:{text_alem}\nTraducao: {text_port}\n''')

    print("_________________________END-OF-WORD-TABLE_________________________\n")

    print("_______________________________FIM-DA-SESSAO______________________________")






def main():
    #test()

    ui()

main()

































