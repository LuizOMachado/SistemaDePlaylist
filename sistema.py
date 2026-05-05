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
class NodoFila:
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None


class Fila:
    def __init__(self):
        self.frente = None
        self.tras = None

    def enqueue(self, musica):
        novo_nodo = NodoFila(musica)
        if self.tras is None:
            self.frente = novo_nodo
            self.tras = novo_nodo
        else:
            self.tras.proximo = novo_nodo
            self.tras = novo_nodo

    def dequeue(self):
        if self.frente is None:
            return None 
            
        nodo_removido = self.frente
        self.frente = self.frente.proximo
        
        if self.frente is None:
            self.tras = None
            
        nodo_removido.proximo = None
        return nodo_removido.musica

    def limpar(self):
        self.frente = None
        self.tras = None

    def esta_vazia(self):
        return self.frente is None

    def exibir_fila(self):
        if self.frente is None:
            print("A fila está vazia.")
            return
            
        atual = self.frente
        posicao = 1
        while atual is not None:
            print(f"{posicao}º -> {atual.musica.titulo} - {atual.musica.artista} ({atual.musica.bpm} BPM)")
            atual = atual.proximo
            posicao += 1

    def obter_tamanho(self):
        contador = 0
        atual = self.frente
        while atual is not None:
            contador += 1
            atual = atual.proximo
        return contador


def carregar_dados_iniciais(biblioteca):
  
    biblioteca.inserir_no_final(Musica(1, "Weightless", "Marconi Union", "Ambient", 60.0))
    biblioteca.inserir_no_final(Musica(2, "Clocks", "Coldplay", "Pop Rock", 121.0))
    biblioteca.inserir_no_final(Musica(3, "Stayin' Alive", "Bee Gees", "Disco", 103.0))
    biblioteca.inserir_no_final(Musica(4, "Titanium", "David Guetta", "Dance", 126.0))
    biblioteca.inserir_no_final(Musica(5, "Sandstorm", "Darude", "Electronic", 167.0))

def main():
    biblioteca = Biblioteca()
    carregar_dados_iniciais(biblioteca)
    
    fila_relaxar = Fila()
    fila_focar = Fila()
    fila_animar = Fila()
    fila_treinar = Fila()
    
    historico = Fila()
    proximo_id = 6
    
    while True:
        print("\n" + "="*40)
        print("=== Sistema de Playlist ===")
        print("="*40)
        print("1. Adicionar Música")
        print("2. Remover Música")
        print("3. Buscar Música")
        print("4. Listar Biblioteca")
        print("5. Montar Filas Automaticamente")
        print("6. Reproduzir Próxima (Por Humor)")
        print("7. Reproduzir Música Específica (Por ID)")
        print("8. Exibir Filas de Reprodução")
        print("9. Exibir Histórico")
        print("10. Estatísticas Oficiais")
        print("11. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            input("\nPressione Enter para confirmar a opção 1")
            print("\n--- Adicionar Música ---")
            titulo = input("Título: ")
            artista = input("Artista: ")
            genero = input("Gênero: ")
            bpm_str = input("BPM: ")
            
            try:
                bpm = float(bpm_str)
                if bpm <= 0:
                    print("Erro: O BPM deve ser maior que zero.")
                    continue
            except ValueError:
                print("Erro: Digite um valor numérico válido para o BPM.")
                continue
                
            nova_musica = Musica(proximo_id, titulo, artista, genero, bpm)
            biblioteca.inserir_no_final(nova_musica)
            print(f"Sucesso! Música adicionada com ID: {proximo_id}")
            proximo_id += 1
            
        elif opcao == "2":
            input("\nPressione Enter para confirmar a opção 2")
            print("\n--- Remover Música ---")
            id_str = input("ID da música a ser removida: ")
            try:
                id_remover = int(id_str)
                removido = biblioteca.remover_por_id(id_remover)
                if removido:
                    print("Música removida com sucesso da biblioteca.")
                else:
                    print("Erro: ID não encontrado.")
            except ValueError:
                print("Erro: O ID deve ser um número inteiro.")
                
        elif opcao == "3":
            input("\nPressione Enter para confirmar a opção 3")
            print("\n--- Buscar Música ---")
            print("1. Por ID")
            print("2. Por Título")
            tipo_busca = input("Opção de busca: ")
            
            if tipo_busca == "1":
                try:
                    id_busca = int(input("ID: "))
                    musica = biblioteca.buscar_por_id(id_busca)
                    if musica:
                        print(f"\n[Encontrada] {musica.titulo} - {musica.artista} ({musica.bpm} BPM)")
                    else:
                        print("Música não encontrada.")
                except ValueError:
                    print("Erro: O ID deve ser um número inteiro.")
            elif tipo_busca == "2":
                titulo_busca = input("Título: ")
                musica = biblioteca.buscar_por_titulo(titulo_busca)
                if musica:
                    print(f"\n[Encontrada] {musica.titulo} - {musica.artista} (ID: {musica.id})")
                else:
                    print("Música não encontrada.")
            else:
                print("Opção inválida.")
                
        elif opcao == "4":
            input("\nPressione Enter para confirmar a opção 4")
            print("\n--- Biblioteca ---")
            biblioteca.exibir_biblioteca()
                    
        elif opcao == "5":
            input("\nPressione Enter para confirmar a opção 5")
            print("\n--- Montando Filas Automaticamente ---")
            fila_relaxar.limpar()
            fila_focar.limpar()
            fila_animar.limpar()
            fila_treinar.limpar()
            
            atual = biblioteca.cabeca
            contador_total = 0
            
            while atual is not None:
                bpm = atual.musica.bpm
                
                if bpm <= 80:
                    fila_relaxar.enqueue(atual.musica)
                elif bpm <= 120:
                    fila_focar.enqueue(atual.musica)
                elif bpm <= 160:
                    fila_animar.enqueue(atual.musica)
                else:
                    fila_treinar.enqueue(atual.musica)
                    
                contador_total += 1
                atual = atual.proximo
                
            print(f"Sucesso! {contador_total} música(s) distribuída(s) nas filas.")
            
        elif opcao == "6":
            input("\nPressione Enter para confirmar a opção 6")
            print("\n--- Reproduzir Próxima (Por Humor) ---")
            print("Escolha a fila de humor desejada:")
            print("1. Relaxar")
            print("2. Focar")
            print("3. Animar")
            print("4. Treinar")
            
            escolha = input("Fila desejada: ")
            
            fila_alvo = None
            if escolha == "1": fila_alvo = fila_relaxar
            elif escolha == "2": fila_alvo = fila_focar
            elif escolha == "3": fila_alvo = fila_animar
            elif escolha == "4": fila_alvo = fila_treinar
            else:
                print("Opção de fila inválida.")
                continue
                
            if fila_alvo.esta_vazia():
                print("Erro: fila vazia ao tentar reproduzir")
            else:
                musica_tocando = fila_alvo.dequeue()
                print(f"\nTocando agora da fila:")
                print(f"ID: {musica_tocando.id} | Título: {musica_tocando.titulo} | Artista: {musica_tocando.artista} | Gênero: {musica_tocando.genero} | BPM: {musica_tocando.bpm}")
                historico.enqueue(musica_tocando)

        elif opcao == "7":
            input("\nPressione Enter para confirmar a opção 7")
            print("\n--- Reproduzir Música Específica (Por ID) ---")
            try:
                id_busca = int(input("Digite o ID da música que deseja ouvir: "))
                # Fazemos apenas a busca, preservando a música na Biblioteca e nas Filas de Humor
                musica_encontrada = biblioteca.buscar_por_id(id_busca)
                
                if musica_encontrada:
                    print(f"\nTocando agora (Reprodução Avulsa):")
                    print(f"ID: {musica_encontrada.id} | Título: {musica_encontrada.titulo} | Artista: {musica_encontrada.artista} | Gênero: {musica_encontrada.genero} | BPM: {musica_encontrada.bpm}")
                    historico.enqueue(musica_encontrada)
                else:
                    print("Erro: Música não encontrada na biblioteca.")
            except ValueError:
                print("Erro: O ID deve ser um número inteiro.")
                
        elif opcao == "8":
            input("\nPressione Enter para confirmar a opção 8")
            print("\n--- Exibir Filas de Reprodução ---")
            print("\n[Fila: Relaxar]")
            fila_relaxar.exibir_fila()
            print("\n[Fila: Focar]")
            fila_focar.exibir_fila()
            print("\n[Fila: Animar]")
            fila_animar.exibir_fila()
            print("\n[Fila: Treinar]")
            fila_treinar.exibir_fila()
                    
        elif opcao == "9":
            input("\nPressione Enter para confirmar a opção 9")
            print("\n--- Histórico de Reprodução ---")
            historico.exibir_fila()
                    
        elif opcao == "10":
            input("\nPressione Enter para confirmar a opção 10")
            print("\n--- Estatísticas Oficiais ---")
            print(f"Total de músicas na Biblioteca : {biblioteca.obter_tamanho()}")
            print(f"Tamanho Fila [Relaxar]         : {fila_relaxar.obter_tamanho()}")
            print(f"Tamanho Fila [Focar]           : {fila_focar.obter_tamanho()}")
            print(f"Tamanho Fila [Animar]          : {fila_animar.obter_tamanho()}")
            print(f"Tamanho Fila [Treinar]         : {fila_treinar.obter_tamanho()}")
            print(f"Total reproduzido (Histórico)  : {historico.obter_tamanho()}")
                
        elif opcao == "11":
            input("\nPressione Enter para confirmar a opção 11")
            print("\nLimpando memória e encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()


