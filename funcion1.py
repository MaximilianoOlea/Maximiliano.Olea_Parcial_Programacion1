# 1. Crear una función llamada aplicarAumento que reciba como parámetro el 
# precio de un producto y devuelva el valor del producto con un aumento del 5%. Realizar la llamada desde el main.

def aplicarAumento (precio:float)->float:
    """_summary_
        recibe un precio y le aplica un aumento del %5
    Args:
        precio (float): precio al que se quiere aplicar aumento del %5

    Returns:
        float: devuelve el precio con el aumento aplicado
    """
    precio_con_aumento = precio + precio * 0.5
    
    return precio_con_aumento


precio = 10.5

precio_con_aumento = aplicarAumento(precio)

print (f"El precio es de ${precio} y con aumento es de ${precio_con_aumento}")