'''
    File name: request_bot.py
    Author: Adolfo Garza
    Date created: 08/11/2018
    Date last modified: 08/11/2018
    Python Version: 3.6

    Description: Responsible for handling the fetching of the data as well
    as the processing to a comma separated file document, it is capable of
    processing any requestable object.
'''

import requests
import csv
import os


class DataHandler():
    def fetch_request(self, form_data, request_type):
        try:
            response = requests.post(
                request_type.url,
                data=form_data,
                timeout=5).json()

            self.export_csv_document(
                    response=response,
                    request_type=request_type)

        except requests.exceptions.Timeout:
            print('\nServer Busy: Try Again in 3 minutes\n')

    def export_csv_document(self, response, request_type):
        with open(request_type.filename, 'w', newline='') as f:
            response_array = request_type.extract_array_from_wrapper(response)
            fieldnames = request_type.extract_fieldnames_from_array(
                                                response_array=response_array)
            writer_instance = csv.DictWriter(f, fieldnames=fieldnames)
            writer_instance.writeheader()

            for dictionary in response_array:
                writer_instance.writerow(dictionary)
                request_type.print_dictionary(dictionary=dictionary)

        print('\nexported document sucessfully')
        print(f'name: {request_type.filename}')
        print(f'found items: {len(response_array)}')
        print(f'location: {os.getcwd()}\n')
