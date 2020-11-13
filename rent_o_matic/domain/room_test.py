import uuid

from .room import Room


def test_room_model_init():
    code = uuid.uuid4()
    room = Room(code, size=200, price=10,
                longitude=-0.09998975,
                latitude=51.75436293)
    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.09998975
    assert room.latitude == 51.75436293


def test_create_room_from_dict():
    code = uuid.uuid4()
    room = Room.from_dict(
        {
            'code': code,
            'size': 200,
            'price': 10,
            'longitude': -0.09998975,
            'latitude': 51.75436293
        }
    )

    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.09998975
    assert room.latitude == 51.75436293


def test_room_model_to_dict():
    room_dict = {
        'code': uuid.uuid4(),
        'size': 200,
        'price': 10,
        'longitude': -0.09998975,
        'latitude': 51.75436293
    }
    room = Room.from_dict(room_dict)
    assert room.to_dict() == room_dict


def test_room_model_comparison():
    room_dict = {
        'code': uuid.uuid4(),
        'size': 200,
        'price': 10,
        'longitude': -0.09998975,
        'latitude': 51.75436293
    }
    room1 = Room.from_dict(room_dict)
    room2 = Room.from_dict(room_dict)
    assert room1 == room2
