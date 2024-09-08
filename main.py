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
                # Embaralhar os números para inserir de forma aleatória
                random.shuffle(numeros_possiveis)

                for num in numeros_possiveis:
                    if is_valid(tabuleiro, num, row, col):
                        tabuleiro[row][col] = num
                        print_board(tabuleiro)
                        print("\n")
                        # Recursão para preencher o restante do tabuleiro
                        if fill_board(tabuleiro):
                            return True
                        # Se não conseguir preencher o restante, desfazer a última inserção (backtracking)
                        tabuleiro[row][col] = 0
                        print_board(tabuleiro)
                        print("\n")

                # Se nenhum número funcionar, retornar falso para o backtracking
                return False

    return True


def print_board(tabuleiro):
    tamanho = len(tabuleiro)
    for i in range(tamanho):
        if i % 3 == 0 and i != 0:
            # Linha separadora a cada 3 linhas
            print("- " * (tamanho + (tamanho // 3 - 1)))
        for j in range(tamanho):
            if j % 3 == 0 and j != 0:
                print("| ", end="")  # Linha separadora a cada 3 colunas
            if j == tamanho - 1:
                print(tabuleiro[i][j])
            else:
                print(str(tabuleiro[i][j]) + " ", end="")


def remove_numbers(tabuleiro, n_removals):
    """
    Remove números do tabuleiro para criar espaços vazios (zeros), respeitando a estrutura de Sudoku.
    """
    tamanho = len(tabuleiro)
    count = 0

    while count < n_removals:
        # Escolher uma posição aleatória na matriz
        row = random.randint(0, tamanho - 1)
        col = random.randint(0, tamanho - 1)

        # Apenas remover o número se a célula não estiver vazia
        if tabuleiro[row][col] != 0:
            tabuleiro[row][col] = 0
            count += 1


def solve_sudoku(tabuleiro):
    """
    Tenta resolver o tabuleiro de Sudoku usando backtracking.
    """
    tamanho = len(tabuleiro)

    # Encontra uma célula vazia (com valor 0)
    for row in range(tamanho):
        for col in range(tamanho):
            if tabuleiro[row][col] == 0:
                # Testa números de 1 a 9 para essa célula
                for num in range(1, 10):
                    if is_valid(tabuleiro, num, row, col):
                        tabuleiro[row][col] = num

                        # Recursivamente tenta preencher o restante
                        if solve_sudoku(tabuleiro):
                            return True

                        # Se falhar, volta atrás e tenta outro número
                        tabuleiro[row][col] = 0

                # Se nenhum número funcionar, retorna falso
                return False

    # Se não encontrar células vazias, o Sudoku está resolvido
    return True


board = create_table(9)
fill_board(board)
remove_numbers(board, 45)

if solve_sudoku(board):
    print("Sudoku resolvido com sucesso!")
    print("\n")
else:
    print("Não foi possível resolver o Sudoku.")
    print("\n")

print_board(board)
print("\n")