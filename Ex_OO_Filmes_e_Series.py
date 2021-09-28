def exemplo_likes(vingadores, atlanta, tmep, demolidor):
    vingadores.dar_like()
    vingadores.dar_like()
    vingadores.dar_like()
    vingadores.dar_like()
    vingadores.dar_like()
    vingadores.dar_like()
    vingadores.dar_like()
    vingadores.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()
    tmep.dar_like()
    tmep.dar_like()
    tmep.dar_like()
    tmep.dar_like()
    atlanta.dar_like()
    atlanta.dar_like()
    atlanta.dar_like()
    atlanta.dar_like()
    atlanta.dar_like()
    atlanta.dar_like()

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.duracao} min  - {programa.likes} likes"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.temporadas} temporadas  - {programa.likes} likes"


class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas) 

    


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
tmep = Filme("Todo mundo em pânico", 2000, 100)
demolidor = Serie("Demolidor", 2015, 3)

exemplo_likes(vingadores, atlanta, tmep, demolidor)

filmes_e_series = [vingadores, atlanta, tmep, demolidor]
playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)


for programa in playlist_fim_de_semana:
    print(programa)
