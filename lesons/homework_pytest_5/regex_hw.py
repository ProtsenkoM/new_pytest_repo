import re

my_string = "Place of delivery of goods or place of performance of work or provision of services: 82172, Ukraine, Lviv Region, Stebnyk, str. Doroshenko, 1 Deadline for delivery of goods, performance of works or provision of services: 31.12.2023"


if __name__ == '__main__':
    data = {
        'country': re.search(r'(?P<country>[A-Za-z]+),\s(?P<region>[A-Za-z\s]+)(?=\sRegion)', my_string).group('country'),
        'region': re.search(r'(?P<country>[A-Za-z]+),\s(?P<region>[A-Za-z\s]+)(?=\sRegion)', my_string).group('region'),
        'city': re.search(r'(?P<country>[A-Za-z\s]+),\s(?P<region>[A-Za-z\s]+),\s(?P<city>[A-Za-z\s]+)', my_string).group('city'),
        'postal': re.search(r'(?P<postal>[\d]+),', my_string).group('postal'),
        'address': re.search(r'(?P<address>str\. ([\w]+,\s\d))', my_string).group('address'),
        'deadline': re.search(r'(?P<deadline>[\d]+\.[\d]+\.[\d]+)', my_string).group('deadline'),
    }
    print(data)


