import sys
import os

# Добавляем текущую директорию в sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from median_filter import median_filter_sparse_cross
from difference import difference_image
from my_io import prompt, image_to_np_array, path, Image

images = {
    'game': 'game_bin.png',
    'Tiger': 'tiger_bin.png',
    'Fingerprint': 'fingerprint_semitone.png',
    'Man': 'man_bin.png',
    'Photo': 'photo_semitone.png',
    'Text': 'text_bin.png',
    'Xray': 'xray_semitone.png'
}

if __name__ == '__main__':
    print('Выберите изображение:')
    selected_image = prompt(images)
    img = image_to_np_array(selected_image)

    res_img = median_filter_sparse_cross(img)  # Применяем медианный фильтр
    difference = difference_image(img, res_img)

    res_img = Image.fromarray(res_img, 'L')
    difference = Image.fromarray(difference, 'L')

    difference.save(path.join('differential_pictures', selected_image))
    print('Введите название сохраненного изображения (оставьте пустым, чтобы не сохранять)')
    selected_path = input()
    if selected_path:
        res_img.save(path.join('pictures_results', selected_path))