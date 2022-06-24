from datetime import datetime

# Fecha actual.
current_day = datetime.now()

def validate_age(): # validar la edad
    while True: 
        date_joined = input('Ingrese fecha "dd/mm/aaaa"...: ') 
        try: 
            date_modified = datetime.strptime(date_joined, '%d/%m/%Y')
            date_joined = date_modified.strftime('%d-%m-%Y') 
        except ValueError: 
            print("No ha ingresado una fecha correcta...")
        else: 
            return date_joined


def calculate_age(date): # calcular la edad
    date = datetime.strptime(date, '%d-%m-%Y')
    user_days = current_day - date
    years = user_days/365 # Obtener años del socio.
    return years.days