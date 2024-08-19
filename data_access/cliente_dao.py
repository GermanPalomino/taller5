from models.cliente_dto import ClienteDTO

class ClienteDAO:
    def __init__(self, database):
        self._db = database

    def insertar_cliente(self, cliente):
        connection = self._db.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "{CALL InsertarCliente (?, ?, ?, ?, ?, ?, ?)}",
            cliente.nombre, cliente.apellido, cliente.direccion,
            cliente.ciudad, cliente.email, cliente.telefono, cliente.ocupacion
        )
        connection.commit()

    def obtener_cliente_por_id(self, cliente_id):
        connection = self._db.get_connection()
        cursor = connection.cursor()
        cursor.execute("{CALL ObtenerClientePorID (?)}", cliente_id)
        row = cursor.fetchone()
        if row:
            return ClienteDTO(
                id=row.ID, nombre=row.Nombre, apellido=row.Apellido,
                direccion=row.Direccion, ciudad=row.Ciudad, email=row.Email,
                telefono=row.Telefono, ocupacion=row.Ocupacion
            )
        return None

    def actualizar_cliente(self, cliente):
        connection = self._db.get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "{CALL ActualizarCliente (?, ?, ?, ?, ?, ?, ?, ?)}",
            cliente.id, cliente.nombre, cliente.apellido, cliente.direccion,
            cliente.ciudad, cliente.email, cliente.telefono, cliente.ocupacion
        )
        connection.commit()

    def eliminar_cliente(self, cliente_id):
        connection = self._db.get_connection()
        cursor = connection.cursor()
        cursor.execute("{CALL EliminarCliente (?)}", cliente_id)
        connection.commit()