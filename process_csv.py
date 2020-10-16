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


def create_new_row(name, price):
    first_name, last_name = split_name_into_first_and_last_name(name)
    price = remove_leading_zeros(price)
    is_above_100 = set_above_100(price)
    return ",".join([first_name, last_name, price, is_above_100])


def get_output_header():
    pass


def split_name_into_first_and_last_name(name):
    pass


def remove_leading_zeros(price):
    pass


def set_above_100(price):
    pass
