import sys


def invmerge(A):
    if len(A) == 1:
        return A, 0
    mid = len(A) // 2
    L, invL = invmerge(A[:mid])
    R, invR = invmerge(A[mid:])
    sortA = []
    inv = invL + invR
    i, j = 0, 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            sortA.append(L[i])
            i += 1
        else:
            sortA.append(R[j])
            j += 1
            inv += len(L) - i
    sortA += L[i:]
    sortA += R[j:]
    return sortA, inv


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        _ = int(sys.stdin.readline())
        a = sys.stdin.readline().strip().split(" ")
        b = sys.stdin.readline().strip().split(" ")
        gooddict = {a: i for i, a in enumerate(a)}
        bnums = [gooddict[word] for word in b]
        print(invmerge(bnums)[1])


if __name__ == "__main__":
    main()
