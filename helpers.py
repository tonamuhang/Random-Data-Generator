import random
import string

"""
Generate a random alphanumeric data.
Options:
L: Upper case letter
l: Lower case letter
C: A letter(either upper case or lower case)
d: A digit 1-9
D: A digit 0-9

Anything else will not change
Example parse_option(e) => 'e'
"""
def parse_option(char):
    if char == 'L':
        return random.choice(string.ascii_uppercase)
    elif char == 'l':
        return random.choice(string.ascii_lowercase)
    elif char == 'C':
        return random.choice(string.ascii_letters)
    elif char == 'd':
        return random.randint(1, 9)
    elif char == 'D':
        return random.randint(0, 9)
    elif char == '?':
        return random.choices([random.choice(string.ascii_letters), random.randint(0, 9)])[0]
    else:
        return char


def generate_alphanumeric(options, length=0):
    options = list(options)
    result = ""
    if len(options) == 1 and length == 0:
        length = random.randint(1, 8)
        for i in range(length):
            result += str(parse_option(options[0]))
        return result
    else:
        for i, c in enumerate(options):
            result += str(parse_option(c))

    return result


"""
Generate a random date type between the start date and the end date
Sample format: "2020-02-25"
"""
def generate_date(start=1996, end=2050):
    year = str(random.randint(start, end))
    month = random.randint(1, 12)
    day = random.randint(1, 30)

    month = f"{month:02d}"
    day = f"{day:02d}"

    return year+"-"+month+"-"+day


"""
Compare two dates
Return true if date 1 is earlier than date 2
"""
def compare_dates(date1, date2):
    date1 = date1.split("-")
    date2 = date2.split("-")


    for i in range(3):
        print(date1[i], " ", date2[i])
        if date1[i] == date2[i]:
            continue
        else:
            return date1[i] < date2[i]

"""
Generate a random email address given the host address
"""
def generate_email(host="mail.com", length=0):

    username = generate_alphanumeric("?", length)
    return username + "@" + host



"""
A wrapper that calls the corresponding generators
"""
def generate_data(*args, length=1, start=1996,
                  end=2050, host="mail.com", email_length=5,
                  alphanumeric="l", alphanumeric_len = 1, **kwargs,):

    alphanumeric_name = kwargs.get("alphanumeric_name", "")

    data_row = []
    for i in range(length):
        result = []
        for option in args:
            option = option.lower()
            if option == "date":
                result.append( {"date" : generate_date(start, end)} )
            elif option == "email":
                result.append( {"email" : generate_email(host, email_length)} )
            elif option == "alphanumeric":
                result.append({alphanumeric_name : generate_alphanumeric(alphanumeric, alphanumeric_len)})

        data_row.append(result)

    return data_row

