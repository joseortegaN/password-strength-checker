"""
Comprobador de fortaleza de contraseñas con interfaz gráfica (tkinter).
"""

import tkinter as tk
from tkinter import ttk


def evaluar_password(password: str) -> dict:
    """
    Comprueba una contraseña y devuelve un diccionario con:
    - "criterios": qué criterios cumple (True/False)
    - "puntos": la puntuación total, de 0 a 4
    """
    criterios = {
        "Al menos 8 caracteres": len(password) >= 8,
        "Al menos una mayúscula": any(letra.isupper() for letra in password),
        "Al menos un número": any(letra.isdigit() for letra in password),
        "Al menos un símbolo": any(
            not letra.isalnum() and not letra.isspace() for letra in password
        ),
    }
    puntos = sum(criterios.values())
    return {"criterios": criterios, "puntos": puntos}


NIVELES = {
    0: ("Muy débil", "#d32f2f"),
    1: ("Muy débil", "#d32f2f"),
    2: ("Débil", "#f57c00"),
    3: ("Aceptable", "#fbc02d"),
    4: ("Fuerte", "#388e3c"),
}


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Comprobador de Contraseñas")
        self.resizable(False, False)
        self.configure(padx=20, pady=20)

        tk.Label(self, text="Introduce una contraseña:", font=("Arial", 11)).grid(
            row=0, column=0, columnspan=2, sticky="w"
        )

        self.mostrar = tk.BooleanVar(value=False)
        self.entrada = tk.Entry(self, width=30, show="*", font=("Arial", 11))
        self.entrada.grid(row=1, column=0, pady=(5, 10))
        self.entrada.bind("<KeyRelease>", lambda evento: self.actualizar())

        tk.Checkbutton(
            self, text="Mostrar", variable=self.mostrar, command=self.alternar_visibilidad
        ).grid(row=1, column=1, padx=(10, 0))

        self.barra = ttk.Progressbar(self, length=260, maximum=4)
        self.barra.grid(row=2, column=0, columnspan=2, pady=(0, 5))

        self.etiqueta_nivel = tk.Label(self, text="", font=("Arial", 12, "bold"))
        self.etiqueta_nivel.grid(row=3, column=0, columnspan=2, pady=(0, 10))

        self.etiquetas_criterios = {}
        criterios_iniciales = evaluar_password("")["criterios"]
        for i, nombre in enumerate(criterios_iniciales):
            etiqueta = tk.Label(
                self, text=f"✗ {nombre}", font=("Arial", 10), fg="#d32f2f", anchor="w"
            )
            etiqueta.grid(row=4 + i, column=0, columnspan=2, sticky="w")
            self.etiquetas_criterios[nombre] = etiqueta

        self.actualizar()

    def alternar_visibilidad(self):
        self.entrada.config(show="" if self.mostrar.get() else "*")

    def actualizar(self):
        password = self.entrada.get()
        resultado = evaluar_password(password)

        self.barra["value"] = resultado["puntos"]
        nivel, color = NIVELES[resultado["puntos"]]
        self.etiqueta_nivel.config(text=f"{nivel} ({resultado['puntos']}/4)", fg=color)

        for nombre, cumple in resultado["criterios"].items():
            etiqueta = self.etiquetas_criterios[nombre]
            if cumple:
                etiqueta.config(text=f"✓ {nombre}", fg="#388e3c")
            else:
                etiqueta.config(text=f"✗ {nombre}", fg="#d32f2f")


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
