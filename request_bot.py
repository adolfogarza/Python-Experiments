import requests
import csv
import os

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
                timeout=5
                )

            graduateArray = response.json()['items']
            self.export_csv_document(graduateArray=graduateArray)

        except requests.exceptions.Timeout:
            print('\nServer Busy: Try Again in 3 minutes\n')

    def export_csv_document(self, graduateArray):
        with open('graduate_results.csv', 'w', newline='') as f:
            column_names = ['nombre',
                            'paterno',
                            'materno',
                            'titulo',
                            'universidad',
                            'graduacion fecha',
                            'cedula sep']

            writer_instance = csv.DictWriter(f, fieldnames=column_names)
            writer_instance.writeheader()
            for graduate in graduateArray:
                graduate_dictionary = {
                    'nombre': graduate['nombre'],
                    'paterno': graduate['paterno'],
                    'materno': graduate['materno'],
                    'titulo': graduate['titulo'],
                    'universidad': graduate['desins'],
                    'graduacion fecha': graduate['anioreg'],
                    'cedula sep': graduate['idCedula']
                }

                writer_instance.writerow(graduate_dictionary)
                self.print_graduate_array(graduate=graduate)
        print('\nexported document sucessfully')
        print('with name: graduate_results.csv')
        print(f'in location: {os.getcwd()}\n')

    def print_graduate_array(self, graduate):
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
    print("Last updated: August, 11, 2018")
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
