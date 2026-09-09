# Lógica

Neste exercicio precisei de duas tentátivas, primeiramente resolvi da seguinte maneira:

```
import sys
input = sys.stdin.readline
n = int(input())
ni = map(int, input().split())
print(len(set(ni)))
```

Ví que não passava na plataforma, apresentava TLE no caso de teste específico número 13, então pesquisei e descubri que o TLE nesse caso de teste acontece por causa de um anti-hash test case.

set em Python usa tabela de hash (média O(1) por inserção → O(n) total). No entanto, o **CSES** tem um teste construído de propósito para forçar muitas colisões no hash de Python, degradando o desempenho para O(n²) no pior caso. Por isso só esse teste dá TLE, enquanto os outros passam.

Com isso vi que a forma mais fiável é usar **sorted O(n log n)** garantido, sem hash:

```
import sys
input = sys.stdin.readline

n = int(input())
a = sorted(map(int, input().split()))
print(len(set(a)))
```

