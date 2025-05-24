import numpy as np
from PIL import Image
import cv2
import os


def image_to_np_array(image_name: str) -> np.array:
    full_path = os.path.join('pictures_src', image_name)
    print(f"Пытаемся открыть изображение: {full_path}")
    img_src = Image.open(full_path).convert('RGB')
    return np.array(img_src)


def convert_to_grayscale(image_array: np.array) -> np.array:
    gray_image = np.dot(image_array[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
    return gray_image


def adaptive_threshold(gray_image: np.array) -> np.array:
    binary_image = cv2.adaptiveThreshold(gray_image, 255,
                                         cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY, 7, 5)
    return binary_image


if __name__ == "__main__":
    # Путь к изображению
    input_image_name = r"C:\Users\huawei\Desktop\ОАВИ\lab2\pictures_src\rentgen.png"
  # Измените на полный путь, если нужно
    output_gray_image_name = 'output_gray.bmp'
    output_binary_image_name = 'output_binary1.bmp'

    # Проверка наличия директории
    base_dir = r"C:\Users\huawei\Desktop\ОАВИ\lab2"
    input_image_path = os.path.join(base_dir, 'pictures_src', input_image_name)

    # Загрузка изображения и преобразование в массив NumPy
    try:
        image_array = image_to_np_array(input_image_name)
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        exit()

    # Приведение к полутоновому
    gray_image = convert_to_grayscale(image_array)

    # Сохранение полутонового изображения
    gray_image_pil = Image.fromarray(gray_image)
    try:
        gray_image_pil.save(os.path.join(base_dir, 'pictures_src', output_gray_image_name))
        print(
            f"Полутоновое изображение сохранено по пути: {os.path.join(base_dir, 'pictures_src', output_gray_image_name)}")
    except Exception as e:
        print(f"Ошибка при сохранении полутонового изображения: {e}")

    # Приведение к монохромному методом пороговой обработки
    binary_image = adaptive_threshold(gray_image)

    # Сохранение монохромного изображения
    binary_image_pil = Image.fromarray(binary_image)
    try:
        binary_image_pil.save(os.path.join(base_dir, 'pictures_src', output_binary_image_name))
        print(
            f"Монохромное изображение сохранено по пути: {os.path.join(base_dir, 'pictures_src', output_binary_image_name)}")
    except Exception as e:
        print(f"Ошибка при сохранении монохромного изображения: {e}")
