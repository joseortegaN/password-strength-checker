"""
EJEMPLO: solo el criterio de LONGITUD está hecho.
Tienes que añadir tú los otros tres: mayúscula, número y símbolo.
"""


def check_password(password: str) -> int:
    """
    Comprueba una contraseña y devuelve una puntuación de 0 a 4.
    Cada criterio que cumpla suma 1 punto.
    """
    puntos = 0

    # --- CRITERIO 1: longitud (ya hecho, como ejemplo) ---
    if len(password) >= 8:
        puntos += 1

    # --- CRITERIO 2: ¿tiene alguna mayúscula? ---
    for letra in password:
        if letra.isupper():
            puntos += 1
            break

    # --- CRITERIO 3: ¿tiene algún número? ---
    for letra in password:
        if letra.isdigit():
            puntos += 1
            break

    # --- CRITERIO 4: ¿tiene algún símbolo (no letra y no número)? ---
    for letra in password:
        if not letra.isalpha() and not letra.isdigit():
            puntos += 1
            break


    return puntos


if __name__ == "__main__":
    clave = input("Escribe una contraseña para comprobar: ")
    resultado = check_password(clave)
    print(f"Puntuación: {resultado}/4")
