
def NULL_not_found(object: any) -> int:
    """
    Print different types of none values
    """
    status: int = 0
    text_to_print: str = "Type not Found"
    type_obj = type(object)

    if (object is None):
        text_to_print = f"Nothing: {object} {type_obj}"
    elif (type_obj == float and object != object):
        text_to_print = f"Cheese: {object} {type_obj}"
    elif (type_obj == int and object == 0):
        text_to_print = f"Zero: {object} {type_obj}"
    elif (type_obj == str and object == ""):
        text_to_print = f"Empty: {object} {type_obj}"
    elif (type_obj == bool and object is False):
        text_to_print = f"Fake: {object} {type_obj}"
    else:
        status = 1

    print(text_to_print)
    return status
