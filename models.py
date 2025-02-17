from datetime import datetime


class Hotel:
    def __init__(self, hotel_id: str, name: str, location: str,
                 total_rooms: int):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.total_rooms = total_rooms
        self.available_rooms = total_rooms

    def to_dict(self):
        return {
            'hotel_id': self.hotel_id,
            'name': self.name,
            'location': self.location,
            'total_rooms': self.total_rooms,
            'available_rooms': self.available_rooms
        }

    @classmethod
    def from_dict(cls, data):
        hotel = cls(
            data['hotel_id'],
            data['name'],
            data['location'],
            data['total_rooms']
        )
        hotel.available_rooms = data['available_rooms']
        return hotel


class Customer:
    def __init__(self, customer_id: str, name: str, email: str, phone: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['customer_id'],
            data['name'],
            data['email'],
            data['phone']
        )


class Reservation:
    def __init__(self, reservation_id: str, hotel_id: str, customer_id: str,
                 check_in: datetime, check_out: datetime, num_rooms: int):
        self.reservation_id = reservation_id
        self.hotel_id = hotel_id
        self.customer_id = customer_id
        self.check_in = check_in
        self.check_out = check_out
        self.num_rooms = num_rooms
        self.status = "active"

    def to_dict(self):
        return {
            'reservation_id': self.reservation_id,
            'hotel_id': self.hotel_id,
            'customer_id': self.customer_id,
            'check_in': self.check_in.isoformat(),
            'check_out': self.check_out.isoformat(),
            'num_rooms': self.num_rooms,
            'status': self.status
        }

    @classmethod
    def from_dict(cls, data):
        reservation = cls(
            data['reservation_id'],
            data['hotel_id'],
            data['customer_id'],
            datetime.fromisoformat(data['check_in']),
            datetime.fromisoformat(data['check_out']),
            data['num_rooms']
        )
        reservation.status = data['status']
        return reservation
