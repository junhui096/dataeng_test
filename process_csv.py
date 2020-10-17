from decimal import Decimal
from sys import argv

# Driver function responsible for File I/O
def process_dataset(input_name, output_name):
    with open(input_name, "r") as f:
        header = f.readline()
        with open(output_name, "w") as out:
            out.write('{}\n'.format(get_output_header()))
            row = f.readline()
            while row:
                try:
                    name, price = row.split(",")
                    out.write('{}\n'.format(create_new_row(name, price)))
                except:
                    pass
                row = f.readline()

# Orchestrates the helper functions below to create a new row.
def create_new_row(name, price):
    first_name, last_name = split_name_into_first_and_last_name(name)
    price = remove_leading_zeros(price)
    is_above_100 = set_above_100(price)
    return ",".join([first_name, last_name, price, str(is_above_100)])

# Responsible for presentation of output header.
def get_output_header():
    return ",".join(["first_name", "last_name", "price", "above_100"])

# Split name helper
def split_name_into_first_and_last_name(name):
    name_chars = name.split()
    first_name = " ".join(name_chars[0:-1])
    last_name = name_chars[-1]
    return first_name, last_name


# Remove leading zeros from price helper
def remove_leading_zeros(price):
    return price.strip().lstrip("0")


# Check if price exceeds 100 helper
def set_above_100(price):
    return Decimal(price) > 100


process_dataset(argv[1], argv[2])
