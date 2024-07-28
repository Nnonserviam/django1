document.addEventListener('DOMContentLoaded', () => {
    const botonesCarrito = document.querySelectorAll('.botonCarrito');
    const carritoItems = document.getElementById('carritoItems');
    const totalCarrito = document.getElementById('totalCarrito');
    const comprarButton = document.getElementById('comprar');
    
    let carrito = [];
    
    botonesCarrito.forEach(boton => {
        boton.addEventListener('click', (e) => {
            const producto = e.target.closest('.cardProducto');
            const nombreProducto = producto.querySelector('h4').textContent;
            const precioProducto = parseFloat(producto.querySelector('p:nth-of-type(2)').textContent.replace('Precio: $', ''));
            const idProducto = e.target.getAttribute('data-id');
            
            const productoCarrito = {
                id: idProducto,
                nombre: nombreProducto,
                precio: precioProducto,
                cantidad: 1
            };

            const productoExistente = carrito.find(item => item.id === idProducto);

            if (productoExistente) {
                productoExistente.cantidad += 1;
            } else {
                carrito.push(productoCarrito);
            }

            actualizarCarrito();
        });
    });

    comprarButton.addEventListener('click', () => {
        alert('Compra realizada con éxito!');
        carrito = [];
        actualizarCarrito();
    });

    function actualizarCarrito() {
        carritoItems.innerHTML = '';
        let total = 0;

        carrito.forEach(producto => {
            const item = document.createElement('div');
            item.classList.add('itemCarrito');
            item.innerHTML = `
                <p>${producto.nombre} - $${producto.precio} x ${producto.cantidad}</p>
            `;
            carritoItems.appendChild(item);
            total += producto.precio * producto.cantidad;
        });

        totalCarrito.textContent = total.toFixed(2);
    }
});
