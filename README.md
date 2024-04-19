# challenger-dev-python

# Traffic Offenses Registration Project

This project implements a traffic offenses registration system in Python using the Django framework. The system consists of an administrative interface for managing persons, vehicles, and officers, as well as an API that allows an application used by police officers to upload offenses for vehicles.

## Installation

1. Clone this repository:

    ```
    git clone https://github.com/felixsuarez0727/challenger-dev-python.git
    ```

2. Create and activate a virtual environment:

    ```
    python -m venv challenger-dev-venv
    source challenger-dev-venv/bin/activate
    ```

3. Install the project dependencies:

    ```
    pip install -r requirements.txt
    ```

## Running the Project

1. Activate your virtual environment if you haven't already:

    ```
    source challenger-dev-venv/bin/activate
    ```

2. Navigate to the project directory:

    ```
    cd traffic-offences
    ```

3. Run the Django development server:

    ```
    python manage.py runserver
    ```

4. Access the administrative interface in your web browser:

    ```
    http://localhost:8000/admin
    ```

5. Enter the following credentials to access the administrative interface:

    - **Username:** superusertraffic
    - **Password:** superuserpass
