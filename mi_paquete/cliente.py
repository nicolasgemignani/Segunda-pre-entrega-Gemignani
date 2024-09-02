from .persona import Persona
from .utilidades import guardarArchivo

class Cliente(Persona):
    def __init__(self, nombre, apellido, edad, email, celular, id_cliente):
        """ 
        Inicializa un nuevo objeto Cliente.

        :param nombre: Nombre del cliente
        :param apellido: Apellido del cliente
        :param edad: Edad del cliente
        :param email: Correo del cliente
        :param celular: Numero de celular del cliente
        :param id_cliente: Identificador unico del cliente
        """
        super().__init__(nombre, apellido, edad)
        self.email = email
        self.celular = celular
        self.id_cliente = id_cliente
        self.compras = []

    def __str__(self):
        """ 
        Representacion en cadena del cliente.
        :return: Cadena con la informacion del cliente
        """
        return f'Cliente: {self.nombre} {self.apellido}, Correo: {self.email}'

    def registrarse(self, BD):
        """
        Registra un nuevo cliente en el diccionario BD si no esta registrado.

        :param BD: Diccionario que contiene la base de datos de clientes
        :return: Tru si el cliente se registro exitosamente, False si ya esta registrado
        """
        cliente = {
            'Nombre': self.nombre,
            'Apellido': self.apellido,
            'Edad': self.edad,
            'Email': self.email,
            'Celular': self.celular,
            'ID': self.id_cliente
        }

        clave_cliente = self.email

        # Verifica si el cliente ya esta en la base de datos
        if clave_cliente not in BD:
            BD[clave_cliente] = cliente
            print(f'Cliente {self.nombre} registrado exitosamente.')
            return True
        else:
            print('El cliente ya está registrado.')
            return False

    def comprar(self, articulo, cantidad, precio_unitario):
        """ 
        Registra una compra realizada por el cliente:

        :param articulo: Nombre del articulo comprado
        :param cantidad: Cantidad del articulo comprado
        :param precio_unitario: Precio unitario del articulo
        """
        #Verifica que la cantidad y el precio sean validos
        if cantidad <= 0 or precio_unitario <= 0:
            print('La cantidad y el precio unitario deben ser mayores que cero')
            return

        costo_total = cantidad * precio_unitario
        self.compras.append({
            'Articulo': articulo,
            'Cantidad': cantidad,
            'Precio Unitario': precio_unitario,
            'Costo Total': costo_total
        })
        print(f'Compra realizada: {cantidad} {articulo}(s) por ${costo_total:.2f}.')

    def mostrar_compras(self): 
        """
        Muestra el historial de compras del cliente actual

        :return: None
        """
        if not self.compras:
            print(f'No hay compras registradas para el cliente {self.nombre}.')
            return

        print(f'Historial de compras de {self.nombre}:')
        for compra in self.compras:
            print(f"Articulo: {compra['Articulo']}, Cantidad: {compra['Cantidad']}, Precio Unitario: ${compra['Precio Unitario']:.2f}, Costo Total: ${compra['Costo Total']:.2f}")


    def registrar_y_guardar(self, BD, archivo):
        """ 
        Registra el cliente y guarda la base de datos en el archivo especificado

        :param BD: Diccionario que contiene la base de datos de Clientes
        :param archivo: Nombre del archivo en el que se guardara la base de datos
        """
        if self.registrarse(BD):
            guardarArchivo(BD, archivo)