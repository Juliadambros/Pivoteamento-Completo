def pivoteamento_completo(A, b):
    n = len(A)
    ordem = list(range(n))  # ordem das variáveis
    multiplicadores = []  #  armazenar os multiplicadores


    for i in range(n):
        A[i].append(b[i])

    for k in range(n - 1):  
        # Encontrar o pivô máximo 
        max_val = 0
        max_i, max_j = k, k
        for i in range(k, n):
            for j in range(k, n):
                if abs(A[i][j]) > max_val:
                    max_val = abs(A[i][j])
                    max_i, max_j = i, j

        print(f"\nIteração {k + 1}: Pivô escolhido é A[{max_i}][{max_j}] = {A[max_i][max_j]}")

        # Trocar as linhas 
        if max_i != k:
            A[k], A[max_i] = A[max_i], A[k]
            print(f"Trocando linha {k} com linha {max_i}")

        # Trocar as colunas 
        if max_j != k:
            for row in A:
                row[k], row[max_j] = row[max_j], row[k]
            ordem[k], ordem[max_j] = ordem[max_j], ordem[k]
            print(f"Trocando coluna {k} com coluna {max_j}")

        print("Matriz após trocas:")
        for row in A:
            print(row)

        # zerar os elementos abaixo do pivô
        for i in range(k + 1, n):
            fator = A[i][k] / A[k][k]
            multiplicadores.append((i, k, fator))  
            for j in range(k, n + 1):  # n+1 inclui a coluna do vetor b
                A[i][j] -= fator * A[k][j]

        print("Matriz após eliminação:")
        for row in A:
            print(row)

    print("\nMultiplicadores (m_ij):")
    for m in multiplicadores:
        print(f"m_{m[0] + 1}{m[1] + 1} = {m[2]}")

    # Substituição regressiva para encontrar a solução
    x = [0] * n
    for i in range(n - 1, -1, -1):
        soma = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (A[i][n] - soma) / A[i][i]

    # Reordenar (x1,x2.....)
    solucao_final = [0] * n
    for i, idx in enumerate(ordem):
        solucao_final[idx] = x[i]

    return solucao_final


A = [
    [2, -1, 3, 5],
    [6, -3, 12, 11],
    [4, -1, 10, 8],
    [0, -2, -8, 10]
]
b = [-7, 4, 4, -60]

solucao = pivoteamento_completo(A, b)
print("\nSolução do sistema:", solucao)
