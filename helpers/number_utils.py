def convert_string_to_float(num_str: str, decimal_places: int = 2):
    num = float(num_str)
    format_str = '{:.' + str(decimal_places) + 'f}'
    return format_str.format(num)
