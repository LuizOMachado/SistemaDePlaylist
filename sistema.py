class Musica:
    def __init__(self, id_musica, titulo, artista, genero, bpm):
        self.id = id_musica
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm


class NodoLista:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None


class Biblioteca:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def inserir_no_final(self, musica):
        novo_nodo = NodoLista(musica)
        if self.cabeca is None:
            self.cabeca = novo_nodo
            self.cauda = novo_nodo
        else:
            self.cauda.proximo = novo_nodo
            self.cauda = novo_nodo
