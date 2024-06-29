from django.urls import path 
from . import views



urlpatterns = [
    path('index/', views.index, name='index'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('inicioDeSesion/', views.inicioDeSesion, name='inicioDeSesion'),
    path('ayuda/', views.ayuda, name='ayuda'),
    path('informacion/', views.informacion, name='informacion'),
    path('registro/', views.registro, name='registro'),
    path('QuienesSomos/', views.QuienesSomos, name='QuienesSomos'),
    path('productosPerro/', views.productoPerro, name='productosPerro'),
    path('productosGatos/', views.productoGato, name='productosGato'),
    
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('agregar_al_carrito_perro/<int:producto_id>/', views.agregar_al_carrito_perro, name='agregar_al_carrito_perro'),
    path('agregar_al_carrito_gato/<int:producto_id>/', views.agregar_al_carrito_gato, name='agregar_al_carrito_gato'),
    path('eliminar_del_carrito/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    
    path('autenticacion/', views.autenticacion, name='autenticacion'),
    
    #admin productos generales
    path('admin/productos/', views.lista_productos, name='lista_productos'),
    path('admin/productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('admin/productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('admin/productos/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    
    #admin productos para perros
    path('agregar_producto_perros/', views.agregar_producto_perros, name='agregar_producto_perros'),
    path('editar_producto_perros/<int:producto_id>/', views.editar_producto_perros, name='editar_producto_perros'),
    path('eliminar_producto_perro/<int:producto_id>/', views.eliminar_producto_perros, name='eliminar_producto_perros'),
    #admin productos para gatos
    path('agregar_producto_gatos/', views.agregar_producto_gatos, name='agregar_producto_gatos'),
    path('editar_producto_gatos/<int:producto_id>/', views.editar_producto_gatos, name='editar_producto_gatos'),
    path('eliminar_producto_gatos/<int:producto_id>/', views.eliminar_producto_gatos, name='eliminar_producto_gatos'),
    
]
