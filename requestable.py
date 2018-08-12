'''
    File name: requestable.py
    Author: Adolfo Garza
    Date created: 08/11/2018
    Date last modified: 08/11/2018
    Python Version: 3.6
'''

from data_handler import DataHandler


class Requestable():
    def get_request_parameters(self):
        request_parameters = ['']
        return request_parameters

    def launch_sequence(self):
        request_queryparam_dictionary = {}
        request_parameters = self.get_request_parameters()
        for key in request_parameters:
            queryparam = input(f'insert {key}: ')
            request_queryparam_dictionary[key] = queryparam
        self.fetch_request(
                request_query_dictionary=request_queryparam_dictionary)

    def generate_request_form_data(self, request_query_dictionary):
        return request_query_dictionary

    def fetch_request(self, request_query_dictionary):
        form_data = self.generate_request_form_data(
                            request_query_dictionary=request_query_dictionary)
        DataHandler().fetch_request(
                    form_data=form_data,
                    request_type=self)

    def extract_array_from_wrapper(self, response):
        return response

    def extract_fieldnames_from_array(self, response_array):
        fieldnames = []
        for key, value in response_array[0].items():
            fieldnames.append(key)
        print(fieldnames)
        return fieldnames

    def print_dictionary(self, dictionary):
        print('\n')
        for key, value in dictionary.items():
            if value is not None:
                print(f'{key}: {value}')
