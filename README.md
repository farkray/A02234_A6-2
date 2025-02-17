# A02234_A6-2
Ejercicio de programación 3 y pruebas de unidad

# Sistema de Reservas de Hotel

## Video Tutorial del Sistema

[![Video Tutorial](https://cdn.loom.com/sessions/thumbnails/134be541761445a1be79ba4caf5bb0b5-6629c9addc2584f3-full-play.gif)](https://www.loom.com/share/134be541761445a1be79ba4caf5bb0b5)

[Ver video tutorial completo](https://www.loom.com/share/134be541761445a1be79ba4caf5bb0b5?sid=808c2a4b-7430-4305-adaa-64fb6e426c9f)

## Descripción
Sistema de gestión de reservas hoteleras que permite administrar hoteles, clientes y reservaciones a través de una interfaz de consola.

## Características Principales
- Gestión completa de hoteles (crear, mostrar, modificar, eliminar)
- Gestión de clientes (crear, mostrar, modificar, eliminar)
- Sistema de reservaciones (crear, mostrar, cancelar)
- Persistencia de datos en archivos JSON
- Validaciones de negocio
- Interfaz de usuario por consola

## Requisitos
- Python 3.7 o superior
- Sistema operativo: Windows, Linux o macOS
- Permisos de lectura/escritura en el directorio de la aplicación

## Instalación
1. Clonar el repositorio
```bash
git clone [URL del repositorio]
```

2. Navegar al directorio del proyecto
```bash
cd hotel-system
```

## Uso
Ejecutar el programa:
```bash
python main.py
```

## Estructura del Proyecto
```
hotel_system/
│
├── data/                  # Directorio donde se guardan los archivos JSON
│   ├── hotels.json
│   ├── customers.json
│   └── reservations.json 
│
├── models.py             # Definición de las clases base
├── repository.py         # Clases para persistencia de datos
├── services.py          # Lógica de negocio
├── console_ui.py        # Interfaz de usuario
└── main.py              # Punto de entrada de la aplicación
```
