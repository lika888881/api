import folium

# Определяем координаты точек пути
route_coordinates = [
    [55.751244, 37.618423],
    [55.715551, 37.554191],
    [55.791540, 37.559809]
]

# Создаем карту с начальной позицией
map_view = folium.Map(location=route_coordinates[0], zoom_start=11)

# Добавляем линии между точками пути
for index in range(len(route_coordinates) - 1):
    folium.PolyLine([route_coordinates[index], route_coordinates[index + 1]], color="blue", weight=2.5).add_to(map_view)

# Находим среднюю точку пути
mid_index = len(route_coordinates) // 2
average_point = route_coordinates[mid_index]

# Добавляем маркер на среднюю точку
folium.Marker(location=average_point, popup="Средняя точка пути").add_to(map_view)

# Сохраняем карту в файл
map_view.save("Map.html")

print("Откройте файл Map.html")
