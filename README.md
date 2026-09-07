# Comprobador de Fortaleza de Contraseñas

Aplicación en Python con interfaz gráfica (tkinter) que evalúa la fortaleza de una contraseña en tiempo real y muestra una puntuación de 0 a 4, sumando un punto por cada uno de estos criterios:

1. Longitud mínima de 8 caracteres
2. Al menos una letra mayúscula
3. Al menos un dígito
4. Al menos un símbolo (carácter que no es letra ni número)

## Requisitos

- Python 3 instalado (tkinter viene incluido de serie en la mayoría de instalaciones)

## Uso

```bash
python3 password_checker.py
```

Se abrirá una ventana donde puedes escribir la contraseña. Mientras escribes, se actualizan en tiempo real la barra de progreso, el nivel de fortaleza y la lista de criterios cumplidos. Hay una casilla "Mostrar" para ver la contraseña en texto plano.

## Informe de revisión de código

Este repositorio incluye [`informe_revision_codigo.pdf`](informe_revision_codigo.pdf), un informe de revisión del código con observaciones sobre su funcionamiento y posibles mejoras.
