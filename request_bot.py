'''
    File name: request_bot.py
    Author: Adolfo Garza
    Date created: 08/11/2018
    Date last modified: 08/11/2018
    Python Version: 3.6
'''

import requests
import csv
import os

url = 'https://www.cedulaprofesional.sep.gob.mx/cedula/buscaCedulaJson.action'


class Graduate():
    column_names = ['nombre',
                    'paterno',
                    'materno',
                    'titulo',
                    'universidad',
                    'graduacion fecha',
                    'cedula sep']

    def __init__(self, dictionary):
        self.name = dictionary['nombre']
        self.paternal_lastname = dictionary['paterno']
        self.maternal_lastname = dictionary['materno']
        self.university_major = dictionary['titulo']
        self.university_name = dictionary['desins']
        self.graduation_year = dictionary['anioreg']
        self.graduation_code = dictionary['idCedula']

    def print_formatted(self):
        print(f'\nName: {self.name}')
        print(f'Paternal Lastname: {self.paternal_lastname}')
        print(f'Maternal Lastname: {self.maternal_lastname}')
        print(f'University: {self.university_name}')
        print(f'Major: {self.university_major}')
        print(f'Graduation Year: {self.graduation_year}')
        print(f'Graduation Code (SEP Cedula): {self.graduation_code}\n')

    def generate_csv_row(self):
        row = {
            'nombre': self.name,
            'paterno': self.paternal_lastname,
            'materno': self.maternal_lastname,
            'titulo': self.university_major,
            'universidad': self.university_name,
            'graduacion fecha': self.graduation_year,
            'cedula sep': self.graduation_code
        }
        return row


class RequestBot():

    def __init__(self, name, paternal, maternal, request_url):
        self.name = name
        self.paternal_lastname = paternal
        self.maternal_lastname = maternal
        self.url = request_url

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
                self.url,
                data=form_data,
                timeout=5)

            graduate_array = response.json()['items']
            self.export_csv_document(graduate_array=graduate_array)

        except requests.exceptions.Timeout:
            print('\nServer Busy: Try Again in 3 minutes\n')

    def export_csv_document(self, graduate_array):
        with open('graduate_results.csv', 'w', newline='') as f:
            column_names = Graduate.column_names
            writer_instance = csv.DictWriter(f, fieldnames=column_names)
            writer_instance.writeheader()

            for graduate_dictionary in graduate_array:
                graduate_instance = Graduate(dictionary=graduate_dictionary)
                row = graduate_instance.generate_csv_row()
                writer_instance.writerow(row)
                graduate_instance.print_formatted()

        print('\nexported document sucessfully')
        print('with name: graduate_results.csv')
        print(f'in location: {os.getcwd()}\n')


def main():
    print("\n--------------------------------")
    print("Request Bot: Fetch Graduate Data")
    print("Coder: Adolfo Garza")
    print("Last updated: August, 11, 2018")
    print("--------------------------------\n")

    name = input('Graduate Name: ')
    paternal_lastname = input('Graduate Paternal Lastname: ')
    maternal_lastname = input('Graduate Maternal Lastname: ')
    request_url = url

    robot = RequestBot(
                    name=name,
                    paternal=paternal_lastname,
                    maternal=maternal_lastname,
                    request_url=request_url)

    robot.fetch_graduate_data()


if __name__ == "__main__":
    main()
