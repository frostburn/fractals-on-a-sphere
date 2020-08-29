import numpy as np

EPSILON = 1e-10

class NewtonsMethod(object):
    def __init__(self, func, num_iterations, relaxation=1.0, projection=False, bias=False, cyclic=False, S2=True):
        self.func = func
        self.num_iterations = num_iterations
        self.relaxation = relaxation

        self.projection = projection
        self.bias = bias
        self.cyclic = cyclic
        self.S2 = S2

    def __call__(self, *params):
        result = params

        for _ in range(self.num_iterations):
            value = self.func(*result)
            gradient = self.func.diff(*result)

            if self.cyclic:
                gradient = gradient[-1:] + gradient[:-1]

            if self.projection:
                normal = 0
                for x, dx in zip(result, gradient):
                    normal += x*dx
                gradient = [dx - normal*x for x, dx in zip(result, gradient)]

            if self.bias:
                amount = self.relaxation * value
                result = [x - amount / (dx + (abs(dx) < EPSILON)) for x, dx in zip(result, gradient)]
            else:
                gradient_norm = 0
                for component in gradient:
                    gradient_norm += component**2

                amount = self.relaxation * value / (gradient_norm + (abs(gradient_norm) < EPSILON))
                result = [x - amount * dx for x, dx in zip(result, gradient)]

            if self.S2:
                result_norm = 0
                for component in result:
                    result_norm += component**2
                result_norm **= -0.5
                result = [x * result_norm for x in result]

        return result
