from datetime import datetime
from services import (
    HotelService,
    CustomerService,
    ReservationService,
)


class ConsoleUI:
    def __init__(
        self,
        hotel_service: HotelService,
        customer_service: CustomerService,
        reservation_service: ReservationService,
    ):
        self.hotel_service = hotel_service
        self.customer_service = customer_service
        self.reservation_service = reservation_service

    def start(self):
        """Inicia la interfaz de usuario"""
        while True:
            self._show_main_menu()
            choice = input("\nSeleccione una opción: ")

            try:
                if choice == "1":
                    self._hotel_menu()
                elif choice == "2":
                    self._customer_menu()
                elif choice == "3":
                    self._reservation_menu()
                elif choice == "4":
                    print("\n¡Gracias por usar el sistema de reservas!")
                    break
                else:
                    print("\nOpción inválida. Por favor intente de nuevo.")
            except Exception as e:
                print(f"\nError: {str(e)}")

    def _show_main_menu(self):
        """Muestra el menú principal"""
        print("\n=== SISTEMA DE RESERVAS DE HOTEL ===")
        print("1. Gestión de Hoteles")
        print("2. Gestión de Clientes")
        print("3. Gestión de Reservas")
        print("4. Salir")

    def _hotel_menu(self):
        """Menú de gestión de hoteles"""
        while True:
            print("\n=== GESTIÓN DE HOTELES ===")
            print("1. Crear Hotel")
            print("2. Mostrar Información de Hotel")
            print("3. Modificar Hotel")
            print("4. Eliminar Hotel")
            print("5. Volver al Menú Principal")

            choice = input("\nSeleccione una opción: ")

            try:
                if choice == "1":
                    self._create_hotel()
                elif choice == "2":
                    self._display_hotel()
                elif choice == "3":
                    self._modify_hotel()
                elif choice == "4":
                    self._delete_hotel()
                elif choice == "5":
                    break
                else:
                    print("\nOpción inválida. Por favor intente de nuevo.")
            except Exception as e:
                print(f"\nError: {str(e)}")

    def _customer_menu(self):
        """Menú de gestión de clientes"""
        while True:
            print("\n=== GESTIÓN DE CLIENTES ===")
            print("1. Crear Cliente")
            print("2. Mostrar Información de Cliente")
            print("3. Modificar Cliente")
            print("4. Eliminar Cliente")
            print("5. Volver al Menú Principal")

            choice = input("\nSeleccione una opción: ")

            try:
                if choice == "1":
                    self._create_customer()
                elif choice == "2":
                    self._display_customer()
                elif choice == "3":
                    self._modify_customer()
                elif choice == "4":
                    self._delete_customer()
                elif choice == "5":
                    break
                else:
                    print("\nOpción inválida. Por favor intente de nuevo.")
            except Exception as e:
                print(f"\nError: {str(e)}")

    def _reservation_menu(self):
        """Menú de gestión de reservas"""
        while True:
            print("\n=== GESTIÓN DE RESERVAS ===")
            print("1. Crear Reserva")
            print("2. Mostrar Reserva")
            print("3. Cancelar Reserva")
            print("4. Volver al Menú Principal")

            choice = input("\nSeleccione una opción: ")

            try:
                if choice == "1":
                    self._create_reservation()
                elif choice == "2":
                    self._display_reservation()
                elif choice == "3":
                    self._cancel_reservation()
                elif choice == "4":
                    break
                else:
                    print("\nOpción inválida. Por favor intente de nuevo.")
            except Exception as e:
                print(f"\nError: {str(e)}")

    # Métodos para gestión de hoteles
    def _create_hotel(self):
        """Crear un nuevo hotel"""
        print("\n=== CREAR HOTEL ===")
        name = input("Nombre del hotel: ")
        location = input("Ubicación: ")
        total_rooms = int(input("Número total de habitaciones: "))

        hotel = self.hotel_service.create_hotel(name, location, total_rooms)
        print(f"\nHotel creado exitosamente. ID: {hotel.hotel_id}")

    def _display_hotel(self):
        """Mostrar información de un hotel"""
        print("\n=== INFORMACIÓN DE HOTEL ===")
        hotel_id = input("ID del hotel: ")
        hotel = self.hotel_service.hotel_repo.get_hotel(hotel_id)

        if hotel:
            print(f"\nID: {hotel.hotel_id}")
            print(f"Nombre: {hotel.name}")
            print(f"Ubicación: {hotel.location}")
            print(f"Habitaciones totales: {hotel.total_rooms}")
            print(f"Habitaciones disponibles: {hotel.available_rooms}")
        else:
            print("\nHotel no encontrado.")

    def _modify_hotel(self):
        """Modificar información de un hotel"""
        print("\n=== MODIFICAR HOTEL ===")
        hotel_id = input("ID del hotel: ")
        name = input("Nuevo nombre (dejar vacío para mantener actual): ")
        location = input(
            "Nueva ubicación (dejar vacío para mantener actual): "
        )
        total_rooms = input(
            "Nuevo total de habitaciones (dejar vacío para no cambiar): "
        )

        self.hotel_service.modify_hotel(
            hotel_id,
            name if name else None,
            location if location else None,
            int(total_rooms) if total_rooms else None,
        )
        print("\nHotel modificado exitosamente.")

    def _delete_hotel(self):
        """Eliminar un hotel"""
        print("\n=== ELIMINAR HOTEL ===")
        hotel_id = input("ID del hotel: ")
        self.hotel_service.delete_hotel(hotel_id)
        print("\nHotel eliminado exitosamente.")

    # Métodos para gestión de clientes
    def _create_customer(self):
        """Crear un nuevo cliente"""
        print("\n=== CREAR CLIENTE ===")
        name = input("Nombre del cliente: ")
        email = input("Email: ")
        phone = input("Teléfono: ")

        customer = self.customer_service.create_customer(name, email, phone)
        print(f"\nCliente creado exitosamente. ID: {customer.customer_id}")

    def _display_customer(self):
        """Mostrar información de un cliente"""
        print("\n=== INFORMACIÓN DE CLIENTE ===")
        customer_id = input("ID del cliente: ")
        customer = self.customer_service.customer_repo.get_customer(
            customer_id
        )

        if customer:
            print(f"\nID: {customer.customer_id}")
            print(f"Nombre: {customer.name}")
            print(f"Email: {customer.email}")
            print(f"Teléfono: {customer.phone}")
        else:
            print("\nCliente no encontrado.")

    def _modify_customer(self):
        """Modificar información de un cliente"""
        print("\n=== MODIFICAR CLIENTE ===")
        customer_id = input("ID del cliente: ")
        name = input("Nuevo nombre (dejar vacío para mantener actual): ")
        email = input("Nuevo email (dejar vacío para mantener actual): ")
        phone = input("Nuevo teléfono (dejar vacío para mantener actual): ")

        self.customer_service.modify_customer(
            customer_id,
            name if name else None,
            email if email else None,
            phone if phone else None,
        )
        print("\nCliente modificado exitosamente.")

    def _delete_customer(self):
        """Eliminar un cliente"""
        print("\n=== ELIMINAR CLIENTE ===")
        customer_id = input("ID del cliente: ")
        self.customer_service.delete_customer(customer_id)
        print("\nCliente eliminado exitosamente.")

    # Métodos para gestión de reservas
    def _create_reservation(self):
        """Crear una nueva reserva"""
        print("\n=== CREAR RESERVA ===")
        hotel_id = input("ID del hotel: ")
        customer_id = input("ID del cliente: ")

        check_in_str = input("Fecha de check-in (YYYY-MM-DD): ")
        check_out_str = input("Fecha de check-out (YYYY-MM-DD): ")
        num_rooms = int(input("Número de habitaciones: "))

        check_in = datetime.strptime(check_in_str, "%Y-%m-%d")
        check_out = datetime.strptime(check_out_str, "%Y-%m-%d")

        reservation = self.reservation_service.create_reservation(
            hotel_id, customer_id, check_in, check_out, num_rooms
        )
        print(
            f"\nReserva creada exitosamente. ID: "
            f"{reservation.reservation_id}"
        )

    def _display_reservation(self):
        """Mostrar información de una reserva"""
        print("\n=== INFORMACIÓN DE RESERVA ===")
        reservation_id = input("ID de la reserva: ")
        reservation = (
            self.reservation_service.reservation_repo.get_reservation(
                reservation_id
            )
        )

        if reservation:
            print(f"\nID de Reserva: {reservation.reservation_id}")
            print(f"ID de Hotel: {reservation.hotel_id}")
            print(f"ID de Cliente: {reservation.customer_id}")
            print(f"Check-in: {reservation.check_in}")
            print(f"Check-out: {reservation.check_out}")
            print(
                f"Número de habitaciones: {reservation.num_rooms}"
            )
            estado_str = f"Estado: {reservation.status}"
            print(estado_str)
        else:
            print("\nReserva no encontrada.")

    def _cancel_reservation(self):
        """Cancelar una reserva"""
        print("\n=== CANCELAR RESERVA ===")
        reservation_id = input("ID de la reserva: ")
        self.reservation_service.cancel_reservation(reservation_id)
        print("\nReserva cancelada exitosamente.")
