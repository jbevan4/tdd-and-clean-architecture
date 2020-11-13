class Room:

    def __init__(self, code, size, price, longitude, latitude):
        self.code = code
        self.size = size
        self.price = price
        self.longitude = longitude
        self.latitude = latitude

    @classmethod
    def from_dict(cls, room_dict):
        return cls(
            code=room_dict['code'],
            size=room_dict['size'],
            price=room_dict['price'],
            latitude=room_dict['latitude'],
            longitude=room_dict['longitude'],
        )

    def to_dict(self):
        return {
            "code": self.code,
            "size": self.size,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()
