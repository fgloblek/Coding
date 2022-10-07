import sys


def continuous_binary_search(f, lo, hi, gap=1e-4):
    while hi - lo > gap:
        mid = (hi + lo) / 2.0
        if f(mid):
            hi = mid
        else:
            lo = mid
    return lo


# using global variables inside funtion, don't care lol
#
def volume(level, params):
    vol = 0
    for plist in params:
        if level < plist[0]:
            continue
        elif level >= plist[0] + plist[1]:
            vol += plist[1] * plist[2] * plist[3]
        else:
            vol += (level - plist[0]) * plist[2] * plist[3]
    return vol


def main():
    k = int(sys.stdin.readline())
    for _ in range(k):
        n = int(sys.stdin.readline())
        params = []
        hi = 0
        avail = 0
        for _ in range(n):
            b, h, w, d = map(int, sys.stdin.readline().split())
            avail += h * w * d
            hi = max(hi, b + h)
            params.append([b, h, w, d])
        V = int(sys.stdin.readline())
        if V <= avail:
            level = continuous_binary_search(
                lambda level: volume(level, params) >= V, 0, hi
            )
            print(round(level, 3))
        else:
            print("OVERFLOW")


if __name__ == "__main__":
    main()
