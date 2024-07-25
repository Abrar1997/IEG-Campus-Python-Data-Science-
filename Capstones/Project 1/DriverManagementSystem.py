import datetime
import os

class Driver:
    # add email, license_class
    # format dates to be the same (%d %b %Y))
    def __init__(self, first_name, last_name, id_number, phone_number, license_expiry, status, email, license_class):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.phone_number = phone_number
        self.license_expiry = datetime.datetime.strptime(license_expiry, "%d-%b-%Y")
        self.status = status
        self.email = email
        self.license_class = license_class

    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.id_number},{self.phone_number},{self.license_expiry.strftime('%Y-%m-%d')},{self.status}"

class DriverDetails(Driver):
    # add email, license_class to super__init__
    # replace age with birth_date (format %d %b %Y)
    # add emergency_contact, blood_type, medical_condition
    def __init__(self, first_name, last_name, id_number, phone_number, license_expiry, status, age, gender, nationality, email, license_class):
        super().__init__(first_name, last_name, id_number, phone_number, license_expiry, status, email, license_class)
        self.age = age
        self.gender = gender
        self.nationality = nationality

    def __str__(self):
        return super().__str__() + f",{self.age},{self.gender},{self.nationality}"

class DriverAddress(Driver):
    # replace address attributes: house_number, street, postcode, state, city, country
    def __init__(self, first_name, last_name, id_number, phone_number, license_expiry, status, zipcode, state, city, house_number, street, postcode, country):
        super().__init__(first_name, last_name, id_number, phone_number, license_expiry, status)
        self.id_number = id_number
        self.zipcode = zipcode
        self.state = state
        self.city = city
        self.house_number = house_number
        self.street = street
        self.postcode = postcode
        self.country = country

    def __str__(self):
        return f"{self.id_number},{self.zipcode},{self.state},{self.city}"

class DriverSchedule:
    def __init__(self, id_number, start_time, end_time):
        self.id_number = id_number
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.id_number},{self.start_time},{self.end_time}"

class Registration:
    def __init__(self, drivers):
        self.drivers = drivers

    def register(self):
        # check if attributes same as class Driver
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        id_number = input("ID Number: ")
        phone_number = input("Phone Number: ")
        license_expiry = input("License Expiry Date (YYYY-MM-DD): ")
        status = input("Driver Status: ")
        email = input("Email Address: ")
        license_class = input("License Class: ")
        driver = Driver(first_name, last_name, id_number, phone_number, license_expiry, status, email, license_class)
        self.drivers.append(driver)
        with open('Drivers.txt', 'a') as file:
            file.write(str(driver) + '\n')

class UpdateDriverDetails:
    def __init__(self, drivers):
        self.drivers = drivers
    
    # check if attributes same as class DriverDetails
    # add option of which attribute to update
    # or enter if don't want to update (similar to filehandling.py example in class)
    # use try-except to print out error message if wrong input
    def update_driver_details(self):
        id_number = input("Enter ID Number to update details: ")
        age = input("Age: ")
        gender = input("Gender: ")
        nationality = input("Nationality: ")
        zipcode = input("Zipcode: ")
        state = input("State: ")
        city = input("City: ")

        for driver in self.drivers:
            if driver.id_number == id_number:
                driver_details = DriverDetails(driver.first_name, driver.last_name, driver.id_number, driver.phone_number, driver.license_expiry.strftime('%Y-%m-%d'), driver.status, age, gender, nationality)
                driver_address = DriverAddress(driver.id_number, zipcode, state, city)
                
                self.update_file('DriverDetails.txt', driver_details)
                self.update_file('DriverAddress.txt', driver_address)
                break
        else:
            print("Driver not found!")

    def update_file(self, filename, new_data):
        temp_file = f"temp_{filename}"
        updated = False
        if os.path.exists(filename):
            with open(filename, 'r') as file, open(temp_file, 'w') as temp:
                for line in file:
                    if line.startswith(new_data.id_number):
                        temp.write(str(new_data) + '\n')
                        updated = True
                    else:
                        temp.write(line)
        if not updated:
            with open(temp_file, 'a') as temp:
                temp.write(str(new_data) + '\n')
        os.replace(temp_file, filename)

# create class UpdateDriverAddress similar to UpdateDriverDetails

class Report:
    def report(self):
        print("Drivers Report:")
        with open('Drivers.txt', 'r') as file:
            for line in file:
                print(line.strip())
        
        print("\nDriver Details Report:")
        with open('DriverDetails.txt', 'r') as file:
            for line in file:
                print(line.strip())
        
        print("\nDriver Address Report:")
        with open('DriverAddress.txt', 'r') as file:
            for line in file:
                print(line.strip())
        
        print("\nDriver Schedule Report:")
        with open('DriverSchedules.txt', 'r') as file:
            for line in file:
                print(line.strip())

class DriverManagementSystem:
    def __init__(self):
        self.drivers = self.load_drivers()
        self.schedules = self.load_schedules()
        self.registration = Registration(self.drivers)
        self.update_driver_details_module = UpdateDriverDetails(self.drivers)
        self.report_module = Report()

    def load_drivers(self):
        drivers = []
        if os.path.exists('Drivers.txt'):
            with open('Drivers.txt', 'r') as file:
                for line in file:
                    first_name, last_name, id_number, phone_number, license_expiry, status = line.strip().split(',')
                    drivers.append(Driver(first_name, last_name, id_number, phone_number, license_expiry, status))
        return drivers

    def load_schedules(self):
        schedules = []
        if os.path.exists('DriverSchedules.txt'):
            with open('DriverSchedules.txt', 'r') as file:
                for line in file:
                    id_number, start_time, end_time = line.strip().split(',')
                    schedules.append(DriverSchedule(id_number, start_time, end_time))
        return schedules

    def alert_license_expiry(self):
        current_date = datetime.datetime.now()
        for driver in self.drivers:
            if (driver.license_expiry - current_date).days <= 90:
                print(f"Alert: Driver {driver.first_name} {driver.last_name}'s license is expiring soon on {driver.license_expiry.strftime('%Y-%m-%d')}")

    def driver_schedule(self):
        id_number = input("Enter Driver ID Number for schedule: ")
        for schedule in self.schedules:
            if schedule.id_number == id_number:
                print(f"Driver ID: {schedule.id_number}, Start Time: {schedule.start_time}, End Time: {schedule.end_time}")
                break
        else:
            print("Driver schedule not found!")

    def menu(self):
        while True:
            print("\nMenu:")
            print("0. Exit")
            print("1. Registration")
            print("2. Update Driver Details")
            print("3. Report")
            print("4. Alert for Driving License Expiry Date")
            print("5. Driver Schedule")
            choice = input("Enter your choice: ")

            if choice == '0':
                break
            elif choice == '1':
                self.registration.register()
            elif choice == '2':
                self.update_driver_details_module.update_driver_details()
            elif choice == '3':
                self.report_module.report()
            elif choice == '4':
                self.alert_license_expiry()
            elif choice == '5':
                self.driver_schedule()
            else:
                print("Invalid choice, please try again.")

system = DriverManagementSystem()
system.menu()

# try-except to print error message
# driver expiry date alert
# driver schedule
