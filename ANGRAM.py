import sys


def anagram(phrase1, phrase2) -> bool:
    if "".join(sorted(phrase1)) == "".join(sorted(phrase2)):
        return "true"
    return "false"


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        phrase1, phrase2 = sys.stdin.readline().split()
        print(anagram(phrase1, phrase2))


if __name__ == "__main__":
    main()
