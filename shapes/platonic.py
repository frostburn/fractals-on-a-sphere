import numpy as np

def get_tetrahedron_corners():
    """
    Return coordinates of the corners of a regular tetrahedron that lie on the unit sphere.
    """
    return np.array([
            [1, 1, 1],
            [1, -1, -1],
            [-1, 1, -1],
            [-1, -1, 1],
        ]) / np.sqrt(3)


def get_octahedron_corners():
    return np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [-1, 0, 0],
            [0, -1, 0],
            [0, 0, -1],
        ])


def get_cube_corners():
    c = get_tetrahedron_corners()
    return np.concatenate([c, -c])


def get_icosahedron_corners():
    phi = 0.5 * (1 + np.sqrt(5))
    corners = []
    for s1 in [-1, 1]:
        for s2 in [-phi, phi]:
            corner = [0, s1, s2]
            for _ in range(3):
                corners.append(corner[:])
                corner = [corner[2], corner[0], corner[1]]
    return np.array(corners) / np.sqrt(2 + phi)


def get_dodecahedron_corners():
    phi = 0.5 * (1 + np.sqrt(5))
    corners = []
    for s1 in [-1, 1]:
        for s2 in [-1, 1]:
            for s3 in [-1, 1]:
                corner = [s1, s2, s3]
                corners.append(corner)
            corners.append([0, s1*phi, s2/phi])
            corners.append([s2/phi, 0, s1*phi])
            corners.append([s1*phi, s2/phi, 0])
    return corners / np.sqrt(3)
