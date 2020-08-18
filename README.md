# Resulta Coding Exercise ##

## Overview ##

This project contains the solution for the Resulta coding challenge.  The application
reads start and end dates from the command line which are used as filters 
for the event details.

 ##  Project Layout ##
 
 ```
helpers 
  - Contains the helper classes used to process the API results
rest
   - Python files that contain the API endpoint calls
main.py
   - Entry point for the application
``` 

#### Python Version ####

This project was built and tested with Python 3.8, however, there should be no issues with a lower version.

## Setup ##

1. Ensure the prerequisites are installed
    ```
    - Python3.x
    - pip (tool for installing Python packages)
        - curl https://bootstrap.pypa.io/get-pip.py | python3.7
    ```

2. Create virtual env for python3 inside project directory:
    ```
    python3 -m venv venv 
    ```

3. Activate newly created environment
    ```
    . venv/bin/activate (Linux/OSX)
    venv\Scripts\activate.bat (Windows)
    ```

4. Install the required python packages
    ```
    pip install -r requirements.txt
    ```

## Run Project ##

Ensure that the API key is set as an environment variable
```
 export API_KEY=<API KEY> (Linux/OSX)
 set API_KEY=<API KEY> (Windows)
 ```

Run the application
 ```
 python3 main.py -sd <start_date> -ed <end_date>
 ```

NOTES:
* Dates must be in the format YYYY-MM-DD
* The results of the application will be displayed on the screen