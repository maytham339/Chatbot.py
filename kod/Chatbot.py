import csv
import os

# Constants for the CSV filename
CSV_FILE = 'users.csv'

# Function to load users from a CSV file
def load_users(filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        return {row['username']: row for row in reader}

# Function to save users to a CSV file
def save_users(filename, users):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'surname', 'username', 'password', 'personal_ID'])
        writer.writeheader()
        for user in users.values():
            writer.writerow(user)

# Function to create a new user account
def create_account(users):
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    personal_id = input("Enter your personal-id (10-num): ")
    password = input("Choose a password: ")
    user_number = 1
    for i in range(1, len(users) + 1):
        user_number = i + 1
    if len(users) < 10:
        username = name[0].lower() + surname[0].lower() + "00" + str(user_number)
    elif 10 <= len(users) < 100:
        username = name[0].lower() + surname[0].lower() + "0" + str(user_number)
    else:
        username = name[0].lower() + surname[0].lower() + str(user_number)
    users[username] = {'name': name,
                       'surname': surname,
                       'username': username,
                       'password': password,
                       'personal_ID': personal_id
                       }
    print(f"\n-> Account created. Your username is {username}")
    return users

# Login function
def login(users):
    username = input("Enter your username: ").lower()
    password = input("Enter your password: ")
    user = users.get(username)
    if user and user['password'] == password:
        print("\n-> Logged in successfully.")
        system_menu(user, users)  # Redirect to system menu after login
    else:
        print("\n-> Invalid username or password.")

def booking_time_options():
    time_1 = "1 Januari 2024, 13:00"
    time_2 = "3 Januari 2024, 10:00"
    time_3 = "11 Januari 2024, 12:00"
    print("\nAvailable times")
    print(20 * "-")
    print('1:', time_1)
    print('2:', time_2)
    print('3:', time_3)
    print(20 * "-")
    while True:
        patient_time_choice = int(input('Choose one of the following times (1, 2 or 3): '))
        right_time_choice = False
        if patient_time_choice == 1 or patient_time_choice == 2 or patient_time_choice == 3:
            right_time_choice = True
        if right_time_choice:
            if patient_time_choice == 1:
                return time_1
            elif patient_time_choice == 2:
                return time_2
            else:
                return time_3
        else:
            print('\n-> Try again, invalid time')
def book_appointment(user, users):
    print(f"\n{user['name']}, choose your doctor")
    print(20 * "-")
    doctor_1 = users.get(' as1999')
    doctor_2 = users.get(' tn1967')
    doctor_3 = users.get(' me1988')
    print('A:', doctor_1['name'], doctor_1['surname'])
    print('T:', doctor_2['name'], doctor_2['surname'])
    print('M:', doctor_3['name'], doctor_3['surname'])
    print(20 * "-")
    while True:
        patient_doctor_choice = input('Enter your doctor: ').upper()
        right_doctor_choice = False
        if patient_doctor_choice == 'A' or patient_doctor_choice == 'T' or patient_doctor_choice == 'M':
            right_doctor_choice = True
        if right_doctor_choice:
            appointment_date = booking_time_options()
            print('\n-> Your appointment is successfully booked!')
            print('\nBooking confirmation:')
            print(20 * "-")
            if patient_doctor_choice == 'A':
                print('The appointment is booked with doctor', doctor_1['name'], doctor_1['surname'])
            if patient_doctor_choice == 'T':
                print('The appointment is booked with doctor', doctor_2['name'], doctor_2['surname'])
            if patient_doctor_choice == 'M':
                print('The appointment is booked with doctor', doctor_3['name'], doctor_3['surname'])
            print('Booking date is:', appointment_date)
            input('\nPress enter to continue!')
            return
        else:
            print('\n-> Try again, invalid doctor')


# System menu after successful login
def system_menu(user, users):
    while True:
        print(f"\nWelcome, {user['name']}!")
        print(20 * "-")
        print("B - Book Appointment")
        print("L - Logout")
        print(20 * "-")
        choice = input("Choose an option: ").upper()
        if choice == 'B':
            book_appointment(user, users)
        elif choice == 'L':
            print("\n-> Logging out...")
            break
        else:
            print("\n-> Invalid option.")

# Main menu system
def main_menu():
    users = load_users(CSV_FILE)
    while True:
        print("\nChatbot Login")
        print(20*"-")
        print("L - Login")
        print("N - New account")
        print(20 * "-")
        choice = input("Choose an option: ").upper()
        if choice == 'L':
            login(users)
        elif choice == 'N':
            u = create_account(users)
            save_users(CSV_FILE, u)
        else:
            print("\n-> Invalid option.")

# Run the program
if __name__ == "__main__":
   main_menu()