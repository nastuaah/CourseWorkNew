import os
import django
import sys
from django.core.files import File
from transliterate import translit
from PIL import Image  # Импортируем библиотеку для работы с изображениями

sys.path.append(r"C:\Users\Настя\PycharmProjects\CourseWorkNew\coursework")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coursework.settings")
django.setup()

from myApp.models import Product

IMAGE_DIR = r"C:\Users\Настя\PycharmProjects\CourseWorkNew\coursework\myApp\media"


TARGET_SIZE = (800, 1000)

if not os.path.exists(IMAGE_DIR):
    print(f"Директория {IMAGE_DIR} не существует!")
    exit(1)

product_names = [
    "Бирки", "Буклеты", "Журналы", "Календари", "Книги", "Визитки",
    "Листовки", "Меню", "Открытки", "Пакеты", "Плакаты", "Пригласительные",
    "Сертификаты", "Стикеры", "Тейбл-тенты", "Баннеры"
]

for name in product_names:

    translit_name = translit(name, "ru", reversed=True).lower().replace("'", "")
    image_filename = f"{translit_name}.jpg"
    image_path = os.path.join(IMAGE_DIR, image_filename)

    print(f"Ищем файл: {image_path}")

    if not os.path.exists(image_path):
        print(f"Файл {image_path} не найден, пропускаем...")
        continue

    with Image.open(image_path) as img:
        img = img.resize(TARGET_SIZE, Image.Resampling.LANCZOS)

        temp_image_path = os.path.join(IMAGE_DIR, f"temp_{image_filename}")
        img.save(temp_image_path, "JPEG")

        with open(temp_image_path, "rb") as img_file:
            product, created = Product.objects.get_or_create(name=name)
            product.image.save(image_filename, File(img_file), save=True)

        os.remove(temp_image_path)

        if created:
            print(f"Добавлено: {name}")
        else:
            print(f"Обновлено: {name}")

print("Готово!")