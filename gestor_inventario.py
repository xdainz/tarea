mensaje_error = 'Error en los datos ingresados.\n'

productos = []

def asignar_producto(nombre,categoria,precio,stock):
    productos = {
    'Nombre': nombre,
    'Categoría': categoria,
    'Precio': precio,
    'Stock': stock
}
    return productos

while True:
    while True:
        print('[1] Registrar producto\n'
            '[2] Listar todos los productos\n'
            '[3] Imprimir informe de inventario\n'
            '[4] Salir del programa')
        
        try:
            opcion_menu = int(input(': '))
        except ValueError:
            print(mensaje_error)
            continue
        
        if 1 <= opcion_menu <= 4:
            break
        else:
            print(mensaje_error)

    if opcion_menu == 1:
        while True:
            nombre_producto = input('Ingrese nombre del producto\n: ')
            while True:
                try:
                    elegir_categoria = int(input('Ingrese categoría\n'
                                            '[1] Electrónica\n'
                                            '[2] Ropa\n'
                                            '[3] Alimentos\n: '))
                except ValueError:
                    print(mensaje_error)
                    continue

                if 1 <= elegir_categoria <= 3:
                    if elegir_categoria == 1:
                        categoria_producto = 'Electrónica'
                    elif elegir_categoria == 2:
                        categoria_producto = 'Ropa'
                    else:
                        categoria_producto = 'Alimentos'
                    break
                else:
                    print(mensaje_error)
            
            while True:
                try:
                    precio_producto = int(input('Ingrese precio\n: '))
                except ValueError:
                    print(mensaje_error)
                    continue
                break
            while True:
                try:
                    stock_producto = int(input('Ingrese el stock\n: '))
                except ValueError:
                    print(mensaje_error)
                    continue
                break

            productos.append(asignar_producto(nombre_producto,categoria_producto,precio_producto, stock_producto))
            print('Producto agregado con exito.')
            break

    elif opcion_menu == 2:
        for producto in productos:
            print(producto['Nombre'])

    elif opcion_menu == 3:
        while True:
            try:
                opcion_inventario = int(input('Seleccione los productos a mostrar\n'
                                            '[1] Todos los productos\n'
                                            '[2] Por categoría\n: '))
            except ValueError:
                print(mensaje_error)
                continue
            
            if 1 <= opcion_inventario <= 2:
                break
            else:
                print(mensaje_error)

        if opcion_inventario == 1:
            for producto in productos:
                print(f'{producto['Nombre']}, Stock: {producto['Stock']}')

        else:
            while True:
                try:
                    opcion_categoria = int(input('[1] Electronica\n'
                                                 '[2] Ropa\n'
                                                 '[3] Alimentos\n: '))
                except ValueError:
                    print(mensaje_error)
                    continue
                if 1<= opcion_categoria <= 3:
                    break
                else:
                    print(mensaje_error)

            if opcion_categoria == 1:
                for producto in productos:
                    if producto['Categoría'] == 'Electrónica':
                        print(f'{producto['Nombre']}, Stock: {producto['Stock']}')
            elif opcion_categoria == 2:
                for producto in productos:
                    if producto['Categoría'] == 'Ropa':
                        print(f'{producto['Nombre']}, Stock: {producto['Stock']}')
            else:
                for producto in productos:
                    if producto['Categoría'] == 'Alimentos':
                        print(f'{producto['Nombre']}, Stock: {producto['Stock']}')

    if opcion_menu == 4:
        input('Presione enter para finalizar...')
        break