import requests

URL = 'https://rpachallenge.com/assets/downloadFiles/challenge.xlsx'
FILE_PATH = "output/challenge.xlsx"

def get_file()->str:
    response = requests.get(URL)
    
    with open(FILE_PATH, "wb") as file:
        file.write(response.content)
    
    return FILE_PATH
        
        
# def parse_data(payload: dict):
#     name = payload["Name"]
#     lname = payload["LastName"]
#     company_name = payload["CompanyName"]
#     role = payload["Role"]
#     address = payload["Address"]
#     email = payload["Email"]
#     phone = payload["Phone"]
#     return name, lname, company_name, role, address, email, phone