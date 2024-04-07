# Hospital Management System

## Description
This project is a Hospital Management System developed using Django, a high-level Python web framework. The system provides different levels of access to users including President, Doctor, and Receptionist. 

- **President**: The president has the highest level of access and can add or delete doctors and patients.
- **Doctor**: Doctors can view patient data and update their details.
- **Receptionist**: Receptionists have permission to add patient data including their details.

## Features
- User authentication and authorization for different roles.
- CRUD (Create, Read, Update, Delete) operations for doctors and patients.
- Secure access control ensuring proper permissions for each user role.
- Responsive web design for better user experience across different devices.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yJoelhenry7/HospitalManagement
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Navigate to the project directory: 
   ```
   cd HospitalManagement
   ```
4. Apply database migrations:
   ```
   python manage.py migrate
   ```
5. Create a superuser (president account):
   ```
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage
1. Visit the website in your browser: [http://localhost:8000/](http://localhost:8000/)
2. Log in with your credentials based on your assigned role.
3. Depending on your role, you'll have different functionalities available:
   - **President**: Add or delete doctors and patients.
   - **Doctor**: View patient data and update their details.
   - **Receptionist**: Add patient data including their details.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Django Documentation: [https://docs.djangoproject.com/en/stable/](https://docs.djangoproject.com/en/stable/)
- Bootstrap Documentation: [https://getbootstrap.com/docs/](https://getbootstrap.com/docs/)
- Font Awesome: [https://fontawesome.com/](https://fontawesome.com/)


---
