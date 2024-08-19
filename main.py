from data_access.connection import Database
from data_access.cliente_dao import ClienteDAO
from models.cliente_dto import ClienteDTO

def menu():
    print("\nSeleccione una opción:")
    print("1. Insertar un nuevo cliente")
    print("2. Obtener un cliente por ID")
    print("3. Actualizar un cliente")
    print("4. Eliminar un cliente")
    print("5. Salir")
    return input("Ingrese el número de la opción: ")

def get_cliente_data():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    direccion = input("Dirección: ")
    ciudad = input("Ciudad: ")
    email = input("Email: ")
    telefono = input("Teléfono: ")
    ocupacion = input("Ocupación: ")
    return ClienteDTO(nombre=nombre, apellido=apellido, direccion=direccion, ciudad=ciudad, email=email, telefono=telefono, ocupacion=ocupacion)

def main():
    # Configurar la conexión a la base de datos SQL Server con autenticación de Windows
    db = Database()
    db.connect(
        driver='ODBC Driver 17 for SQL Server',
        server='PC-DE-GERMAN',
        database='Practica_Patrones'
    )

    # Crear una instancia de ClienteDAO
    cliente_dao = ClienteDAO(db)

    while True:
        opcion = menu()
        
        if opcion == '1':
            print("\n--- Insertar un nuevo cliente ---")
            nuevo_cliente = get_cliente_data()
            cliente_dao.insertar_cliente(nuevo_cliente)
            print("Cliente insertado con éxito.")
        
        elif opcion == '2':
            print("\n--- Obtener un cliente por ID ---")
            cliente_id = int(input("Ingrese el ID del cliente: "))
            cliente = cliente_dao.obtener_cliente_por_id(cliente_id)
            if cliente:
                print(f"\nCliente: {cliente.nombre} {cliente.apellido}, {cliente.direccion}, {cliente.ciudad}, {cliente.email}, {cliente.telefono}, {cliente.ocupacion}")
            else:
                print("Cliente no encontrado.")
        
        elif opcion == '3':
            print("\n--- Actualizar un cliente ---")
            cliente_id = int(input("Ingrese el ID del cliente a actualizar: "))
            cliente = cliente_dao.obtener_cliente_por_id(cliente_id)
            if cliente:
                print("Ingrese los nuevos datos del cliente (deje en blanco para mantener el valor actual):")
                cliente.nombre = input(f"Nombre ({cliente.nombre}): ") or cliente.nombre
                cliente.apellido = input(f"Apellido ({cliente.apellido}): ") or cliente.apellido
                cliente.direccion = input(f"Dirección ({cliente.direccion}): ") or cliente.direccion
                cliente.ciudad = input(f"Ciudad ({cliente.ciudad}): ") or cliente.ciudad
                cliente.email = input(f"Email ({cliente.email}): ") or cliente.email
                cliente.telefono = input(f"Teléfono ({cliente.telefono}): ") or cliente.telefono
                cliente.ocupacion = input(f"Ocupación ({cliente.ocupacion}): ") or cliente.ocupacion
                cliente_dao.actualizar_cliente(cliente)
                print("Cliente actualizado con éxito.")
            else:
                print("Cliente no encontrado.")
        
        elif opcion == '4':
            print("\n--- Eliminar un cliente ---")
            cliente_id = int(input("Ingrese el ID del cliente a eliminar: "))
            cliente = cliente_dao.obtener_cliente_por_id(cliente_id)
            if cliente:
                confirm = input(f"¿Está seguro que desea eliminar al cliente {cliente.nombre} {cliente.apellido}? (s/n): ")
                if confirm.lower() == 's':
                    cliente_dao.eliminar_cliente(cliente_id)
                    print("Cliente eliminado con éxito.")
                else:
                    print("Operación cancelada.")
            else:
                print("Cliente no encontrado.")
        
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

    # Cerrar la conexión a la base de datos
    db.close_connection()

if __name__ == "__main__":
    main()