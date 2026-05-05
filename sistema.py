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
    def remover_por_id(self, id_musica):
        atual = self.cabeca
        anterior = None
        
        while atual is not None:
            if atual.musica.id == id_musica:
                if anterior is None:
                    self.cabeca = atual.proximo
                    if self.cabeca is None:
                        self.cauda = None
                else:
                    anterior.proximo = atual.proximo
                    if atual.proximo is None:
                        self.cauda = anterior
                
                atual.proximo = None
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def buscar_por_id(self, id_musica):
        # Varredura linear pela lista encadeada (O(n))
        atual = self.cabeca
        while atual is not None:
            if atual.musica.id == id_musica:
                return atual.musica
            atual = atual.proximo
        return None

    def buscar_por_titulo(self, titulo):
        atual = self.cabeca
        while atual is not None:
            if atual.musica.titulo.lower() == titulo.lower():
                return atual.musica
            atual = atual.proximo
        return None

    def exibir_biblioteca(self):
        if self.cabeca is None:
            print("A biblioteca está vazia.")
            return
            
        atual = self.cabeca
        while atual is not None:
            m = atual.musica
            print(f"ID: {m.id} | {m.titulo} - {m.artista} ({m.bpm} BPM) [{m.genero}]")
            atual = atual.proximo

    def obter_tamanho(self):
        contador = 0
        atual = self.cabeca
        while atual is not None:
            contador += 1
            atual = atual.proximo
        return contador


