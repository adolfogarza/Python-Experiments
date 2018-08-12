'''
    File name: graduate.py
    Author: Adolfo Garza
    Date created: 08/11/2018
    Date last modified: 08/11/2018
    Python Version: 3.6

    Description: Subclass that overrides traits where needed to consume web
    form sucessfully without having to deal with boilerplate code.
'''
from requestable import Requestable


class Graduate(Requestable):
    url = 'https://www.cedulaprofesional.sep.gob.mx/cedula/buscaCedulaJson.action'
    filename = 'graduate_results.csv'

    def get_request_parameters(self):
        request_parameters = ['nombre', 'paterno', 'materno', 'idCedula']
        return request_parameters

    def extract_array_from_wrapper(self, response):
        return response['items']

    def generate_request_form_data(self, request_query_dictionary):
        form_data = {'json': str(request_query_dictionary)}
        return form_data
