import numpy as np
import shapes

def test_cube_corners():
    corners = shapes.get_cube_corners()
    assert (len(set([tuple(c) for c in corners])) == 8)

    for corner in corners:
        assert (np.isclose(np.linalg.norm(corner), 1))


def test_icosahedron_corners():
    corners = shapes.get_icosahedron_corners()
    assert (len(set([tuple(c) for c in corners])) == 12)

    for corner in corners:
        assert (np.isclose(np.linalg.norm(corner), 1))


def test_dodecahedron_corners():
    corners = shapes.get_dodecahedron_corners()
    assert (len(set([tuple(c) for c in corners])) == 20)

    for corner in corners:
        assert (np.isclose(np.linalg.norm(corner), 1))


def test_tetrahedron():
    corners = shapes.get_tetrahedron_corners()
    for corner in corners:
        assert (np.isclose(shapes.tetrahedron(*corner), 0))
        assert (np.isclose(shapes.tetrahedron.diff(*corner), [0, 0, 0]).all())

    while True:
        xyz = np.random.rand(3)
        for corner in corners:
            if np.isclose(xyz, corner).all():
                break
        else:
            break

    assert (not np.isclose(shapes.tetrahedron(*xyz), 0))
