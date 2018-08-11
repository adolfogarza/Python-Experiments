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


class RequestBot():

    @staticmethod
    def fetch_request(form_data, request_type):
        try:
            response = requests.post(
                request_type.url,
                data=form_data,
                timeout=5).json()
            RequestBot.export_csv_document(
                    response=response,
                    request_type=request_type)

        except requests.exceptions.Timeout:
            print('\nServer Busy: Try Again in 3 minutes\n')

    @staticmethod
    def export_csv_document(response, request_type):
        with open(request_type.filename, 'w', newline='') as f:
            column_names = request_type.column_names
            writer_instance = csv.DictWriter(f, fieldnames=column_names)
            writer_instance.writeheader()
            response_array = request_type.extract_from_wrapper(response)

            for dictionary in response_array:
                response_instance = request_type(dictionary=dictionary)
                row = response_instance.generate_csv_row()
                writer_instance.writerow(row)
                response_instance.print_formatted()

        print('\nexported document sucessfully')
        print(f'name: {request_type.filename}')
        print(f'found items: {len(response_array)}')
        print(f'location: {os.getcwd()}\n')
