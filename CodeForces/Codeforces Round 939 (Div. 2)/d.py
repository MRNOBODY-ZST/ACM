L = print
I = range
from sys import stdin

input = lambda: stdin.readline().rstrip("\r\n")
D = int(input())
K = list(map(int, input().split()))
J = 0, 0
for C in I(1 << D):
    H = 0
    for B in I(D):
        if C >> B & 1:
            H += K[B]
    A = 0
    for B in I(D):
        if C >> B & 1:
            H += A * A
            A = 0
        else:
            A += 1
    H += A * A
    J = max(J, (H, C))
M, C = J
C |= 1 << D
E = A = 0
F = []
G = []
for B in I(D):
    if C >> B & 1:
        E = B + 1
        A = 0
        G.clear()
    else:
        if A > 1:
            G += G[: (1 << A - 1) - 1]
        G += [(E + 1, E + A + 1)]
        if K[B] != A:
            F += [(E + 1, B + 1)]
            F += G[:-1]
        if C >> B + 1 & 1:
            F += [(E + 1, B + 1)]
        A += 1
L(M, len(F))
for N in F:
    L(*N)
