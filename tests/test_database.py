"""
Тестирование базы данных данных
"""
import map_game.loader
import map_game.database



def test_parser():
    FILENAME = 'map.xml'
    result = map_game.loader._load(FILENAME)
    parsed = map_game.loader.parser(result)
    db = map_game.database.DataBase()
    packed = db._pack(parsed)
    assert 'Node' in packed
    assert 'Way' in packed
    assert 'House' in packed
    assert 'Area' in packed
