class Cidade:
    def __init__(self, nome):
        self.nome = nome
        self.ligacoes = {}

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

Aveiro.ligacoes = [[Porto.name, 68], [Coimbra.name, 68], [Viseu.name, 95], [Leiria.name, 115]]
Beja.ligacoes = [[Evora.name, 78], [Setubal.name, 142], [Faro.name, 152]]
Braga.ligacoes = [[VianaDoCastelo.name, 48], [VilaReal.name, 106], [Porto.name, 53]]
Braganca.ligacoes = [[VilaReal.name, 137], [Guarda.name, 202]]
CasteloBranco.ligacoes = [[Portalegre.name, 80], [Guarda.name, 106], [Coimbra.name, 159], [Evora.name, 203]]
Coimbra.ligacoes = [[Viseu.name, 96], [Leiria.name, 67], [CasteloBranco.name, 159], [Aveiro.name, 68]]
Evora.ligacoes = [[Lisboa.name, 150], [Santarem.name, 117], [Portalegre.name, 131], [Setubal.name, 103], [Beja.name, 78], [CasteloBranco.name, 203]]
Faro.ligacoes = [[Setubal.name, 249], [Lisboa.name, 299], [Beja.name, 152]]
Guarda.ligacoes = [[VilaReal.name, 157], [Viseu.name, 85], [Braganca.name, 202], [CasteloBranco.name, 106]]
Leiria.ligacoes = [[Lisboa.name, 129], [Santarem.name, 70], [Coimbra.name, 67], [Aveiro.name, 115]]
Lisboa.ligacoes = [[Santarem.name, 78], [Setubal.name, 50], [Leiria.name, 129], [Evora.name, 150], [Faro.name, 299]]
Portalegre.ligacoes = [[CasteloBranco.name, 80], [Evora.name, 131]]
Porto.ligacoes = [[VianaDoCastelo.name, 71], [VilaReal.name, 116], [Viseu.name, 133], [Aveiro.name, 68], [Braga.name, 53]]
Santarem.ligacoes = [[Leiria.name, 70], [Lisboa.name, 78], [Evora.name, 117]]
Setubal.ligacoes = [[Lisboa.name, 50], [Evora.name, 103], [Beja.name, 142], [Faro.name, 249]]   
VianaDoCastelo.ligacoes = [[Braga.name, 48], [Porto.name, 71]]
VilaReal.ligacoes = [[Viseu.name, 110], [Braga.name, 106], [Porto.name, 116], [Braganca.name, 137], [Guarda.name, 157]]
Viseu.ligacoes = [[Guarda.name, 85], [Aveiro.name, 95], [Coimbra.name, 96], [VilaReal.name, 110], [Porto.name, 133]]