# Sistema de playlist
Este projeto consiste no desenvolvimento do backend de um sistema de gerenciamento de músicas, desenvolvido como requisito para a disciplina de Estrutura de Dados da Fatec Rio Claro. O foco principal é a aplicação prática de conceitos de alocação dinâmica e manipulação de ponteiros.

## Descrição do Projeto
O sistema permite a gestão completa de uma biblioteca musical e a organização de filas de reprodução baseadas no ritmo (BPM) das faixas cadastras. A solução foi projetada para operar em ambiente de terminal, oferecendo uma interface de menu para interação com o usuário.

## Restrições Técnicas
Conforme exigido pelos requisitos do projeto, o desenvolvimento seguiu as seguintes diretrizes:
Proibição total do uso de estruturas nativas do Python como list, dict, set ou módulos como collections.  
Implementação manual de todas as estruturas de dados utilizando classes de Nodos e referências de ponteiros.  
Utilização de Lista Encadeada Simples para a biblioteca principal.  
Utilização de Filas do tipo FIFO (First-In, First-Out) para as playlists de humor e histórico.

## Estrutura do Código
O software está dividido em classes com responsabilidades específicas:
Musica: Armazena os atributos id, título, artista, gênero e BPM.  
Biblioteca: Gerencia a lista encadeada principal, sendo responsável pela inserção ao final, busca e remoção por ID.  
Fila: Estrutura independente que gerencia as playlists de humor e o histórico de reprodução, implementando as funções enqueue e dequeue.  
Nodos: Classes auxiliares (NodoLista e NodoFila) que permitem a conexão entre os elementos através de referências.

## Funcionalidades Implementadas
Cadastro de músicas com geração automática de ID sequencial.  
Remoção de faixas via ID com rearranjo de ponteiros.  
Busca por ID ou Título na biblioteca.  
Listagem completa de faixas cadastradas.  
Distribuição automática em filas de humor:
Relaxar (até 80 BPM).  
Focar (81 a 120 BPM).  
Animar (121 a 160 BPM).  
Treinar (acima de 160 BPM).  
Reprodução sequencial por fila de humor com migração automática para o histórico.  
Reprodução avulsa via ID direto da biblioteca.  
Módulo de estatísticas com contagem manual de nós.

## Como Executar
Certifique-se de ter o Python 3 instalado. O programa não possui dependências externas.

Clone o repositório.

Navegue até a pasta do projeto.

Execute o comando:

python sistema.py
