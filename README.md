# map_game
Игра "Защитник города"

## Введение

Игра стрелялка на основе реальной карты города.
Карта города загружается с сайта osm.org

## Используемые технологии

* XML
* pygame

## Формат базы данных

База данных - это словарь
С основными ключами

* way
* house
* area

Значение для каждого ключа - это список объектов

### Объект Road
 
* id
* points
* width
* color

### House и Area

* id
* points
* color
* can_cross