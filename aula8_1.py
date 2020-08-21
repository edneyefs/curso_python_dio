def escrever_arquivo(texto):
    arquivo = open('aluno.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('aluno.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo)
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    escrever_arquivo('Primeira linha.\n')
    #atualizar_arquivo('Quarta linha.\n')
    #ler_arquivo('teste.txt')
