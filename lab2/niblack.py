import numpy as np
from PIL import Image
from integral import integral_image
from semitone import image_to_np_array
from semitone import semitone


def niblack_threshold(img: np.ndarray, window_size: int = 7, k: float = -0.2) -> np.ndarray:
    """
    Адаптивная бинаризация методом Эйквила

    :param img: Полутоновое изображение в виде массива NumPy.
    :param window_size: Размер окна (по умолчанию 7x7).
    :param k: Параметр, регулирующий чувствительность порога (по умолчанию -0.2).
    :return: Бинаризованное изображение.
    """
    if window_size % 2 == 0:
        raise ValueError("Размер окна должен быть нечетным!")

    half_win = window_size // 2
    img = img.astype(np.float64)

    # Вычисляем интегральные изображения
    int_img = integral_image(img)
    int_img_sq = integral_image(img ** 2)

    rows, cols = img.shape
    binarized = np.zeros_like(img, dtype=np.uint8)

    for y in range(rows):
        for x in range(cols):
            # Определяем границы окна
            y1, y2 = max(0, y - half_win), min(rows - 1, y + half_win)
            x1, x2 = max(0, x - half_win), min(cols - 1, x + half_win)

            # Вычисляем площадь окна
            area = (y2 - y1 + 1) * (x2 - x1 + 1)

            # Сумма пикселей и сумма квадратов пикселей в окне
            sum_pixels = int_img[y2, x2]
            sum_sq_pixels = int_img_sq[y2, x2]

            if x1 > 0:
                sum_pixels -= int_img[y2, x1 - 1]
                sum_sq_pixels -= int_img_sq[y2, x1 - 1]

            if y1 > 0:
                sum_pixels -= int_img[y1 - 1, x2]
                sum_sq_pixels -= int_img_sq[y1 - 1, x2]

            if x1 > 0 and y1 > 0:
                sum_pixels += int_img[y1 - 1, x1 - 1]
                sum_sq_pixels += int_img_sq[y1 - 1, x1 - 1]

            # Вычисляем среднее и стандартное отклонение
            mean = sum_pixels / area
            std_dev = np.sqrt((sum_sq_pixels / area) - (mean ** 2))

            # Формула Эйквила (Niblack)
            threshold = mean + k * std_dev

            # Бинаризация
            binarized[y, x] = 255 if img[y, x] > threshold else 0

    return binarized


if __name__ == '__main__':
    # Загрузка изображения
    img = image_to_np_array("test.png")
    img_gray = semitone(img)

    # Бинаризация методом Эйквила
    bin_img = niblack_threshold(img_gray, window_size=7, k=-0.2)

    # Сохранение и отображение результата
    result = Image.fromarray(bin_img, "L")
    result.show()
    result.save('pictures_results/test_binarized_niblack.png')