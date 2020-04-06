
import  copy

class Cidade:
    def __init__(self, nome):
        self.nome = nome
        self.ligacoes = {}
        self.ligacoesC = {}


class ligacoes:
    def __init__(self):
        self.cidade = Cidade

class Global:

    #Criacao das cidades

    Aveiro = Cidade('Aveiro')
    Beja = Cidade('Beja')
    Braga = Cidade('Braga')
    Braganca = Cidade('Braganca')
    CasteloBranco = Cidade('Castelo Branco')
    Coimbra = Cidade('Coimbra')
    Evora = Cidade('Evora')
    Faro = Cidade('Faro')
    Guarda = Cidade('Guarda')
    Leiria = Cidade('Leiria')
    Lisboa = Cidade('Lisboa')
    Portalegre = Cidade('Portalegre')
    Porto = Cidade('Porto')
    Santarem = Cidade('Santarem')
    Setubal = Cidade('Setubal')
    VianaDoCastelo = Cidade('Viana do Castelo')
    VilaReal = Cidade('Vila Real')
    Viseu = Cidade('Viseu')

    Aveiro.ligacoes = [[Porto.nome, 68],  [Viseu.nome, 95], [Coimbra.nome, 68], [Leiria.nome, 115]]
    Braga.ligacoes = [[VianaDoCastelo.nome, 48], [VilaReal.nome, 106], [Porto.nome, 53]]
    Braganca.ligacoes = [[VilaReal.nome, 137], [Guarda.nome, 202]]
    Beja.ligacoes = [[Evora.nome, 78], [Setubal.nome, 142], [Faro.nome, 152]]
    CasteloBranco.ligacoes = [[Portalegre.nome, 80], [Guarda.nome, 106], [Coimbra.nome, 159], [Evora.nome, 203]]
    Coimbra.ligacoes = [[Viseu.nome, 96], [Leiria.nome, 67], [CasteloBranco.nome, 159], [Aveiro.nome, 68]]
    Evora.ligacoes = [[Lisboa.nome, 150], [Santarem.nome, 117], [Portalegre.nome, 131], [Setubal.nome, 103], [Beja.nome, 78], [CasteloBranco.nome, 203]]
    Faro.ligacoes = [[Setubal.nome, 249], [Lisboa.nome, 299], [Beja.nome, 152]]
    Guarda.ligacoes = [[VilaReal.nome, 157], [Viseu.nome, 85], [Braganca.nome, 202], [CasteloBranco.nome, 106]]
    Leiria.ligacoes = [[Lisboa.nome, 129], [Santarem.nome, 70], [Coimbra.nome, 67], [Aveiro.nome, 115]]
    Lisboa.ligacoes = [[Santarem.nome, 78], [Setubal.nome, 50], [Leiria.nome, 129], [Evora.nome, 150], [Faro.nome, 299]]
    Porto.ligacoes = [[VianaDoCastelo.nome, 71], [VilaReal.nome, 116], [Viseu.nome, 133], [Aveiro.nome, 68],[Braga.nome, 53]]
    Portalegre.ligacoes = [[CasteloBranco.nome, 80], [Evora.nome, 131]]
    Santarem.ligacoes = [[Leiria.nome, 70], [Lisboa.nome, 78], [Evora.nome, 117]]
    Setubal.ligacoes = [[Lisboa.nome, 50], [Evora.nome, 103], [Beja.nome, 142], [Faro.nome, 249]]
    VianaDoCastelo.ligacoes = [[Braga.nome, 48], [Porto.nome, 71]]
    VilaReal.ligacoes = [[Viseu.nome, 110], [Braga.nome, 106], [Porto.nome, 116], [Braganca.nome, 137], [Guarda.nome, 157]]
    Viseu.ligacoes = [[Guarda.nome, 85], [Aveiro.nome, 95], [Coimbra.nome, 96], [VilaReal.nome, 110], [Porto.nome, 133]]


    #ARRAY CIDADES

    arraycidades = [Aveiro, Braga, Braganca, Beja, CasteloBranco, Coimbra, Evora, Faro, Guarda, Leiria, Lisboa, Porto,
                    VilaReal, Santarem, Portalegre, VianaDoCastelo, Viseu, Setubal]
    #LISTA CIDADES
    listacidades = ['Aveiro', 'Beja', 'Braga', 'Braganca', 'CasteloBranco', 'Coimbra', 'Evora', 'Faro', 'Guarda',
                    'Leiria', 'Lisboa', 'Portalegre', 'Porto', 'Santarem', 'Setubal', 'VianaDoCastelo', 'VilaReal',
                    'Viseu']
    #DICIONARIO Cidades
    dicionariocidades = {1: 'Aveiro',
                         2: 'Beja',
                         3: 'Braga',
                         4: 'Braganca',
                         5: 'CasteloBranco',
                         6: 'Coimbra',
                         7: 'Evora',
                         8: 'Faro',
                         9: 'Guarda',
                         10: 'Leiria',
                         11: 'Lisboa',
                         12: 'Portalegre',
                         13: 'Porto',
                         14: 'Santarem',
                         15: 'Setubal',
                         16: 'VianaDoCastelo',
                         17: 'VilaReal',
                         18: 'Viseu'}


    iteracoes = 0
    listaux = []
    #variaveis Cego Profundidade
    list_cidadespassadas = []
    controlo = 0
    aux = 0

    # verificar input
    def VerifInputCidade(self, origi, destini):
        if destini != 0:
            if origi in Global.listacidades and destini in Global.listacidades:
                return True
            else:
                return False
        else:
            if origi in Global.listacidades:
                return True
            else:
                return False

    #Procura Cega - Profundidade - Sempre a esquerda
    def cegoprofundidade(self, origem, destino):
        if Global.controlo == 0:
            Global.list_cidadespassadas = [origem]
            Global.controlo = 1

        if Global.iteracoes > 300:
            print('Iteracoes infinitas, abortado')
            Global.list_cidadespassadas = []
            Global.iteracoes = 0
            Global.controlo = 0
        else:
            if Global.list_cidadespassadas[0] == destino:
                print('Viagem Acabou')
                print('Nº Interacoes: \n' , Global.iteracoes)
                Global.list_cidadespassadas = []
                Global.iteracoes = 0
                Global.controlo = 0
            else:

                for x in Global.arraycidades:
                    if x.nome == Global.list_cidadespassadas[0]:
                        for c in range(len(x.ligacoes)):
                            Global.list_cidadespassadas.insert(1 + c, x.ligacoes[c][0])
                Global.iteracoes += 1
                Global.list_cidadespassadas.pop(0)
                print('Iteracoes:' + str(Global.iteracoes) + '\n' + 'Cidade Origem:' + str(origem) + '\n Cidade Destino:' + str(destino) + '\n' + str(len(Global.list_cidadespassadas)))
                print('\n')
                print(Global.list_cidadespassadas)
                print('\n')
                Global.cegoprofundidade(self, origem, destino)

def menugeral():
        while True:
            print('*******************************')
            print('\*/   IA - Projeto Final     */')
            print('*/»»»»»»»»»»»»»««««««««««««««/*')
            print('*/   1 - Procura Cega        /*')
            print('*/                           /*')
            print('*/   2 - Procura heurística  /*')
            print('*/                           /*')
            print('*/   3 - Sair                /*')
            print('*/»»»»»»»»»»»»«««««««««««««««/*')
            print('\*/   Introduza uma opção:   */')
            print('*******************************')
            op = input()
            if int(op) == 1:
                menuprocuracega()
            elif int(op) == 2:
                menuprocuraheuristica()
            elif int(op) >= 3 or int(op) <= 0:
                print('Invalid selection!')
                break

def menuprocuracega():
        while True:
            print('*******************************')
            print('*/»»»»»»»»»»»»»««««««««««««««/*')
            print('*/ 1 - Custo uniforme        /*')
            print('*/ 2 -Profundidade limitada  /*')
            print('*/  3- Voltar                /*')
            print('*/  4 - Sair                 /*')
            print('*/»»»»»»»»»»»»«««««««««««««««/*')
            print('\*/   Introduza uma opção:   */')
            print('*******************************')
            op = input()
            if int(op) == 1:
                continue
            elif int(op) == 2:
                g = Global()
                partida = str(input('\nInsira a cidade de Partida: '))
                chegada = str(input('\n Insira a cidade de Chegada: '))
                if (g.VerifInputCidade(partida, chegada) == True):
                    g.cegoprofundidade(partida, chegada)
                else:
                    print('\t\t Nome da cidade incorreta!')
                    continue

            elif int(op) >= 3 or int(op) <= 0:
                print('Invalid selection!')
                break

def menuprocuraheuristica():
        while True:
            print('*******************************')
            print('*/»»»»»»»»»»»»»««««««««««««««/*')
            print('*/      1 - Procura sôfrega  /*')
            print('*/      2 - A*               /*')
            print('*/      3- Voltar            /*')
            print('*/      4 - Sair             /*')
            print('*/»»»»»»»»»»»»«««««««««««««««/*')
            print('\*/   Introduza uma opção:   */')
            print('*******************************')
            op = input()
            if int(op) == 1:
                continue
            elif int(op) == 2:
                continue
            elif int(op) == 3:
                return menugeral
            elif int(op) >= 4 or int(op) <= 0:
                print('Invalid selection!')
            return

menugeral()
