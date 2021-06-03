def pointNotInCanvas(canvas, i, j):

    width = len(canvas[0]) - 2
    height = len(canvas)
    if (j < 0 or j > width) or (i < 0 or i > height - 1):
        return True
    return False
