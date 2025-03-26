import csv
import pickle

# Load data from CSV file
def load_csv(file_name):
    data = []
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        pass
    return data

# Save data to CSV file
def save_csv(file_name, data, fieldnames):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Load preferences from binary file
def load_preferences(file_name):
    try:
        with open(file_name, 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return {}

# Save preferences to binary file
def save_preferences(file_name, data):
    with open(file_name, 'wb') as file:
        pickle.dump(data, file)

# Initialize data
customers = load_csv("customers.csv")
available_cars = load_csv("available_cars.csv")
purchased_cars = load_csv("purchased_cars.csv")
preferences = load_preferences("preferences.dat")

# Function to add default cars if no cars are present
def check_and_add_default_cars():
    if not available_cars:  # If the list is empty
        print("No cars found in the file. Adding default cars...")
        
        # Add default cars with diverse engine configurations (inline, V, and boxer) and prices
        default_cars = [
            # V engines
            {'name': 'BMW 7 Series', 'engine_name': 'BMW V8', 'cylinder_type': 'V', 'capacity': '4.4', 'torque': '500', 'transmission': 'automatic', 'power': '540', 'price': 86000},
            {'name': 'Rolls Royce Phantom', 'engine_name': 'Rolls Royce V12', 'cylinder_type': 'V', 'capacity': '6.75', 'torque': '900', 'transmission': 'automatic', 'power': '563', 'price': 450000},
            {'name': 'Mercedes-Benz S-Class', 'engine_name': 'Mercedes V8', 'cylinder_type': 'V', 'capacity': '4.0', 'torque': '700', 'transmission': 'automatic', 'power': '503', 'price': 110000},
            {'name': 'Audi A8', 'engine_name': 'Audi V8', 'cylinder_type': 'V', 'capacity': '3.0', 'torque': '600', 'transmission': 'automatic', 'power': '333', 'price': 86000},
            {'name': 'Porsche Panamera', 'engine_name': 'Porsche V6', 'cylinder_type': 'V', 'capacity': '2.9', 'torque': '450', 'transmission': 'automatic', 'power': '330', 'price': 89000},
            {'name': 'Lexus LS 500', 'engine_name': 'Lexus V8', 'cylinder_type': 'V', 'capacity': '3.5', 'torque': '500', 'transmission': 'automatic', 'power': '416', 'price': 76000},

            # Inline engines
            {'name': 'BMW 3 Series', 'engine_name': 'BMW Inline-6', 'cylinder_type': 'inline', 'capacity': '3.0', 'torque': '450', 'transmission': 'automatic', 'power': '382', 'price': 41000},
            {'name': 'Mercedes-Benz E-Class', 'engine_name': 'Mercedes Inline-6', 'cylinder_type': 'inline', 'capacity': '3.0', 'torque': '500', 'transmission': 'automatic', 'power': '362', 'price': 55000},
            {'name': 'Toyota Supra', 'engine_name': 'Toyota Inline-6', 'cylinder_type': 'inline', 'capacity': '3.0', 'torque': '500', 'transmission': 'automatic', 'power': '382', 'price': 51000},

            # Boxer engines
            {'name': 'Subaru WRX', 'engine_name': 'Subaru Boxer-4', 'cylinder_type': 'boxer', 'capacity': '2.0', 'torque': '350', 'transmission': 'manual', 'power': '268', 'price': 28000},
            {'name': 'Porsche 911 Carrera', 'engine_name': 'Porsche Boxer-6', 'cylinder_type': 'boxer', 'capacity': '3.0', 'torque': '450', 'transmission': 'automatic', 'power': '379', 'price': 101000},
        ]
        
        # Add the default cars to the available_cars list
        available_cars.extend(default_cars)

        # Save the updated list to the CSV file
        save_csv("available_cars.csv", available_cars, available_cars[0].keys())
        print("Default cars added successfully.")
        #this is just a test line to check if this keyboard is mechanical or

# Check and add default cars if no cars are found
if check_and_add_default_cars()==1:
    main_menu()
    
password=1122
# Function to display the main menu
def main_menu():
    while True:
        print("\nWelcome to Big Boy Cars!")
        print("1. Know about engine features")
        print("2. View all available cars")
        print("3. Search cars by preferences")
        print("4. Buy a car")
        print("5. Admin Menu")
        print("6. Register New Customer")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            display_engine_features()
        elif choice == '2':
            display_all_cars()
        elif choice == '3':
            search_cars_by_preferences()
        elif choice == '4':
            buy_car()
        elif choice == '5':
            g=3
            print("\nYou have only 3 attempts\n")
            for i in range (0,3):
                
                
                try:
                    a=int(input("Enter password  "))
                    if a==password:
                        print("\n\nHello admin\n")
                        admin_menu()
                    else:
                        g=g-1
                        if g>0:   
                            print("\nWrong password. Try again\n")
                            print("You have only",g,"attempts left!!\n")
                            
                except ValueError:
                    print("\nEnter numbers only\n")
                    continue
                    
            print("Too many attempts, Please try again later.\n")
            main_menu()
                
        elif choice == '6':
            add_customer()
        elif choice == '7':
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to display engine features
def display_engine_features():
    features = [
        "1. Cylinder Type: The cylinder is the central part of an engine where fuel is burned to power the vehicle. The type of cylinder arrangement can vary, with the most common configurations being inline, V, and flat or horizontally opposed. Inline engines have all cylinders arranged in a single line, V engines have cylinders arranged in two banks, and flat engines have cylinders arranged in two banks horizontally opposed to each other.",
        "2. Cylinder Capacity: Also known as engine displacement, cylinder capacity refers to the total volume of air and fuel that an engine can draw in and expel during one complete engine cycle. It is measured in cubic centimeters (cc) or liters (L) and is a crucial factor in determining an engine's power output.",
        "3. Torque: Torque is a measure of the rotational force produced by an engine. It is typically measured in foot-pounds (ft-lb) or Newton-meters (Nm) and is an important factor in determining an engine's acceleration and towing capabilities.",
        "4. Turbo: A turbocharger is a type of forced induction system that uses exhaust gases to spin a turbine, which in turn compresses air and forces it into the engine. This results in increased power output and improved fuel efficiency.",
        "5. Supercharger: A supercharger is another type of forced induction system that uses a belt or chain to drive a compressor, which in turn compresses air and forces it into the engine. Like a turbocharger, a supercharger increases power output and improves fuel efficiency.",
        "6. Transmission: The transmission is the component of a vehicle that transmits power from the engine to the wheels. It includes a clutch, gearbox, drive shaft, and differential and is responsible for adapting the engine's output to the speed and load requirements of the vehicle.",
        "7. Fuel Supply System: The fuel supply system is the component of an engine that delivers fuel to the cylinders. It includes the fuel tank, fuel pump, fuel filter, and fuel injectors and is responsible for ensuring a consistent and reliable supply of fuel to the engine.",
        "8. Power: Power is a measure of an engine's ability to do work over a given period of time. It is typically measured in horsepower (hp) or watts (W) and is a crucial factor in determining an engine's performance capabilities."
    ]
    for feature in features:
        print(feature,"\n")

# Function to display all cars
def display_all_cars():
    for car in available_cars:
        print("Vehicle Name:", car['name'])
        print("Engine Name:", car['engine_name'])
        print("Cylinder Type:", car['cylinder_type'])
        print("Capacity:", car['capacity'])
        print("Torque:", car['torque'])
        print("Transmission:", car['transmission'])
        print("Power:", car['power'])
        print("Price:", car['price'], "\n")
# Function to search cars by preferences
def search_cars_by_preferences():
    print("Enter your preferences for engine features:")
    cyl_type = input("Cylinder Type (inline, V, boxer): ")
    try:
        min_capacity = float(input("Minimum Capacity(eg. 2.0) (in liters): "))
        min_power = int(input("Minimum Power(eg. 250) (in HP): "))
        min_torque = int(input("Minimum Torque (eg. 250) (in Nm): "))
    except ValueError:
        print("Invalid input for numeric values. Please enter valid numbers.")
        return

    matching_cars = []

    for car in available_cars:
        try:
            # Ensuring the capacity, power, and torque are correctly parsed as numbers
            car_capacity = float(car['capacity'])
            car_power = int(car['power'])
            car_torque = int(car['torque'])

            # Compare based on preferences
            if car['cylinder_type'].lower() == cyl_type.lower() and \
               car_capacity >= min_capacity and \
               car_power >= min_power and \
               car_torque >= min_torque:
                matching_cars.append(car)
        except ValueError:
            print("Invalid value typed.")
            continue
        
    if not matching_cars:
        print("No cars found matching your preferences.")
    else:
        print("\nCars matching your preferences:\n")
        for car in matching_cars:
            print(f"Vehicle Name: {car['name']}")
            print(f"Engine Name: {car['engine_name']}")
            print(f"Cylinder Type: {car['cylinder_type']}")
            print(f"Capacity: {car['capacity']} L")
            print(f"Power: {car['power']} HP")
            print(f"Torque: {car['torque']} Nm\n")
# Function to buy a car
def buy_car():
    display_all_cars()
    car_name = input("Enter the name of the car you want to buy: ").strip()
    
    for car in available_cars:
        if car['name'].lower() == car_name.lower():
            g = input("Are you an existing customer? yes/no: ").strip().lower()
            
            customers = load_csv("customers.csv")  # Load customers
            customer_name = ""
            customer_email = ""
            customer_phone = ""
            existing_customer = False
            
            if g == 'yes':
                # Check if customer exists
                customer_name = input("Enter your name: ").strip()
                customer_email = input("Enter your email: ").strip()
                
                for customer in customers:
                    if customer['name'].lower() == customer_name.lower() and customer['email'].lower() == customer_email.lower():
                        print("Existing customer found.")
                        customer_phone = customer['contact']
                        existing_customer = True
                        break

                if not existing_customer:
                    print("Customer not found. Please try again or register as a new customer.")
                    return

            else:
                # Add new customer
                new_customer = {
                    'name': input("Enter customer name: ").strip(),
                    'contact': input("Enter contact number: ").strip(),
                    'email': input("Enter email address: ").strip()
                }
                customers.append(new_customer)
                save_csv("customers.csv", customers, customers[0].keys())
                print("Customer added successfully.")
                customer_name = new_customer['name']
                customer_phone = new_customer['contact']
                customer_email = new_customer['email']
            

            # Prepare purchase details
            purchase = {
                'customer_name': customer_name,
                'email': customer_email,
                'contact': customer_phone,
                'car_name': car['name'],
                'engine_name': car['engine_name'],
                'cylinder_type': car['cylinder_type'],
                'capacity': car['capacity'],
                'torque': car['torque'],
                'transmission': car['transmission'],
                'power': car['power'],
                'price': car['price']
            }
            
            # Confirm purchase
            amg = input(f"Do you really want to buy {car['name']} with price {car['price']}? yes/no: ").strip().lower()
            if amg == "yes":
                # Load purchased cars and append
                purchased_cars = load_csv("purchased_cars.csv")
                purchased_cars.append(purchase)
                save_csv("purchased_cars.csv", purchased_cars, purchase.keys())
                print(f"Thank you, {customer_name}! You have successfully purchased the {car['name']}.")
                available_cars.remove(car)
                save_csv("available_cars.csv", available_cars, available_cars[0].keys())
                print("An admin will contact you shortly for payment and delivery.")
                print("Returning to main menu...")
                main_menu()
            else:
                print("Cancelling purchase.")
                defg = input("Go back to main menu? yes/no: ").strip().lower()
                if defg == "yes":
                    main_menu()
                else:
                    print("Restarting the program...")
                    buy_car()
            return
    print("Car not found. Please try again.")

           
#Function to add new customers
def add_customer():
    customer = {
        'name': input("Enter customer name: "),
        'contact': input("Enter contact number: "),
        'email': input("Enter email address: ")
    }
    customers.append(customer)
    save_csv("customers.csv", customers, customers[0].keys())
    print("Customer added successfully.")
    
    # Admin menu for managing data
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. View all customers")
        print("2. Add new car")
        print("3. Update existing car")
        print("4. Add new customer")    
        print("5. Delete a customer")
        print("6. View sold cars")
        print("7. Delete a car")
        print("8. Back to main menu")

        choice1 = input("Enter your choice (1-8): ").strip()

        if choice1 == '1':
            view_customers()
        elif choice1 == '2':
            add_car()
        elif choice1 == '3':
            update_car()
        elif choice1 == '4':              
            add_customer()
        elif choice1 == '5':              
            delete_customer()
        elif choice1 == '6':
            view_purchases()
        elif choice1 == '7':
            delete_car()
        elif choice1 == '8':
            main_menu()
            break
        else:
            print("Invalid choice. Please try again.")

    
#Function to delete a customer
def delete_customer():
    customer_name = input("Enter the name of the customer to delete: ")
    for customer in customers:
        if customer['name'].lower() == customer_name.lower():
            customers.remove(customer)
            save_csv("customers.csv", customers, customers[0].keys())
            print("Customer deleted successfully.")
            return
    print("Customer not found.")
    
#Function to delete a car
def delete_car():
    display_all_cars()
    car_name = input("Enter the name of the car to delete: ")
    for car in available_cars:
        if car['name'].lower() == car_name.lower():
            available_cars.remove(car)
            save_csv("available_cars.csv", available_cars, available_cars[0].keys())
            print("Car deleted successfully.")
            return
    print("Car not found.")


#Function to view all customers
def view_customers():
    for customer in customers:
        print("Customer Name:", customer['name'])
        print("Contact:", customer['contact'])
        print("Email:", customer['email'], "\n")


#Function to add a new car
def add_car():
    car = {
        'name': input("Enter car name: "),
        'engine_name': input("Enter engine name: "),
        'cylinder_type': input("Enter cylinder type (inline, V, boxer): "),
        'capacity': input("Enter engine capacity (in liters): "),
        'torque': input("Enter torque (in Nm): "),
        'transmission': input("Enter transmission type: "),
        'power': input("Enter power (in HP): "),
        'price': input("Enter price in dollars: ")
    }
    available_cars.append(car)
    save_csv("available_cars.csv", available_cars, available_cars[0].keys())
    print("Car added successfully.")
    

#Function to update an existing car
def update_car():
    car_name = input("Enter the name of the car to update: ")
    for car in available_cars:
        if car['name'].lower() == car_name.lower():
            car['engine_name'] = input("Enter new engine name: ")
            car['cylinder_type'] = input("Enter new cylinder type: ")
            car['capacity'] = input("Enter new capacity: ")
            car['torque'] = input("Enter new torque: ")
            car['transmission'] = input("Enter new transmission: ")
            car['power'] = input("Enter new power: ")
            save_csv("available_cars.csv", available_cars, available_cars[0].keys())
            print("Car updated successfully.")
            customers = load_csv("customers.csv")
            return
    print("Car not found.")
    
# Function to view all purchased cars with details
def view_purchases():
    purchases = load_csv("purchased_cars.csv")  # Load purchases from the CSV file
    if not purchases:
        print("No purchases found.")
        return

    print("\nDetails of Purchased Cars:")
    for purchase in purchases:
        print("Customer Name:", purchase['customer_name'])
        print("Contact:", purchase['contact'])
        print("Email:", purchase['email'])
        print("Car Name:", purchase['car_name'])
        print("Engine Name:", purchase['engine_name'])
        print("Cylinder Type:", purchase['cylinder_type'])
        print("Capacity:", purchase['capacity'], "L")
        print("Torque:", purchase['torque'], "Nm")
        print("Transmission:", purchase['transmission'])
        print("Power:", purchase['power'], "HP")
        print("Price:", purchase['price'])
        print("-" * 40)
    
main_menu()
