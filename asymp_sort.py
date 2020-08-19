#!/usr/bin/env python3

import random

import sympy as sym


class AsympFunc:
    def __init__(self, func, var, name=None, string_rep=None):
        self.func = func
        self.var = var
        self.name = name
        self.string_rep = string_rep
        self.cache = {}

    def limit(self, other):
        if other not in self.cache:
            self.cache[other] = sym.limit(self.func / other.func, self.var, sym.oo)
        return self.cache[other]

    def __lt__(self, other):
        return self.limit(other) == 0

    def __repr__(self):
        if not self.string_rep:
            return str(self.func)
        else:
            return self.string_rep


def main():
    n = sym.Symbol("n")
    funcs = [
        AsympFunc(n ** 3, n, string_rep="n^3"),
        AsympFunc(n / sym.log(n, 2) ** 2, n, string_rep="n / log^2n"),
        AsympFunc(n * sym.log(n, 2), n, string_rep="nlogn"),
        AsympFunc(1.1 ** n, n, string_rep="1.1^n"),
        AsympFunc(1 / n ** 3, n, string_rep="1 / n^3"),
        AsympFunc(sym.log(n, 2) ** 6, n, string_rep="log^6n"),
        AsympFunc(1 / n, n, string_rep="1 / n"),
        AsympFunc(2 ** sym.log(n, 2), n, string_rep="2^logn"),
        AsympFunc(sym.factorial(n), n, string_rep="n!"),
        AsympFunc(n ** (sym.log(sym.log(n, 2), 2)), n, string_rep="n^loglogn"),
        AsympFunc(2 ** (sym.log(n, 2) ** 0.5), n, string_rep="2^sqrt(logn)"),
        AsympFunc(n ** (1 / sym.log(n)), n, string_rep="n^(1 / logn)"),
    ]
    print(sorted(funcs))


if __name__ == "__main__":
    main()
