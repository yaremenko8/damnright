import z3

class UncertainPolynomial:
    def __init__(self, head, *tail, own_alphabet=None):
        self.head = head
        self.tail = tail
        if own_alphabet is None:
            self.own_alphabet = []
        assert str(head.sort()) == 'Real'
        for constraint in tail:
            assert str(constraint.sort()) == 'Bool'
            assert str(constraint.arg(0).sort()) == 'Real'
            assert str(constraint.arg(1).sort()) == 'Real'
            assert str(constraint.decl()) in ["<", ">", "<=", ">="]

    def _common_alphabet(self, other):
        pass

    def __mul__(self, other):
        if type(other) is type(z3.Real('x')):
            assert str(other.sort()) == 'Real'
            return self * UncertainPolynomial(other)
        elif type(other) in [int, float]:
            return self * z3.RealVal(other)
        pass

    def __mul__(self, other):
        if type(other) is type(z3.Real('x')):
            assert str(other.sort()) == 'Real'
            return self * UncertainPolynomial(other)
        elif type(other) in [int, float]:
            return self * z3.RealVal(other)
        pass

    def __pow__(self, pwr):
        assert type(pwr) is int
        return UncertainPolynomial(self.head ** pwr,
                                   *self.tail,
                                   own_alphabet=self.own_alphabet)


    def __call__(self, **variables):
        for variable in variables:
            pass


a = UncertainPolynomial(z3.Real('x'), z3.Real('x') < 3)


print(a.head)