
#metodo escrever
def escrever_arquivo(texto):
    diretorio = 'home/ti/Música/projetos'
    arquivo = open('diretorio', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open('teste.txt', 'a')
    arquivo.write(texto)
    arquivo.close()
   # leitura do arquivo
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    print(aluno_nota)
    #for x in aluno_nota:
    #print(x)


if __name__ == '__main__':
    media_notas(('notas.txt'))
   # atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('teste.txt')
    #escrever_arquivo('primeira linha ')
    #aluno = 'maria, 10, 10,10'
#arquivo  = open('teste.txt', 'a')
#arquivo.write('\n Não desistir Meta'\n)
#arquivo.close()
#arquivo.write('Vou vencer no python')
#arquivo.close()