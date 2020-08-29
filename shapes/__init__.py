from .platonic import *
from .polynomial import *

tetrahedron = QuadraticRootPolynomial(get_tetrahedron_corners())
octahedron = QuadraticRootPolynomial(get_octahedron_corners())
cube = QuadraticRootPolynomial(get_cube_corners())
icosahedron = QuadraticRootPolynomial(get_icosahedron_corners())
dodecahedron = QuadraticRootPolynomial(get_dodecahedron_corners())
