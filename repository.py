import json
import os
from models import Hotel, Customer, Reservation


class FileRepository:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir
        self._ensure_data_directory()

    def _ensure_data_directory(self):
        """Ensure the data directory exists"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def _save_to_file(self, filename: str, data: list):
        """Save data to a JSON file"""
        filepath = os.path.join(self.data_dir, filename)
        try:
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            raise Exception(
                f"Error saving to {filename}: {str(e)}"
            )

    def _load_from_file(self, filename: str) -> list:
        """Load data from a JSON file"""
        filepath = os.path.join(self.data_dir, filename)
        try:
            if not os.path.exists(filepath):
                return []
            with open(filepath, 'r') as f:
                return json.load(f)
        except Exception as e:
            raise Exception(
                f"Error loading from {filename}: {str(e)}"
            )


class HotelRepository(FileRepository):
    def __init__(self, data_dir: str):
        super().__init__(data_dir)
        self.filename = "hotels.json"

    def save_hotel(self, hotel: Hotel):
        """Save a new hotel or update existing one"""
        hotels = self._load_from_file(self.filename)
        hotel_dict = hotel.to_dict()

        # Update existing or add new
        updated = False
        for i, h in enumerate(hotels):
            if h['hotel_id'] == hotel.hotel_id:
                hotels[i] = hotel_dict
                updated = True
                break

        if not updated:
            hotels.append(hotel_dict)

        self._save_to_file(self.filename, hotels)

    def get_hotel(self, hotel_id: str) -> Hotel:
        """Get a hotel by ID"""
        hotels = self._load_from_file(self.filename)
        for hotel_data in hotels:
            if hotel_data['hotel_id'] == hotel_id:
                return Hotel.from_dict(hotel_data)
        return None

    def delete_hotel(self, hotel_id: str):
        """Delete a hotel by ID"""
        hotels = self._load_from_file(self.filename)
        hotels = [h for h in hotels if h['hotel_id'] != hotel_id]
        self._save_to_file(self.filename, hotels)

    def get_all_hotels(self) -> list:
        """Get all hotels"""
        hotels = self._load_from_file(self.filename)
        return [Hotel.from_dict(h) for h in hotels]


class CustomerRepository(FileRepository):
    def __init__(self, data_dir: str):
        super().__init__(data_dir)
        self.filename = "customers.json"

    def save_customer(self, customer: Customer):
        """Save a new customer or update existing one"""
        customers = self._load_from_file(self.filename)
        customer_dict = customer.to_dict()

        # Update existing or add new
        updated = False
        for i, c in enumerate(customers):
            if c['customer_id'] == customer.customer_id:
                customers[i] = customer_dict
                updated = True
                break

        if not updated:
            customers.append(customer_dict)

        self._save_to_file(self.filename, customers)

    def get_customer(self, customer_id: str) -> Customer:
        """Get a customer by ID"""
        customers = self._load_from_file(self.filename)
        for customer_data in customers:
            if customer_data['customer_id'] == customer_id:
                return Customer.from_dict(customer_data)
        return None

    def delete_customer(self, customer_id: str):
        """Delete a customer by ID"""
        customers = self._load_from_file(self.filename)
        customers = [c for c in customers if c['customer_id'] != customer_id]
        self._save_to_file(self.filename, customers)

    def get_all_customers(self) -> list:
        """Get all customers"""
        customers = self._load_from_file(self.filename)
        return [Customer.from_dict(c) for c in customers]


class ReservationRepository(FileRepository):
    def __init__(self, data_dir: str):
        super().__init__(data_dir)
        self.filename = "reservations.json"

    def save_reservation(self, reservation: Reservation):
        """Save a new reservation or update existing one"""
        reservations = self._load_from_file(self.filename)
        reservation_dict = reservation.to_dict()

        # Update existing or add new
        updated = False
        for i, r in enumerate(reservations):
            if r['reservation_id'] == reservation.reservation_id:
                reservations[i] = reservation_dict
                updated = True
                break

        if not updated:
            reservations.append(reservation_dict)

        self._save_to_file(self.filename, reservations)

    def get_reservation(self, reservation_id: str) -> Reservation:
        """Get a reservation by ID"""
        reservations = self._load_from_file(self.filename)
        for reservation_data in reservations:
            if reservation_data['reservation_id'] == reservation_id:
                return Reservation.from_dict(reservation_data)
        return None

    def delete_reservation(self, reservation_id: str):
        """Delete a reservation by ID"""
        reservations = self._load_from_file(self.filename)
        reservations = [
            r for r in reservations
            if r['reservation_id'] != reservation_id
        ]
        self._save_to_file(self.filename, reservations)

    def get_all_reservations(self) -> list:
        """Get all reservations"""
        reservations = self._load_from_file(self.filename)
        return [Reservation.from_dict(r) for r in reservations]

    def get_hotel_reservations(self, hotel_id: str) -> list:
        """Get all reservations for a specific hotel"""
        all_reservations = self._load_from_file(self.filename)
        hotel_reservations = [
            r for r in all_reservations if r['hotel_id'] == hotel_id
        ]
        return [Reservation.from_dict(r) for r in hotel_reservations]

    def get_customer_reservations(self, customer_id: str) -> list:
        """Get all reservations for a specific customer"""
        all_reservations = self._load_from_file(self.filename)
        customer_reservations = [
            r for r in all_reservations if r['customer_id'] == customer_id
        ]
        return [Reservation.from_dict(r) for r in customer_reservations]
