from django.shortcuts import render, get_object_or_404, redirect
from .models import AnimalProducto, ProductoPerros, ProductoGatos, Carrito
from .forms import ProductoForm, ProductoPerrosForm, ProductoGatosForm
# Create your views here.

#vista del index
def index(request):
    productos = AnimalProducto.objects.all()
    return render(request, 'animales/index.html', {'productos': productos})

#vista de la pag favoritos
def favoritos(request):
    context= {}
    return render(request, 'animales/favoritos.html', context)

#vista de la pag carrito

def ver_carrito(request):
    carrito_items = Carrito.objects.all()
    
    def clean_price(price_str):
        # Elimina el signo de dólar y el separador de miles.
        price_str = price_str.replace('$', '').replace('.', '').replace(',', '.')
        return int(price_str)

    total = 0
    for item in carrito_items:
        if item.producto and item.producto.precio:
            total += clean_price(item.producto.precio) * item.cantidad
        elif item.producto_perros and item.producto_perros.precio:
            total += clean_price(item.producto_perros.precio) * item.cantidad
        elif item.producto_gatos and item.producto_gatos.precio:
            total += clean_price(item.producto_gatos.precio) * item.cantidad

    return render(request, 'animales/carrito.html', {'carrito_items': carrito_items, 'total': total})




# vista agregar productos al carro

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(AnimalProducto, id=producto_id)
    item, created = Carrito.objects.get_or_create(producto=producto)
    if not created:
        item.cantidad += 1
        item.save()
    return redirect('ver_carrito')

# vista agregar productos al carro perros
def agregar_al_carrito_perro(request, producto_id):
    producto = get_object_or_404(ProductoPerros, id=producto_id)
    item, created = Carrito.objects.get_or_create(producto_perros=producto)
    if not created:
        item.cantidad += 1
        item.save()
    return redirect('ver_carrito')

# vista agregar productos al carro gatos
def agregar_al_carrito_gato(request, producto_id):
    producto = get_object_or_404(ProductoGatos, id=producto_id)
    item, created = Carrito.objects.get_or_create(producto_gatos=producto)
    if not created:
        item.cantidad += 1
        item.save()
    return redirect('ver_carrito')


# vista eliminar productos
def eliminar_del_carrito(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Carrito, id=item_id)
        item.delete()
        return redirect('ver_carrito') 

#vista de la pag inicio de sesión
def inicioDeSesion(request):
    context={}
    return render(request, 'animales/inicioDeSesion.html', context)

#vista de la pag ayuda
def ayuda(request):
    context= {}
    return render(request, 'animales/ayuda.html', context)

#vista de la pag informacion
def informacion(request):
    context= {}
    return render(request, 'animales/informacion.html', context)

#vista de la pag registro
def registro(request):
    context= {}
    return render(request, 'animales/registro.html', context)

#vista de la pag quienes somos
def QuienesSomos(request):
    context= {}
    return render(request, 'animales/QuienesSomos.html', context)

#vista de la pag productosPerro
def productoPerro(request):
    productos =  ProductoPerros.objects.all()
    return render(request, 'animales/productosPerro.html', {'productos': productos})

#vista de la pag productoGato
def productoGato(request):
    productos =  ProductoGatos.objects.all()
    return render(request, 'animales/productosGato.html', {'productos': productos})

#vista para listar productos desde el admin
# Vista para listar todos los productos (AnimalProducto, ProductoPerros, ProductoGatos)
def lista_productos(request):
    productos_general = AnimalProducto.objects.all()
    productos_perros = ProductoPerros.objects.all()
    productos_gatos = ProductoGatos.objects.all()
    return render(request, 'animales/admin.html', {
        'productos_general': productos_general,
        'productos_perros': productos_perros,
        'productos_gatos': productos_gatos,
    })

#vista para agregar productos desde el admin
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'animales/admin_agregar_producto.html', {'form': form})

# Vista para agregar un producto de perros (ProductoPerros)
def agregar_producto_perros(request):
    if request.method == 'POST':
        form = ProductoPerrosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoPerrosForm()
    return render(request, 'animales/admin_agregar_producto_perros.html', {'form': form})

# Vista para agregar un producto de gatos (ProductoGatos)
def agregar_producto_gatos(request):
    if request.method == 'POST':
        form = ProductoGatosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoGatosForm()
    return render(request, 'animales/admin_agregar_producto_gatos.html', {'form': form})



#vista para eliminar los productos desde el admin
def editar_producto(request, producto_id):
    producto = get_object_or_404(AnimalProducto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'animales/admin_editar_producto.html', {'form': form, 'producto': producto})

# Vista para editar un producto de perros (ProductoPerros)
def editar_producto_perros(request, producto_id):
    producto = get_object_or_404(ProductoPerros, id=producto_id)
    if request.method == 'POST':
        form = ProductoPerrosForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoPerrosForm(instance=producto)
    return render(request, 'animales/admin_editar_producto_perros.html', {'form': form, 'producto': producto})

# Vista para editar un producto de gatos (ProductoGatos)
def editar_producto_gatos(request, producto_id):
    producto = get_object_or_404(ProductoGatos, id=producto_id)
    if request.method == 'POST':
        form = ProductoGatosForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoGatosForm(instance=producto)
    return render(request, 'animales/admin_editar_producto_gatos.html', {'form': form, 'producto': producto})


#vista para eliminar los productos desde el admin
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(AnimalProducto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'animales/admin_eliminar_producto.html', {'producto': producto})


# Vista para eliminar un producto de perros (ProductoPerros)
def eliminar_producto_perros(request, producto_id):
    producto = get_object_or_404(ProductoPerros, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'animales/admin_eliminar_producto_perros.html', {'producto': producto})

# Vista para eliminar un producto de gatos (ProductoGatos)
def eliminar_producto_gatos(request, producto_id):
    producto = get_object_or_404(ProductoGatos, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'animales/admin_eliminar_producto_gatos.html', {'producto': producto})