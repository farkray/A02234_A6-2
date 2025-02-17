from datetime import datetime
import uuid
from models import Hotel, Customer, Reservation
from repository import (
    HotelRepository,
    CustomerRepository,
    ReservationRepository,
)


class HotelService:
    def __init__(
        self,
        hotel_repo: HotelRepository,
        reservation_repo: ReservationRepository,
    ):
        self.hotel_repo = hotel_repo
        self.reservation_repo = reservation_repo

    def create_hotel(
        self, name: str, location: str, total_rooms: int
    ) -> Hotel:
        """Create a new hotel"""
        hotel_id = str(uuid.uuid4())
        hotel = Hotel(hotel_id, name, location, total_rooms)
        self.hotel_repo.save_hotel(hotel)
        return hotel

    def delete_hotel(self, hotel_id: str) -> bool:
        """Delete a hotel if it has no active reservations"""
        reservations = self.reservation_repo.get_hotel_reservations(hotel_id)
        active_reservations = [r for r in reservations if r.status == "active"]

        if active_reservations:
            raise ValueError(
                "Cannot delete hotel with active reservations"
            )

        self.hotel_repo.delete_hotel(hotel_id)
        return True

    def modify_hotel(
        self,
        hotel_id: str,
        name: str = None,
        location: str = None,
        total_rooms: int = None,
    ) -> Hotel:
        """Modify hotel information"""
        hotel = self.hotel_repo.get_hotel(hotel_id)
        if not hotel:
            raise ValueError("Hotel not found")

        if name:
            hotel.name = name
        if location:
            hotel.location = location
        if total_rooms:
            if total_rooms < hotel.total_rooms - hotel.available_rooms:
                raise ValueError(
                    "Cannot reduce total rooms below current occupancy"
                )
            hotel.available_rooms += (total_rooms - hotel.total_rooms)
            hotel.total_rooms = total_rooms

        self.hotel_repo.save_hotel(hotel)
        return hotel


class CustomerService:
    def __init__(
        self,
        customer_repo: CustomerRepository,
        reservation_repo: ReservationRepository,
    ):
        self.customer_repo = customer_repo
        self.reservation_repo = reservation_repo

    def create_customer(self, name: str, email: str, phone: str) -> Customer:
        """Create a new customer"""
        customer_id = str(uuid.uuid4())
        customer = Customer(customer_id, name, email, phone)
        self.customer_repo.save_customer(customer)
        return customer

    def delete_customer(self, customer_id: str) -> bool:
        """Delete a customer if they have no active reservations"""
        reservations = self.reservation_repo.get_customer_reservations(
            customer_id
        )
        active_reservations = [r for r in reservations if r.status == "active"]

        if active_reservations:
            raise ValueError(
                "Cannot delete customer with active reservations"
            )

        self.customer_repo.delete_customer(customer_id)
        return True

    def modify_customer(
        self,
        customer_id: str,
        name: str = None,
        email: str = None,
        phone: str = None,
    ) -> Customer:
        """Modify customer information"""
        customer = self.customer_repo.get_customer(customer_id)
        if not customer:
            raise ValueError("Customer not found")

        if name:
            customer.name = name
        if email:
            customer.email = email
        if phone:
            customer.phone = phone

        self.customer_repo.save_customer(customer)
        return customer


class ReservationService:
    def __init__(
        self,
        hotel_repo: HotelRepository,
        customer_repo: CustomerRepository,
        reservation_repo: ReservationRepository,
    ):
        self.hotel_repo = hotel_repo
        self.customer_repo = customer_repo
        self.reservation_repo = reservation_repo

    def create_reservation(
        self,
        hotel_id: str,
        customer_id: str,
        check_in: datetime,
        check_out: datetime,
        num_rooms: int,
    ) -> Reservation:
        """Create a new reservation"""
        # Validate hotel and customer exist
        hotel = self.hotel_repo.get_hotel(hotel_id)
        customer = self.customer_repo.get_customer(customer_id)

        if not hotel:
            raise ValueError("Hotel not found")
        if not customer:
            raise ValueError("Customer not found")

        # Validate dates
        if check_in >= check_out:
            raise ValueError("Check-out must be after check-in")
        if check_in < datetime.now():
            raise ValueError("Check-in cannot be in the past")

        # Validate room availability
        if num_rooms > hotel.available_rooms:
            raise ValueError("Not enough rooms available")

        # Create reservation
        reservation_id = str(uuid.uuid4())
        reservation = Reservation(
            reservation_id,
            hotel_id,
            customer_id,
            check_in,
            check_out,
            num_rooms,
        )

        # Update hotel availability
        hotel.available_rooms -= num_rooms

        # Save changes
        self.reservation_repo.save_reservation(reservation)
        self.hotel_repo.save_hotel(hotel)

        return reservation

    def cancel_reservation(self, reservation_id: str) -> bool:
        """Cancel a reservation"""
        reservation = self.reservation_repo.get_reservation(reservation_id)
        if not reservation:
            raise ValueError("Reservation not found")

        if reservation.status != "active":
            raise ValueError("Reservation is not active")

        # Update hotel availability
        hotel = self.hotel_repo.get_hotel(reservation.hotel_id)
        hotel.available_rooms += reservation.num_rooms

        # Update reservation status
        reservation.status = "cancelled"

        # Save changes
        self.reservation_repo.save_reservation(reservation)
        self.hotel_repo.save_hotel(hotel)

        return True
