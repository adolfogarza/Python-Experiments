# Python-Request-Bot
Python script that allows you to automate the process of fetching information from web forms. It allows you to visualize all of the captured entries and provides the ability to export the response array on a comma separated file.


## Usage Requirements:

* Have python 3.6 or higher.
* Install the python module called 'requests' locally.

## Custom Fetch Object Implementation:

* You must provide the Request URL of your form as follows:

```python
url = 'https://www.example.com/json.action'
```

* You must provide the desired filename title as follows:

```python
    filename = 'result-data.csv'
```

* Initialize your custom object with a dictionary:

```python
def __init__(self, dictionary):
    self.name = dictionary['name']
    self.paternal_lastname = dictionary['paternal_lastname']
```
