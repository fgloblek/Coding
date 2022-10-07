import sys


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, C = map(int, sys.stdin.readline().split(" "))
        distlist = []
        for _ in range(N):
            distlist.append(int(sys.stdin.readline()))
        distlist.sort()
        difflist = [distlist[i + 1] - distlist[i] for i in range(N - 1)]
        print(distlist)
        print(difflist)


if __name__ == "__main__":
    main()
