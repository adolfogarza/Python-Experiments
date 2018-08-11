import requests

url = 'https://www.cedulaprofesional.sep.gob.mx/cedula/buscaCedulaJson.action'
headers = {'content-type': 'application/x-www-form-urlencoded'}


class RequestBot():

    def __init__(self, name, paternal_lastname, maternal_lastname):
        self.name = name
        self.paternal_lastname = paternal_lastname
        self.maternal_lastname = maternal_lastname

    def build_request_form_data(self):
        search_query = {
                "nombre": self.name,
                "paterno": self.paternal_lastname,
                "materno": self.maternal_lastname,
                "idCedula": ""
        }

        form_data = {'json': str(search_query)}
        return form_data

    def fetch_graduate_data(self):
        try:
            form_data = self.build_request_form_data()
            response = requests.post(
                url,
                data=form_data,
                headers=headers,
                timeout=2
                )

            graduateArray = response.json()['items']
            self.print_graduate_array(graduateArray=graduateArray)

        except requests.exceptions.Timeout:
            print('\nServer Busy: Try Again in 3 minutes\n')

    def print_graduate_array(self, graduateArray):
        for graduate in graduateArray:
            name = graduate['nombre']
            paternal_lastname = graduate['paterno']
            maternal_lastname = graduate['materno']
            university_major = graduate['titulo']
            university_name = graduate['desins']
            graduation_year = graduate['anioreg']
            graduation_code = graduate['idCedula']

            print('\n')
            print(f'Name: {name}')
            print(f'Surname: {paternal_lastname} {maternal_lastname}')
            print(f'University: {university_name}')
            print(f'Major: {university_major}')
            print(f'Graduation Year: {graduation_year}')
            print(f'Graduation Code (SEP Cedula): {graduation_code}')


def main():
    print("\n--------------------------------")
    print("Request Bot: Fetch Graduate Data")
    print("Coder: Adolfo Garza")
    print("--------------------------------\n")

    name = input('Graduate Name: ')
    paternal_lastname = input('Graduate Paternal Lastname: ')
    maternal_lastname = input('Graduate Maternal Lastname: ')

    robot = RequestBot(
                    name=name,
                    paternal_lastname=paternal_lastname,
                    maternal_lastname=maternal_lastname
                    )

    robot.fetch_graduate_data()


if __name__ == "__main__":
    main()
