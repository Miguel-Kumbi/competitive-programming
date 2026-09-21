import sys
import math
import io
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right, insort
from heapq import heappush, heappop, heapify
from functools import lru_cache, cmp_to_key
from itertools import accumulate, permutations, combinations, product

input = sys.stdin.readline
sys.setrecursionlimit(1 << 25)

# ============================================================================
# ALGORITIMOS
# ============================================================================

def special_two_pointer(arr: list, n: int, target: int) -> str:
	"""Inclui two pointers e para sum of two values e sum of three values"""
	for i in range(n-2):
		l = i + 1
		r = n - 1
		while l < r:
			_sum = arr[i][0] + arr[l][0] + arr[r][0]
			if _sum == target:
				return f'{arr[i][1] + 1} {arr[l][1] + 1} {arr[r][1] + 1}'
			elif _sum < target:
				l += 1
			else:
				r -= 1
	return 'IMPOSSIBLE'

# ============================================================================
# MATEMÁTICA / TEORIA DE NÚMEROS
# ============================================================================

def gcd(a, b):
    """Máximo divisor comum. O(log(min(a,b)))"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Mínimo múltiplo comum."""
    return a // gcd(a, b) * b

def extended_gcd(a, b):
    """
    Resolve a*x + b*y = gcd(a,b).
    PROBLEMA: útil para achar inverso modular quando mod não é primo,
    ou para resolver equações diofantinas lineares.
    Retorna (g, x, y) tal que a*x + b*y = g = gcd(a,b).
    """
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def mod_inverse(a, mod):
    """
    Inverso modular de a mod m (a^-1 tal que a*a^-1 ≡ 1 mod m).
    Usa Euclides estendido -> funciona mesmo se mod não for primo,
    desde que gcd(a, mod) == 1.
    Se mod for primo, também podes usar pow(a, mod-2, mod) (Fermat).
    """
    g, x, _ = extended_gcd(a, mod)
    if g != 1:
        raise ValueError("Inverso modular não existe (gcd != 1)")
    return x % mod

def power_I(a, b, mod=None):
    """Exponenciação rápida a^b (mod m se dado). O(log b)."""
    return pow(a, b, mod) if mod else pow(a, b)
    
def power_II(a, b,, c mod=None):
    """Exponenciação rápida a^(b ^c) (mod m se dado)."""
    bc = pow(b, c, mod - 1)
    return pow(a, bc, mod) if mod else pow(a, b, c)

def sieve(n):
    """
    Crivo de Eratóstenes: descobre quais números <= n são primos.
    PROBLEMA: "quais números até N são primos?" / contagem de primos.
    Complexidade: O(n log log n)
    Retorna: lista booleana is_prime[0..n]
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

def smallest_prime_factor_sieve(n):
    """
    Crivo do menor fator primo (SPF - smallest prime factor).
    PROBLEMA: fatorizar MUITOS números rapidamente (várias queries),
    já que fatorizar um número usando spf é O(log n) em vez de O(sqrt n).
    Complexidade construção: O(n log log n)
    Uso:
        spf = smallest_prime_factor_sieve(10**6)
        fatores = factorize_with_spf(360, spf)  # -> {2:3, 3:2, 5:1}
    """
    spf = list(range(n + 1))
    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == i:  # i é primo
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def factorize_with_spf(x, spf):
    """Fatoriza x usando o crivo SPF. Retorna dict {primo: expoente}."""
    fatores = {}
    while x > 1:
        p = spf[x]
        fatores[p] = fatores.get(p, 0) + 1
        x //= p
    return fatores

def factorize(n):
    """
    Fatorização por tentativa de divisão (sem crivo prévio).
    PROBLEMA: fatorizar UM número isolado, n até ~10^12.
    Complexidade: O(sqrt(n))
    """
    fatores = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            fatores[d] = fatores.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        fatores[n] = fatores.get(n, 0) + 1
    return fatores


class Combinatorics:
    """
    Pré-calcula fatoriais e inversos para responder C(n, k) mod p em O(1)
    depois de um pré-processamento O(N).
    PROBLEMA: contar combinações/arranjos módulo primo, muito comum em
    contagem combinatória (ex: "de quantas formas...").
    Uso:
        comb = Combinatorics(200000, 10**9+7)
        comb.C(10, 3)  # -> 120
    """
    def __init__(self, max_n, mod):
        self.mod = mod
        self.fact = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            self.fact[i] = self.fact[i - 1] * i % mod
        self.inv_fact = [1] * (max_n + 1)
        self.inv_fact[max_n] = pow(self.fact[max_n], mod - 2, mod)
        for i in range(max_n, 0, -1):
            self.inv_fact[i - 1] = self.inv_fact[i] * i % mod

    def C(self, n, k):
        """Combinação C(n, k) mod p. Retorna 0 se k inválido."""
        if k < 0 or k > n:
            return 0
        return self.fact[n] * self.inv_fact[k] % self.mod * self.inv_fact[n - k] % self.mod

    def P(self, n, k):
        """Arranjo (permutação) P(n, k) mod p."""
        if k < 0 or k > n:
            return 0
        return self.fact[n] * self.inv_fact[n - k] % self.mod

# ============================================================================
# GRAFOS
# ============================================================================

def bfs(graph, start):
    """
    Busca em Largura.
    PROBLEMA: menor número de arestas (caminho mínimo em grafo NÃO
    ponderado) a partir de `start` até todos os outros nós.
    Complexidade: O(V + E)
    Retorna: dist[] com distância mínima (em nº de arestas), -1 se inalcançável.
    """
    n = len(graph)
    dist = [-1] * n
    dist[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

def dfs_iterative(graph, start):
    """
    Busca em Profundidade (versão iterativa, evita estourar recursão).
    PROBLEMA: percorrer/marcar todos os nós alcançáveis a partir de start.
    Complexidade: O(V + E)
    Retorna: conjunto de nós visitados (na ordem de visita, se precisares).
    """
    visited = [False] * len(graph)
    order = []
    stack = [start]
    visited[start] = True
    while stack:
        u = stack.pop()
        order.append(u)
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    return order

def dijkstra(graph, start):
    """
    Dijkstra: caminho mais curto a partir de um nó, com pesos NÃO negativos.
    PROBLEMA: menor "custo" para chegar a cada nó a partir de start,
    quando as arestas têm pesos positivos.
    Complexidade: O((V + E) log V) usando heap.
    graph: lista de adjacência, graph[u] = [(v, peso), ...]
    """
    n = len(graph)
    dist = [math.inf] * n
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heappush(pq, (nd, v))
    return dist

def bellman_ford(n, edges, start):
    """
    Bellman-Ford: caminho mais curto, aceita pesos NEGATIVOS
    (mas deteta ciclos negativos).
    PROBLEMA: igual ao Dijkstra mas quando há arestas negativas.
    Complexidade: O(V * E)
    edges: lista de (u, v, peso)
    Retorna: (dist[], tem_ciclo_negativo: bool)
    """
    dist = [math.inf] * n
    dist[start] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != math.inf and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    tem_ciclo_negativo = False
    for u, v, w in edges:
        if dist[u] != math.inf and dist[u] + w < dist[v]:
            tem_ciclo_negativo = True
            break
    return dist, tem_ciclo_negativo

def floyd_warshall(n, dist_matrix):
    """
    Floyd-Warshall: caminho mais curto entre TODOS os pares de nós.
    PROBLEMA: preciso saber a distância mínima entre qualquer par (i, j),
    grafo pequeno (n até ~400-500).
    Complexidade: O(V^3)
    dist_matrix: matriz n x n, dist_matrix[i][j] = peso da aresta i->j
                 (math.inf se não existe, 0 na diagonal).
    Modifica a matriz in-place e retorna-a.
    """
    for k in range(n):
        dk = dist_matrix[k]
        for i in range(n):
            dik = dist_matrix[i][k]
            if dik == math.inf:
                continue
            row = dist_matrix[i]
            for j in range(n):
                if dik + dk[j] < row[j]:
                    row[j] = dik + dk[j]
    return dist_matrix

def topological_sort(graph, n):
    """
    Ordenação topológica (Kahn's algorithm, via BFS de graus de entrada).
    PROBLEMA: ordenar nós de um DAG tal que toda aresta u->v tem u antes de v.
    Usado em: dependências de tarefas, DP em DAG.
    Complexidade: O(V + E)
    Retorna: lista com a ordem, ou lista incompleta se houver ciclo
    (len(resultado) < n implica ciclo).
    """
    indeg = [0] * n
    for u in range(n):
        for v in graph[u]:
            indeg[v] += 1
    q = deque([u for u in range(n) if indeg[u] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order

def kruskal(n, edges):
    """
    Kruskal: Árvore Geradora Mínima (MST).
    PROBLEMA: conectar todos os n nós com o menor custo total possível.
    Complexidade: O(E log E)
    edges: lista de (peso, u, v)
    Retorna: (custo_total, lista_de_arestas_usadas)
    """
    edges = sorted(edges)  # ordena por peso
    dsu = DSU(n)
    total = 0
    used = []
    for w, u, v in edges:
        if dsu.union(u, v):
            total += w
            used.append((u, v, w))
    return total, used

def prim(graph, n, start=0):
    """
    Prim: Árvore Geradora Mínima (alternativa ao Kruskal).
    PROBLEMA: igual ao Kruskal, mas melhor quando o grafo é denso
    e já vem em lista de adjacência.
    Complexidade: O(E log V) com heap.
    graph[u] = [(v, peso), ...]
    Retorna: custo_total da MST (ou math.inf se grafo desconexo).
    """
    visited = [False] * n
    pq = [(0, start)]
    total = 0
    count = 0
    while pq and count < n:
        w, u = heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        total += w
        count += 1
        for v, wt in graph[u]:
            if not visited[v]:
                heappush(pq, (wt, v))
    return total if count == n else math.inf


class LCA:
    """
    Lowest Common Ancestor com Binary Lifting.
    PROBLEMA: numa árvore, dado dois nós, achar o ancestral comum mais
    próximo — usado para calcular distância entre nós, caminhos, etc.
    Complexidade: O(n log n) pré-processamento, O(log n) por query.
    Uso:
        lca = LCA(n, adj, root=0)
        lca.query(u, v)
    """
    def __init__(self, n, adj, root=0):
        self.n = n
        self.LOG = max(1, (n).bit_length())
        self.up = [[0] * n for _ in range(self.LOG)]
        self.depth = [0] * n
        self.visited = [False] * n
        self._bfs_init(adj, root)
        for k in range(1, self.LOG):
            for v in range(n):
                self.up[k][v] = self.up[k - 1][self.up[k - 1][v]]

    def _bfs_init(self, adj, root):
        q = deque([root])
        self.visited[root] = True
        self.up[0][root] = root
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not self.visited[v]:
                    self.visited[v] = True
                    self.depth[v] = self.depth[u] + 1
                    self.up[0][v] = u
                    q.append(v)

    def query(self, u, v):
        """Retorna o LCA de u e v."""
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        diff = self.depth[u] - self.depth[v]
        for k in range(self.LOG):
            if (diff >> k) & 1:
                u = self.up[k][u]
        if u == v:
            return u
        for k in range(self.LOG - 1, -1, -1):
            if self.up[k][u] != self.up[k][v]:
                u = self.up[k][u]
                v = self.up[k][v]
        return self.up[0][u]

def main():
    pass

if __name__ == "__main__":
    main()

