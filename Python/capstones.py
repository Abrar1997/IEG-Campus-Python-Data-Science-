# Contoh data

First Name, Last Name, ID, Email, License No, Passport, Contact, Origin Country, Birthday, Street, Post Code, City, Country
John, Doe, 123, john@example.com, L12345, P12345, 555-5555, USA, 1990-01-01, 123 Main St, 12345, Anytown, USA
Jane, Smith, 456, jane@example.com, L67890, P67890, 555-1234, USA, 1985-05-05, 456 Elm St, 67890, Othertown, USA

# contoh code


def read_driver_details(file_path):
    driver_details = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(', ')
        for line in lines[1:]:
            details = line.strip().split(', ')
            driver_details.append(dict(zip(headers, details)))
    return driver_details

def print_driver_report(driver_details):
    print(f"{'Driver Report':^100}")
    print("="*100)
    for i, driver in enumerate(driver_details, 1):
        print(f"Driver #{i}")
        for key, value in driver.items():
            print(f"{key}: {value}")
        print("-"*100)

def main():
    file_path = 'drivers.txt'
    driver_details = read_driver_details(file_path)
    print_driver_report(driver_details)

if __name__ == "__main__":
    main()
