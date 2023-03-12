# Validates that the input data passed to a function is a single character string (Character)
def validate_char_data(func):
    def wrapper(*args):
        data = args[1]
        if not isinstance(data, str) or len (data) != 1: # or ord(data) > 255:
            raise TypeError("Only characters can be added to the linked list.")
        return func(*args)
    return wrapper
