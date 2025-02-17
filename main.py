import os
from repository import (
    HotelRepository,
    CustomerRepository,
    ReservationRepository,
)
from services import HotelService, CustomerService, ReservationService
from console_ui import ConsoleUI


def main():
    # Crear directorio de datos si no existe
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Inicializar repositorios
    hotel_repo = HotelRepository(data_dir)
    customer_repo = CustomerRepository(data_dir)
    reservation_repo = ReservationRepository(data_dir)

    # Inicializar servicios
    hotel_service = HotelService(hotel_repo, reservation_repo)
    customer_service = CustomerService(customer_repo, reservation_repo)
    reservation_service = ReservationService(
        hotel_repo,
        customer_repo,
        reservation_repo
    )

    # Inicializar y ejecutar la interfaz de usuario
    ui = ConsoleUI(hotel_service, customer_service, reservation_service)
    ui.start()


if __name__ == "__main__":
    main()
