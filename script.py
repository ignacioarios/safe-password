import random
import string

def get_available_characters(include_uppercase, include_numbers, include_symbols):
    characters = string.ascii_lowercase  #minúsculas por defecto
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    return characters 

def generate_password(length, include_uppercase, include_numbers, include_symbols):
    characters = get_available_characters(include_uppercase, include_numbers, include_symbols)
    
    # Generamos contraseña aleatoria
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def ask_user_for_options():
    length = int(input("Ingrese la longitud de la contraseña: "))
    include_uppercase = input("¿Incluir letras mayúsculas? (s/n): ").lower() == 's'
    include_numbers = input("¿Incluir números? (s/n): ").lower() == 's'
    include_symbols = input("¿Incluir símbolos? (s/n): ").lower() == 's'
    
    return length, include_uppercase, include_numbers, include_symbols

def main():
    print("Bienvenido al generador de contraseñas seguras.")
    length, include_uppercase, include_numbers, include_symbols = ask_user_for_options()
    
    password = generate_password(length, include_uppercase, include_numbers, include_symbols)
    
    print(f"Tu contraseña segura es: {password}. Gracias por usar SafePasswor encoded by n.rivers <3")

if __name__ == "__main__":
    main()
