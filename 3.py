import requests

def save_satellite_image(coordinates, zoom_level=16, output_filename="satellite_image.png"):
    base_url = "https://static-maps.yandex.ru/1.x/"
    params = {
        "ll": f"{coordinates[1]},{coordinates[0]}",
        "z": zoom_level,
        "l": "sat",
        "size": "600,400"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        with open(output_filename, "wb") as file:
            file.write(response.content)
        print(f"Снимок сохранён в файл {output_filename}")
    else:
        print(f"Не удалось получить снимок: {response.status_code}")
        print("Ответ сервера:", response.text)

if __name__ == "__main__":
    try:
        latitude = float(input("Введите широту объекта: "))
        longitude = float(input("Введите долготу объекта: "))
        save_satellite_image([latitude, longitude])
    except ValueError:
        print("Ошибка ввода! Введите координаты в виде десятичных чисел.")

# Пример использования
# save_satellite_image([55.7558, 37.6173])
