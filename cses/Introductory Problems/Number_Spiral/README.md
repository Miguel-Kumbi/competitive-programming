# Number Spiral — CSES

## Problema

Dadas coordenadas `(y, x)` em uma matriz preenchida em espiral, determine o número que está nessa posição.

Exemplo:

```text
1   2   9  10  25
4   3   8  11  24
5   6   7  12  23
16 15  14  13  22
17 18  19  20  21
```

## Ideia

Não construímos a matriz. Para cada posição:

```text
n = max(y, x)
```

O maior número do quadrado `n × n` é:

```text
n²
```

A posição de `n²` depende da paridade de `n`:

- **n ímpar:** `n²` fica no canto superior direito.
- **n par:** `n²` fica no canto inferior esquerdo.

A partir disso, calculamos diretamente o valor da posição.

### Fórmulas

**n ímpar:**

```python
if x == n:
    pos_xy = n*n - y + 1
else:
    pos_xy = (n-1)*(n-1) + x
```

**n par:**

```python
if y == n:
    pos_xy = n*n - x + 1
else:
    pos_xy = (n-1)*(n-1) + y
```

## Complexidade

Para cada consulta:

- **Tempo:** `O(1)`
- **Memória:** `O(1)`

A matriz não é construída; o resultado é obtido diretamente através das coordenadas e da paridade de `n`.

## Insight

O ponto principal é identificar o **quadrado externo** ao qual `(y, x)` pertence e usar `n²` como referência. A direção da espiral alterna conforme `n` é par ou ímpar.
