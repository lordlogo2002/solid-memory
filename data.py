from typing import Callable, Any
from colored import colored_input, error_message

USER_INPUT_INVALID = True

class Storage:
    stored = {}

    @classmethod
    def store_value(cls, name:str, value:int|float) -> None:
        cls.store_value[name] = value

    @classmethod
    def delete_value(cls, name:str) -> bool:
        if name not in cls.store_value:
            return False
        del cls.store_value[name]
        return True

def check_input_for_number(value:str) -> float|int|None:
    """
        Check if the input of the user is either an integer or a float value
        and returning it as the representing type
        if its not a integer or a float value it will return None

        Returns:
            int | float: the converted value in the representing type if valid
            None: in any case of the input not being a integer or float value
    """
    if "." in value:
        possible_float_value = value.replace(".", "")
        if possible_float_value.isdigit():
            return float(value)

    if value.isdigit():
        return int(value)

    return None

def request_data_from_user(prompt:str, error_case:Callable, validation_func:Callable) -> Any:
    """
        Request a user to input some value by using the input function with the given prompt
        then validate it with the given Callable validation_func and return its return value
        if its not None
        If its none call the Callable error_case with the user input as argument and restart

        Args:
            prompt(str): the prompt that will be shown to the user
            error_case(Callable): this will be called with the invalid input
                                  if the validation_func returns None
            validation_func(Callable): this will be called to check the input
                                       return None to set it as invalid

        Returns:
            (Any): the return is guarantied to be valid as long as the validation function is correct

        Exceptions:
            TypeError: if you pass a not callable object to error_case or validation_func
    """
    while USER_INPUT_INVALID:
        user_input = colored_input(prompt)
        check_result = validation_func(user_input)
        if check_result is None:
            error_message(error_case(user_input))
            continue
        return check_result