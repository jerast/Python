def valores_permitidos_filter(valores_validos):
    def decorador(func):
        def wrapper(data_path, time_range, filter, values, invert, order_by, desc, accum):
            # Verificar si los valores de los argumentos están en los valores permitidos
            if time_range not in valores_validos['time_range']:
                raise ValueError(f"Valor no válido para 'time_range'. Valores permitidos: {valores_validos['time_range']}")
            if filter not in valores_validos['filter']:
                raise ValueError(f"Valor no válido para 'filter'. Valores permitidos: {valores_validos['filter']}")
            if values not in valores_validos['values']:
                raise ValueError(f"Valor no válido para 'values'. Valores permitidos: {valores_validos['values']}")
            if order_by not in valores_validos['order_by']:
                raise ValueError(f"Valor no válido para 'order_by'. Valores permitidos: {valores_validos['order_by']}")

            # Ejecutar la función original
            return func(data_path, time_range, filter, values, invert, order_by, desc, accum)
        return wrapper
    return decorador