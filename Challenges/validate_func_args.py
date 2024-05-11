from functools import wraps

def options_verifier(args_valid_options: list[list]):
   def decorator(func):
      @wraps(func)
      def validateParamsWrapper(*args, **kwargs):
      
         # Revisar si el parámetro coincide con las opciones válidas por argumento
         for param in kwargs:
            if param in args_valid_options:
               if kwargs[param] not in args_valid_options[param]:
                  raise ValueError(
                     f'{param}: `{kwargs[param]}` is not in valid options: {args_valid_options[param]}'
                  )

         # Ejecutar la función original
         return func(*args, **kwargs)
      return validateParamsWrapper
   return decorator


validateParams = {
   'time_range': ['Y', 'M', 'D'], 
   'filter': ['asesor', 'modelo', 'financiera', 'clasificacion'], 
   'values': ['cantidad', 'costo'], 
   'order_by': ['llave', 'valor'],
}

@options_verifier(validateParams)
def filter_data(
   data_path: str = ..., 
   time_range: str = ..., 
   filter: str = ...,
   values: str = ...,
   order_by: str = ...,
   invert: bool = False,
   desc: bool = False,
   accum: bool = False
) -> None:
   return

filter_data(
   data_path='/assets/data_cleaned.csv',
   time_range='Y', # [Y, M, D]
   filter='modelo', # [asesor, modelo, financiera, clasificacion]
   values='cantidad', # [cantidad, costo]
   order_by='valor', # [llave, valor]
   desc=True,
   accum=True,
   invert=False,
)