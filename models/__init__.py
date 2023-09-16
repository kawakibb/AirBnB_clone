#!/usr/bin/python3
from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for the application
storage = FileStorage()
# Call reload() method on this variable to load objects from the JSON file
storage.reload()
