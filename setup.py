from setuptools import setup, find_packages
import os

# Función para incluir los archivos de assets
def include_assets(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

# Lista de archivos de assets
assets_files = include_assets('assets')

setup(
    name='AstroDash',
    version='0.1',
    packages=find_packages(),
    package_data={
        '': assets_files,  # Incluye los archivos de assets
    },
    include_package_data=True,
    install_requires=[
        # Lista de dependencias si las tienes
    ],
    entry_points={
        'console_scripts': [
            'AstroDash=src.main:main',  # Punto de entrada de tu aplicación
        ],
    },
)