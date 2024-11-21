class Carrito():

    def __init__(self, request):
        self.session = request.session
        #get 'key_sesion' de la sesion actual, si es que existe
        carrito = self.session.get('key_sesion')
        #si el usuario es nuevo no hay 'key_sesion', creamos una
        if 'key_sesion' not in request.session:
            carrito = self.session['key_sesion'] = {}
        #aseguramos que el carrito exista en todos los htmls
        self.carrito = carrito
    def agregar(self, producto):
        producto_id = str(producto.id)
        if producto_id not in self.carrito:
            pass
        else:
            self.carrito[producto_id] = {'precio': str(producto.precio)}
        self.session.modified = True
    
    def __len__(self):
        return len(self.carrito)
