# Sudoku Generator and Solver

## Descrição

Este projeto é um gerador e solucionador de tabuleiros de Sudoku. O gerador cria um tabuleiro de Sudoku válido preenchido com números de 1 a 9, respeitando as regras do jogo, enquanto o solucionador pode preencher um tabuleiro de Sudoku com algumas células vazias (zero) para criar um quebra-cabeça jogável.

## Funcionalidades

- **Geração de Tabuleiro**: Cria um tabuleiro de Sudoku completamente preenchido, respeitando todas as regras do jogo.
- **Preenchimento Aleatório**: Preenche o tabuleiro com números aleatórios de 1 a 9, mantendo alguns espaços com zeros.
- **Validação de Regras**: Garante que os números não se repitam em linhas, colunas ou blocos 3x3.
- **Visualização**: Exibe o tabuleiro em um formato amigável, com separadores entre blocos 3x3.

## Estrutura do Projeto

1. **Funções Principais**:
    - `create_table(tamanho)`: Cria um tabuleiro de Sudoku de tamanho especificado, preenchido inicialmente com zeros.
    - `is_valid(tabuleiro, num, row, col)`: Verifica se um número pode ser colocado na posição especificada sem violar as regras do Sudoku.
    - `fill_board(tabuleiro)`: Preenche o tabuleiro seguindo as regras do Sudoku usando o algoritmo de backtracking.
    - `print_board(tabuleiro)`: Exibe o tabuleiro no formato 9x9 com separadores entre blocos 3x3.

2. **Dependências**:
    - Nenhuma dependência externa além do módulo padrão `random` do Python.

## Uso

1. **Configuração do Ambiente**:
    - Certifique-se de ter o Python 3.x instalado.

2. **Executar o Projeto**:
    - Clone o repositório:
      ```bash
      git clone <URL-do-repositorio>
      cd <diretorio-do-repositorio>
      ```
    - Execute o script Python:
      ```bash
      python sudoku.py
      ```

3. **Exemplo de Código**:
    ```python
    import random

    def create_table(tamanho):
        # Tabuleiro 'tamanho x tamanho' preenchido com zeros
        tabuleiro = [[0 for _ in range(tamanho)] for _ in range(tamanho)]
        return tabuleiro

    def is_valid(tabuleiro, num, row, col):
        # Verificar se o número já está na linha
        for i in range(len(tabuleiro[0])):
            if tabuleiro[row][i] == num:
                return False

        # Verificar se o número já está na coluna
        for i in range(len(tabuleiro)):
            if tabuleiro[i][col] == num:
                return False

        # Verificar se o número já está no bloco 3x3
        box_start_row = row - row % 3
        box_start_col = col - col % 3

        for i in range(3):
            for j in range(3):
                if tabuleiro[box_start_row + i][box_start_col + j] == num:
                    return False

        return True

    def fill_board(tabuleiro):
        """
        Preenche o tabuleiro de acordo com as regras do Sudoku.
        """
        tamanho = len(tabuleiro)
        
        for row in range(tamanho):
            for col in range(tamanho):
                # Preencher apenas se a célula estiver vazia (zero)
                if tabuleiro[row][col] == 0:
                    # Tentar colocar um número de 1 a 9 que respeite as regras do Sudoku
                    numeros_possiveis = list(range(1, 10))
                    random.shuffle(numeros_possiveis)  # Embaralhar os números para inserir de forma aleatória

                    for num in numeros_possiveis:
                        if is_valid(tabuleiro, num, row, col):
                            tabuleiro[row][col] = num
                            # Recursão para preencher o restante do tabuleiro
                            if fill_board(tabuleiro):
                                return True
                            # Se não conseguir preencher o restante, desfazer a última inserção (backtracking)
                            tabuleiro[row][col] = 0
                    
                    # Se nenhum número funcionar, retornar falso para o backtracking
                    return False
        
        return True

    def print_board(tabuleiro):
        tamanho = len(tabuleiro)
        for i in range(tamanho):
            if i % 3 == 0 and i != 0:
                print("- " * (tamanho + (tamanho // 3 - 1)))  # Linha separadora a cada 3 linhas
            for j in range(tamanho):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")  # Linha separadora a cada 3 colunas
                if j == tamanho - 1:
                    print(tabuleiro[i][j])
                else:
                    print(str(tabuleiro[i][j]) + " ", end="")

    # Exemplo de uso
    tamanho_tabuleiro = 9  # Tamanho do tabuleiro (para Sudoku é 9x9)
    board = create_table(tamanho_tabuleiro)
    fill_board(board)  # Preenche o tabuleiro de acordo com as regras do Sudoku
    print_board(board)
    ```

## Testes

- **Verificação Manual**: Após executar o código, verifique se o tabuleiro gerado está correto e se atende às regras do Sudoku.
- **Testes Adicionais**: Adicione diferentes tamanhos de tabuleiro e ajuste as probabilidades de zeros para ver como o algoritmo se comporta.

## Contribuições

Se você deseja contribuir para o projeto, siga estes passos:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (`git checkout -b feature-nome`).
3. Faça commit das suas alterações (`git commit -am 'Adiciona nova feature'`).
4. Envie sua branch para o repositório (`git push origin feature-nome`).
5. Abra um Pull Request.

Sinta-se à vontade para personalizar este README conforme necessário para refletir com mais precisão o seu projeto e suas preferências.
