class Persona:
    def __init__(self, nombre, apellido, edad):
        """ 
        Inicializa una nueva instancia Persona 

        :param nombre: Nombre de la persona
        :param apellido: Apellido de la persona
        :param edad: Edad de la persona
        """
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        """ 
        Devuelve una representacion en cadena de la persona

        :return: Cadena de texto con la representacion de la persona
        """
        return f'Persona: {self.nombre} {self.apellido}, Edad: {self.edad}'

    def saludar(self):
        """ 
        Devuelve un salido que incluye el nombre y el apellido de la persona
        :return: Cadena de texto con el saludo 
        """
        return f'Hola, me llamo {self.nombre} {self.apellido}.'

    def despedir(self):
        """ 
        Devuelve un mensaje de despedida

        :return: Cadena de texto con el mensaje de despedida
        """
        return 'Adiós, un gusto conocerte.'