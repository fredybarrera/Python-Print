# Print Script

Script desarrollado en Python 3.8.17 y win32printing 0.1.3

## Propósito

Script para la impresión de documentos en formato PDF en impresora por defecto instalada en el equipo destino


## Instalación

Crear carpeta en disco "C" con nombre "Python"

Clonar proyecto desde GitHub, dentro de la unidad C:\Python
```bash
git clone https://github.com/fredybarrera/Python-Print.git
```

Se recomienda la instalación dentro de un entorno virtual de [miniconda](https://docs.conda.io/en/latest/miniconda.html).

Instalar miniconda en el sistema operativo y crear un entorno virtual con Python 3.8:
```bash
conda create -n nombre_entorno python==3.8
```
Activar al entorno virtual:
```bash
activate nombre_entorno 
```
Navegar hasta la ubicación del proyecto e instalar las dependencias:

```bash
pip install -r requirements.txt
```

### Configuracion .bat
Editar archivo "Run_Script.bat" y reemplazar la ruta de instalacion de miniconda y el nombre del entorno virtual creado

```bash
"C:\Users\Fredys Barrera\miniconda3\envs\test\python.exe" "C:\Python\main.py" %1 %2
```
