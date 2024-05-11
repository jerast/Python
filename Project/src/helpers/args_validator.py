from functools import wraps

def args_verifier(args_valid_options: list[list]):
   def decorator(func):
      @wraps(func)
      def validateParamsWrapper(*args, **kwargs):
      
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