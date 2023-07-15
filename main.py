import os
from operations import OPERATIONS, operator_collection
from data import request_data_from_user, check_input_for_number
from colored import colored_input, colored_print, run_colored

RESTART_KEYWORD = "1
clear_screen = lambda: os.system("cls")

def show_menu() -> None:
    """
        This procedure will show the user a simple guide to explain the
        purpose and expected input for the prober use
    """
    colored_print(f"%tGreetings user,\n%nyou currently using my Simple Calculator program.\nThe current version of this instance is %i{PROGRAM_VERSION}%n")
    colored_print(f"\n%nThis calculator is designed to calculate single operations only.\nYou can input two integer or float values called number 1 and 2")
    colored_print(f"%nand an operator with witch the calculation will be made,\ncurrently there are the following operations to use: %i{operator_collection}%n.")
    colored_print(f"\n%nPlease enter the following information in order to get\nthe desired outcome:")

def main():
    program_active = True
    clear_screen()
    while program_active:
        show_menu()

        number_1 = request_data_from_user(prompt="Please enter the first number: ",
                error_case=lambda x: f'%i"{x}"%e  is not a valid input, please enter only %ifloat%e or %iinteger%e values!',
                validation_func=check_input_for_number)

        operator_func = request_data_from_user(prompt=f"Please enter you desired operator %i[{operator_collection}]: ",
                error_case=lambda x: f'%i"{x}"%e  is not a valid operator, please select out of thus valid ones: %i{operator_collection}',
                validation_func=lambda x: OPERATIONS.get(x))

        number_2 = request_data_from_user(prompt="Please enter the second number: ",
                error_case=lambda x: f'%i"{x}"%e is not a valid input, please enter only %ifloat%e or %iinteger%e values!',
                validation_func=check_input_for_number)

        result = operator_func(number_1, number_2)

        colored_print(f"%nYou result is %ui{result}")

        user_input = colored_input(f'Start Another Calculation? %i("{RESTART_KEYWORD}": yes, Any: stop)')
        if user_input == RESTART_KEYWORD:
            clear_screen()
            continue

        break

if __name__ == "__main__":
    run_colored(main)
