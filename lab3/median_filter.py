import numpy as np


def median_filter_sparse_cross(img):

    mask = np.array([
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0]
    ], dtype=np.uint8)


    rows, cols = np.where(mask == 1)
    offsets = list(zip(rows - 2, cols - 2))


    result = np.zeros_like(img)


    for y in range(2, img.shape[0] - 2):
        for x in range(2, img.shape[1] - 2):

            values = [img[y + dy, x + dx] for dy, dx in offsets]

            result[y, x] = np.median(values)

    return result


if __name__ == '__main__':
    pass