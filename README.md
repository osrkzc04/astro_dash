# AstroDash 🚀🌑

<div style="text-align:center">
    <img src="./assets/img/astro_dash_logo.png" alt="AstroDash" style="width:50%;"/>
</div>

Este proyecto es un videojuego desarrollado en Python utilizando las librerías `pygame` y `random`. El juego cuenta con sus propios assets (imágenes, sonidos, fuentes, etc.) y está diseñado para ser fácilmente modificable y extensible. A continuación, se detalla la estructura del proyecto, las características principales y cómo puedes contribuir o extender el juego.

## Características del Proyecto

- **Desarrollado en Python**: El juego está escrito en Python, lo que lo hace accesible para desarrolladores de todos los niveles.
- **Uso de Pygame**: Se utiliza la librería `pygame` para manejar gráficos, sonidos y eventos de entrada.
- **Generación Aleatoria**: La librería `random` se emplea para generar elementos aleatorios en el juego, como la posición de los enemigos o los power-ups.
- **Assets Personalizados**: El juego incluye sus propios assets (imágenes, sonidos, fuentes) que pueden ser modificados o reemplazados fácilmente.
- **Modificable y Extensible**: El código está organizado de manera que permite la adición de nuevas características, niveles, personajes, etc.

## Requisitos del Sistema

Para ejecutar este proyecto, necesitarás:

- Python 3.x instalado en tu sistema.
- La librería `pygame` instalada. Puedes instalarla usando pip:

  ```bash
  pip install pygame

  ```
## Cómo Ejecutar el Proyecto
<IfModule mod_rewrite.c>  
  RewriteEngine On  
  RewriteBase /  
  RewriteRule ^index\.html$ - [L]  
  RewriteCond %{REQUEST_FILENAME} !-f  
  RewriteCond %{REQUEST_FILENAME} !-d  
  RewriteRule . /index.html [L]  
</IfModule>
1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/osrkzc04/astro_dash.git

    ```
2. Navega al directorio del proyecto:

    ```bash
    cd astro_dash
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```
3. Ejecuta el juego:

    ```bash
    python src/main.py
    ```
## Vista Previa
<image src="./assets/preview/menu.png" alt="Menu Inicio">
<image src="./assets/preview/game.png" alt="Juego">
<image src="./assets/preview/game_over.png" alt="Juego Terminado">
