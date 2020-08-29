class QuadraticRootPolynomial(object):
    def __init__(self, roots):
        self.roots = roots

    def __call__(self, *params):
        result = 1
        for root in self.roots:
            partial = 0
            for param, component in zip(params, root):
                partial += (param - component)**2
            result *= partial
        return result

    def diff(self, *params):
        result = [0] * len(params)
        for i, root in enumerate(self.roots):
            root = self.roots[i]
            partial = [2*(p - c) for p, c in zip(params, root)]
            for j, other_root in enumerate(self.roots):
                if i == j:
                    continue
                sub_coef = 0
                for param, component in zip(params, other_root):
                    sub_coef += (param - component)**2
                for k in range(len(partial)):
                    partial[k] *= sub_coef
            for k in range(len(result)):
                result[k] += partial[k]
        return result
