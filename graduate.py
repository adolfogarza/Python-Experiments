'''
    File name: graduate.py
    Author: Adolfo Garza
    Date created: 08/11/2018
    Date last modified: 08/11/2018
    Python Version: 3.6
'''


class Graduate():
    url = 'https://www.cedulaprofesional.sep.gob.mx/cedula/buscaCedulaJson.action'
    filename = 'graduate_results.csv'
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

    @staticmethod
    def extract_from_wrapper(response):
        return response['items']

    @staticmethod
    def generate_request_form_data(name, paternal, maternal):
        search_query = {
                "nombre": name,
                "paterno": paternal,
                "materno": maternal,
                "idCedula": ""
        }
        form_data = {'json': str(search_query)}
        return form_data

    @staticmethod
    def fetch_request(name, paternal, maternal, request_mechanism):
        form_data = Graduate.generate_request_form_data(
                                        name=name,
                                        paternal=paternal,
                                        maternal=maternal)
        request_mechanism.fetch_request(
                    form_data=form_data,
                    request_type=Graduate)

    @staticmethod
    def launch_sequence(request_mechanism):
        name = input('Graduate Name: ')
        paternal = input('Graduate Paternal Lastname: ')
        maternal = input('Graduate Maternal Lastname: ')
        Graduate.fetch_request(
                    name=name,
                    paternal=paternal,
                    maternal=maternal,
                    request_mechanism=request_mechanism)
