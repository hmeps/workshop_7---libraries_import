import requests 
import json 
BASE_URL = "https://jsonplaceholder.typicode.com/users/"

def get_user_info(user_id):
    response = requests.get(BASE_URL + str(user_id)) 
    if response.status_code == 200: 
        return json.loads(response.text) 
    else: 
        print(f"Error: Unable to fetch user data (Status code: {response.status_code})") 
    return None

def display_user_info(user_data):
    print("=================")
    print("User Information:")
    print("=============================================================================================================================================================")
    print(f"Name: {user_data['name']}   |")
    print(f"Username: {user_data['username']}   |")
    print(F"Address Details: {user_data['address']} |")
    print(F"Phone Number: {user_data['phone']}  |")
    print(F"Website: {user_data['website']} |")
    print(F"Company Details: {user_data['company']} |")
    print("=============================================================================================================================================================")

def main():
    while True: 
        print("=======================================")
        user_id = input("Enter a user ID (1-10) or 'q' to quit: ")
        if user_id.lower() == 'q': 
            break
        try: 
            user_id = int(user_id) 
            if 1 <= user_id <= 10: 
                user_data = get_user_info(user_id) 
            if user_data: 
                display_user_info(user_data) 
            else: 
                print("Please enter a valid user ID between 1 and 10.") 
        except ValueError: 
            print("Please enter a valid number or 'q' to quit.")
main()