"""This is an example settings.py file."""

# specify which of your DBs will hold the data created by pylytics
pylytics_db = "example"

# define all databases, sources of data and target repo for created data
DATABASES = {
    'example': {
        'host': 'localhost',
        'user': 'test',
        'passwd': 'test',
        'db': 'example',
    }
}
