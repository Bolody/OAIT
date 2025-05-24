from my_io import *
from contour import krun_operator
from my_io import Image
import os

operations = {
    'Градиентная матрица G_x': 'x',
    'Градиентная матрица G_y': 'y',
    'Градиентная матрица G': 'g',
    'Бинаризованная градиентная матрица G_b': 'b',
}

images = {
    'Cartoon': '1.png',
    'car': '2.png',
    'Flower': '3.png',
    'women': '4.png',
    'sky_water': '5.png',
    'Text': '6.png',
    'Map': '7.png',
    'Rentgen': '8.png'
}

if __name__ == '__main__':
    print('Выберите изображение:')
    selected_image = prompt(images)
    img = image_to_np_array(selected_image)

    print('Выберите вид обработки:')
    op = prompt(operations)

    result = Image.fromarray(krun_operator(img, op), 'L')
    print('Введите название сохраненного изображения (оставьте пустым, чтобы не сохранять)')

    selected_path = input()
    if selected_path:
        # Добавляем расширение .png, если оно отсутствует
        if not selected_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            selected_path += '.png'  # По умолчанию сохраняем в формате PNG

        # Создаем директорию, если она не существует
        os.makedirs('pictures_results', exist_ok=True)

        # Сохраняем изображение
        result.save(os.path.join('pictures_results', selected_path))
        print(f'Изображение сохранено как {selected_path} в папке pictures_results')
    else:
        print('Изображение не сохранено.')