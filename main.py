def read_matrix(filename="udg.dat"):
    matrix = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            row = list(map(int, line.split()))
            matrix.append(row)
    return matrix


def prim_mst(adj):
    n = len(adj)

    in_mst = [False] * n
    key = [10**18] * n
    parent = [-1] * n

    key[0] = 0

    for _ in range(n):
        u = -1
        best = 10**18
        for v in range(n):
            if not in_mst[v] and key[v] < best:
                best = key[v]
                u = v

        in_mst[u] = True

        for v in range(n):
            w = adj[u][v]
            if not in_mst[v] and w != 0 and w < key[v]:
                key[v] = w
                parent[v] = u

    total_weight = sum(key)
    return total_weight, parent


def build_mst_matrix(adj, parent):
    n = len(adj)
    mst = [[0] * n for _ in range(n)]

    for v in range(1, n):
        u = parent[v]
        w = adj[u][v]
        mst[u][v] = w
        mst[v][u] = w

    return mst


def write_matrix(matrix, filename="mst.dat"):
    with open(filename, "w") as f:
        for row in matrix:
            f.write(" ".join(map(str, row)) + "\n")


if __name__ == "__main__":
    graph = read_matrix("udg.dat")

    total, parent = prim_mst(graph)
    mst_matrix = build_mst_matrix(graph, parent)

    print(total)
    write_matrix(mst_matrix, "mst.dat")

   