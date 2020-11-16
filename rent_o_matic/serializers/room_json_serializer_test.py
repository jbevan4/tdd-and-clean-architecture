import json
import uuid
from serializers.room_json_serializer import RoomJsonEncoder
from domain.room import Room


def test_serialize_domain_room():
    code = uuid.uuid4()
    room = Room(
        code=code,
        size=200,
        price=10,
        longitude=-0.09998975,
        latitude=51.75436293
    )
    expected_json = """
  {{
  "code": "{}",
  "size": 200,
  "price": 10,
  "longitude": -0.09998975,
  "latitude": 51.75436293
  }}
  """.format(code)
    json_room = json.dumps(room, cls=RoomJsonEncoder)
    assert json.loads(json_room) == json.loads(expected_json)
