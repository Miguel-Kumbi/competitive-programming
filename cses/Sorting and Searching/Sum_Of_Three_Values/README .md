# CSES — Sum of Three Values

Solução para o problema **[Sum of Three Values](https://cses.fi/problemset/task/1641)** do CSES.

## Abordagem

A solução utiliza a técnica de **Two Pointers**:

1. Cada valor é armazenado junto com seu índice original.
2. O array é ordenado pelos valores.
3. Para cada elemento `i`, utilizamos dois ponteiros:
   - `l` começa em `i + 1`;
   - `r` começa no final do array.
4. Calculamos `arr[i] + arr[l] + arr[r]`:
   - Se for igual ao alvo, encontramos a resposta.
   - Se for menor, avançamos `l`.
   - Se for maior, diminuímos `r`.
5. Os índices originais são retornados.

## Complexidade

- Ordenação: **O(n log n)**
- Busca com Two Pointers: **O(n²)**
- Complexidade total: **O(n²)**
- Espaço adicional: **O(n)**

## Técnica

**Python — Sorting + Two Pointers**
