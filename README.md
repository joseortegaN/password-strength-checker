# Comprobador de Fortaleza de Contraseñas

Aplicación en Python con interfaz gráfica (tkinter) que evalúa la fortaleza de una contraseña en tiempo real y muestra una puntuación de 0 a 4, sumando un punto por cada uno de estos criterios:

1. Longitud mínima de 8 caracteres
2. Al menos una letra mayúscula
3. Al menos un dígito
4. Al menos un símbolo (carácter que no es letra ni número)

## Uso (sin instalar nada)

En la sección [Releases](../../releases) hay ejecutables listos para descargar en Windows, macOS y Linux — no necesitas tener Python instalado. Descarga el de tu sistema y ábrelo con doble clic:

- **Windows**: `ComprobadorContrasenas-windows.exe`
- **macOS**: `ComprobadorContrasenas-mac.zip` (descomprime y abre `ComprobadorContrasenas.app`)
- **Linux**: `ComprobadorContrasenas-linux.zip` (descomprime y ejecuta `ComprobadorContrasenas`)

> **Nota para macOS:** al abrir la app por primera vez, macOS avisará de que no puede verificar al desarrollador (normal para apps sin certificado de pago de Apple). Para abrirla: clic derecho (o Control+clic) sobre `ComprobadorContrasenas.app` → **Abrir** → confirmar **Abrir** en el aviso. Solo hace falta la primera vez.

## Uso desde el código fuente

Requiere Python 3 (tkinter viene incluido de serie en la mayoría de instalaciones):

```bash
python3 password_checker.py
```

En macOS también puedes abrir `Abrir Comprobador.command` con doble clic desde el Finder.

Se abrirá una ventana donde puedes escribir la contraseña. Mientras escribes, se actualizan en tiempo real la barra de progreso, el nivel de fortaleza y la lista de criterios cumplidos. Hay una casilla "Mostrar" para ver la contraseña en texto plano.

## Informe de revisión de código

Este repositorio incluye [`informe_revision_codigo.pdf`](informe_revision_codigo.pdf), un informe de revisión del código con observaciones sobre su funcionamiento y posibles mejoras.
