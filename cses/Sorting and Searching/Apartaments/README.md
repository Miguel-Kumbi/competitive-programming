# CSES — Apartments

## 📌 Problema

Dado um conjunto de candidatos à procura de um apartamento e um conjunto de apartamentos disponíveis, devemos determinar o **número máximo de candidatos que podem receber um apartamento**.

Cada candidato possui um tamanho desejado `d`.

Um apartamento de tamanho `a` pode ser atribuído ao candidato quando:

```text
d - k ≤ a ≤ d + k
```

onde `k` é a tolerância permitida.

Cada candidato e cada apartamento só podem ser utilizados **uma vez**.

---

## 💡 Estratégia

A solução utiliza:

- **Ordenação**
- **Two Pointers (dois ponteiros)**

Primeiro ordenamos os dois arrays:

```python
desejados.sort()
disponiveis.sort()
```

Depois utilizamos dois índices:

```python
i = 0  # candidato atual
j = 0  # apartamento atual
```

A ideia é comparar sempre o **menor candidato ainda não atendido** com o **menor apartamento ainda disponível**.

---

## 🔎 Casos possíveis

Para cada par `desejados[i]` e `disponiveis[j]`, temos três situações.

### 1. Apartamento é pequeno demais

Se:

```text
apartamento < desejo - k
```

o apartamento não pode servir para o candidato atual.

Como os apartamentos estão ordenados, ele também não será adequado para candidatos que desejam apartamentos maiores.

Portanto, descartamos o apartamento:

```python
j += 1
```

---

### 2. Apartamento é compatível

Se:

```text
desejo - k ≤ apartamento ≤ desejo + k
```

temos um possível match.

Então atribuímos o apartamento ao candidato:

```python
rented += 1
i += 1
j += 1
```

Avançamos os dois ponteiros porque tanto o candidato quanto o apartamento já foram utilizados.

---

### 3. Apartamento é grande demais

Se:

```text
apartamento > desejo + k
```

o apartamento atual é grande demais para o candidato.

Como os apartamentos estão ordenados, os próximos apartamentos serão ainda maiores.

Logo, não adianta avançar `j`.

Podemos passar para o próximo candidato:

```python
i += 1
```

---

## 🧠 Exemplo

Considere:

```text
n = 4
m = 3
k = 5

desejados  = [60, 45, 80, 60]
disponiveis = [30, 60, 75]
```

Depois da ordenação:

```text
desejados  = [45, 60, 60, 80]
disponiveis = [30, 60, 75]
```

### Comparações

Para `45`:

```text
45 - 5 = 40
45 + 5 = 50
```

O apartamento `30` é pequeno demais:

```text
30 < 40
```

Então:

```text
j++
```

Agora temos:

```text
desejado = 45
apartamento = 60
```

`60` é grande demais para `45`, então:

```text
i++
```

Agora:

```text
desejado = 60
apartamento = 60
```

Existe compatibilidade:

```text
55 ≤ 60 ≤ 65
```

Então fazemos um match.

Depois:

```text
desejado = 60
apartamento = 75
```

Novamente:

```text
55 ≤ 75 ≤ 65
```

é falso, então o apartamento `75` é grande demais para esse candidato.

Avançamos o candidato:

```text
desejado = 80
apartamento = 75
```

Agora:

```text
75 ≤ 75 ≤ 85
```

Existe compatibilidade.

Resultado:

```text
2
```

---

## 💻 Implementação

```python
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

desejados = [int(v) for v in input().split()]
disponiveis = [int(v) for v in input().split()]

desejados.sort()
disponiveis.sort()

i = 0
j = 0
rented = 0

while i < n and j < m:
    if desejados[i] - k <= disponiveis[j] <= desejados[i] + k:
        rented += 1
        i += 1
        j += 1

    elif disponiveis[j] < desejados[i] - k:
        j += 1

    else:
        i += 1

print(rented)
```

---

## ⏱️ Complexidade

### Ordenação

Ordenamos os dois arrays:

```text
O(n log n) + O(m log m)
```

### Two Pointers

Cada ponteiro percorre seu array no máximo uma vez:

```text
O(n + m)
```

Portanto, a complexidade total é:

```text
O(n log n + m log m)
```

A memória adicional utilizada pela estratégia de dois ponteiros é:

```text
O(1)
```

desconsiderando a memória utilizada pelos próprios arrays.

---

## 🎯 Insight principal

O ponto fundamental é perceber que **a ordenação elimina a necessidade de testar todas as combinações possíveis**.

Sem ordenação, poderíamos acabar comparando cada candidato com vários apartamentos.

Com os arrays ordenados, quando sabemos que um apartamento é:

- **pequeno demais** → descartamos o apartamento;
- **compatível** → fazemos o match;
- **grande demais** → passamos para o próximo candidato.

Assim, cada elemento é processado de forma eficiente usando a técnica de **Two Pointers**.