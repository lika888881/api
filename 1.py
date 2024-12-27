import requests  
  
def display_stadiums_map():  
    # Определяем координаты стадионов  
    stadium_coordinates = {  
        "Лужники": "37.554191,55.715551",  
        "Спартак": "37.440262,55.818015",  
        "Динамо": "37.559809,55.791540"  
    }  
  
    # Формируем метки для карты  
    map_markers = "~".join([f"{coords},pm2rdm" for coords in stadium_coordinates.values()])  
  
    # Создаем URL для запроса  
    static_map_url = "https://static-maps.yandex.ru/1.x/"  
    request_params = {  
        "l": "map",  
        "size": "600,400",  
        "pt": map_markers  
    }  
  
    # Отправляем запрос  
    response = requests.get(static_map_url, params=request_params)  
  
    # Обрабатываем ответ  
    if response.status_code == 200:  
        with open("stadiums_map.html", "w") as output_file:  
            html_content = f"""  
            <html>  
                <body>  
                    <h3>Карта с метками стадионов</h3>  
                    <img src="{response.url}" alt="Карта с метками">  
                </body>  
            </html>  
            """  
            output_file.write(html_content)  
        print("Карта сохранена в файле 'stadiums_map.html'")  
    else:  
        print("Ошибка при загрузке карты.")  
  
# Вызов функции  
display_stadiums_map()
