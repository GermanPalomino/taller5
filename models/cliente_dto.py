class ClienteDTO:
    def __init__(self, id=None, nombre=None, apellido=None, direccion=None, ciudad=None, email=None, telefono=None, ocupacion=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.ciudad = ciudad
        self.email = email
        self.telefono = telefono
        self.ocupacion = ocupacion