def filter_phone_number(phone_number):
    """
     This method filters the phone number by adding the country code in front,
     it must be pure either starts with '0' or ''234' (with or without the country code(+234))
    """

    # print('phone received  in filter')
    if not phone_number:
        return ""

    elif phone_number[0:5] == "+2340":
        return filter_phone_number(phone_number[5:])

    elif phone_number[0:4] == "2340":
        return filter_phone_number(phone_number[4:])

    elif phone_number[0:4] == "+234":
        # print(phone_number)
        return phone_number

    elif phone_number[0:3] == "234":

        return filter_phone_number(phone_number[3:])

    elif phone_number[0] == "0":
        return filter_phone_number(phone_number[1:])

    else:
        phone_number = "+234" + phone_number
        # print(phone_number)
        return phone_number