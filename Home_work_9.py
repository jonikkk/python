import json


class JsonParser:
    def __init__(self, user_string):
        self.user_string = user_string

    def __enter__(self):
        self.text = json.loads(self.user_string)
        return self.text

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, point1, point2):
        self.x1, self.y1 = point1.x, point1.y
        self.x2, self.y2 = point2.x, point2.y

    def contains(self, point):
        x, y = point.x, point.y
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2

    def __contains__(self, point):
        return self.contains(point)


if __name__ == '__main__':
    with JsonParser('"hello"') as res:
        assert res == "hello"

    with JsonParser('{"hello": "world", "key": [1,2,3]}') as res:
        assert res == {"hello": "world", "key": [1, 2, 3]}

    start_point = Point(1, 0)
    end_point = Point(7, 3)

    rect = Rectangle(start_point, end_point)
    assert rect.contains(start_point)
    assert not rect.contains(Point(-1, 3))
    assert start_point in rect
    assert Point(-1, 3) not in rect
