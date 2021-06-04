def pointNotInCanvas(canvas, i, j):

    width = len(canvas[0]) - 2
    height = len(canvas)
    if (j < 0 or j > width) or (i < 0 or i > height - 1):
        return True
    return False


def get_adjacents(i, j, matrix):
    """given a matrix and a couple of indices finds indexes of points
    adjacent to given input

    Args:
        i ([int]): [index of row]
        j ([int]): [index of column]
        matrix ([numpy array]): [matrix of measurements]

    Returns:
        [list]: [list of adjacent indexes]
    """
    m = matrix.shape[0]
    n = matrix.shape[1]
    adjacent_indexes = []
    if i > m or j > n or i < 0 or j < 0:
        return adjacent_indexes
    if i > 0:
        adjacent_indexes.append((i - 1, j))

    if i + 1 < m:
        adjacent_indexes.append((i + 1, j))

    if j > 0:
        adjacent_indexes.append((i, j - 1))

    if j + 1 < n:
        adjacent_indexes.append((i, j + 1))
    return adjacent_indexes
