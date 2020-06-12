#!/usr/bin/env python3

import sympy as sym
import random


def quick_sort(array, cmp, *args):
    if len(array) == 0:
        return array
    else:
        pivot = random.choice(array)
        L, P, R = [], [], []
        for ele in array:
            val = cmp(ele, pivot, *args)
            if val == -1:
                L.append(ele)
            elif val == 0:
                P.append(ele)
            else:
                R.append(ele)
        return quick_sort(L, cmp, *args) + P + quick_sort(R, cmp, *args)


def bigO(f1, f2, var):
    limit = sym.limit(f1 / f2, var, sym.oo)
    if limit < sym.oo:
        if limit > 0:
            return 0
        else:
            return -1
    else:
        return 1


def main():
    n = sym.Symbol("n")
    funcs = {
        "n^3": n ** 3,
        "n / log^2n": n / sym.log(n, 2) ** 2,
        "nlogn": n * sym.log(n, 2),
        "1.1^n": 1.1 ** n,
        "1 / n^3": 1 / n ** 3,
        "log^6n": sym.log(n, 2) ** 6,
        "1 / n": 1 / n,
        "2^logn": 2 ** sym.log(n, 2),
        "n!": sym.factorial(n),
        "n^loglogn": n ** (sym.log(sym.log(n, 2), 2)),
        "2^sqrt(logn)": 2 ** (sym.log(n, 2) ** 0.5),
        "n^(1 / logn)": n ** (1 / sym.log(n)),
    }
    func_labels = [key for key in funcs]
    print(quick_sort(func_labels, lambda p, q: bigO(funcs[p], funcs[q], n)))


if __name__ == "__main__":
    main()
