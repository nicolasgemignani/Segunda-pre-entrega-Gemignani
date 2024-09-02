from mi_paquete.cliente import Cliente

BD = {}
archivo = 'clientes.json'

cliente1 = Cliente('Nicolas', 'Gemignani', 25, 'nicolasg@outlook.com', 1153522185, '1')
cliente2 = Cliente('Alejandro', 'Gemignani', 27, 'alejandrof@outlook.com', 1187233487, '2')

cliente1.registrar_y_guardar(BD, archivo)
cliente2.registrar_y_guardar(BD, archivo)

cliente1.comprar('Laptop', 1, 1200.00)
cliente1.comprar('Mouse', 2, 25.50)


cliente2.comprar('Teclado', 1, 200.00)
cliente2.comprar('Auriculares', 3, 500.00)
cliente2.mostrar_compras()
cliente1.mostrar_compras()

print(BD)

cliente3 = Cliente('Alejandro', 'Gemignani', 27, 'alejandrof@outlook.com', 1187233487, '2')
cliente3.registrar_y_guardar(BD, archivo)