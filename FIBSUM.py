# your code goes here
import sys


def fib(n: int) -> int:
    mem = [0, 1]
    for i in range(2, n + 1):
        mem[i % 2] = mem[0] + mem[1]
    return mem[n % 2]


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n, m = map(int, sys.stdin.readline().split())
        print(sum(fib(k) % 1000000007 for k in range(n, m + 1)) % 1000000007)


if __name__ == "__main__":
    main()
