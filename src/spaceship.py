import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (200, 200, 200)
AZUL = (0, 0, 255)
RED = (255, 0, 0)

# Fuente para los botones
fuente = pygame.font.Font(None, 25)

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Animación Escalada")

class SpriteSheet:
    def __init__(self, filename):
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()
    
    def get_image(self, x, y, width, height, scale=1):
        """Extraer un frame y escalarlo"""
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        
        # Escalar la imagen si es necesario
        if scale != 1:
            new_width = int(width * scale)
            new_height = int(height * scale)
            image = pygame.transform.scale(image, (new_width, new_height))
        
        return image

class Animacion:
    def __init__(self, frames, frame_duration=100):
        self.frames = frames
        self.frame_duration = frame_duration  # Duración de cada frame en milisegundos
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()
    
    def update(self):
        """Actualizar el frame actual de la animación"""
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_duration:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
    
    def get_current_frame(self):
        """Obtener el frame actual"""
        return self.frames[self.current_frame]

# Botones
class Boton:
    def __init__(self, x, y, ancho, alto, texto, color):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.texto = texto
        self.color = color
    
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, self.rect)
        texto_surface = fuente.render(self.texto, True, BLANCO)
        texto_rect = texto_surface.get_rect(center=self.rect.center)
        ventana.blit(texto_surface, texto_rect)
    
    def es_clic(self, pos):
        return self.rect.collidepoint(pos)


# Cargar la hoja de sprites (reemplaza 'spritesheet.png' con tu archivo)
sprite_sheet = SpriteSheet('./assets/img/spaceship_sprite.png')

# Extraer frames y escalarlos (ajusta coordenadas y dimensiones según tu sprite sheet)
escala = 7.0  # Escalar los frames al doble de su tamaño original
frames = [
    sprite_sheet.get_image(0, 0, 32, 32, escala),    # Frame 1
    sprite_sheet.get_image(32, 0, 32, 32, escala),   # Frame 2
    sprite_sheet.get_image(64, 0, 32, 32, escala),   # Frame 3
    sprite_sheet.get_image(96, 0, 32, 32, escala)    # Frame 4
]

# Crear botones de zoom
boton_zoom_in = Boton(50, 500, 100, 50, "Zoom In", RED)
boton_zoom_out = Boton(200, 500, 100, 50, "Zoom Out", RED)

# Crear animación
animacion = Animacion(frames, frame_duration=100)

# Posición del sprite
x_pos = ANCHO // 2 - frames[0].get_width() // 2
y_pos = ALTO // 2 - frames[0].get_height() // 2

# Reloj para controlar FPS
reloj = pygame.time.Clock()

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        # elif evento.type == pygame.MOUSEBUTTONDOWN:
        #     # Verificar si se hizo clic en los botones
        #     if boton_zoom_in.es_clic(evento.pos):
        #         escala *= 1.1  # Aumentar escala (zoom in)
        #         frames = [
        #             sprite_sheet.get_image(0, 0, 32, 32, escala),
        #             sprite_sheet.get_image(32, 0, 32, 32, escala),
        #             sprite_sheet.get_image(64, 0, 32, 32, escala),
        #             sprite_sheet.get_image(96, 0, 32, 32, escala)
        #         ]
        #         animacion = Animacion(frames, frame_duration=100)
        #     elif boton_zoom_out.es_clic(evento.pos):
        #         escala /= 1.1  # Reducir escala (zoom out)
        #         frames = [
        #             sprite_sheet.get_image(0, 0, 32, 32, escala),
        #             sprite_sheet.get_image(32, 0, 32, 32, escala),
        #             sprite_sheet.get_image(64, 0, 32, 32, escala),
        #             sprite_sheet.get_image(96, 0, 32, 32, escala)
        #         ]
        #         animacion = Animacion(frames, frame_duration=100)
    
    # Actualizar animación
    animacion.update()
    
    # # Limpiar pantalla
    # ventana.fill((30, 30, 30))
    
    # Dibujar frame actual
    frame_actual = animacion.get_current_frame()
    ventana.blit(frame_actual, (x_pos, y_pos))

    # # Dibujar botones
    # boton_zoom_in.dibujar(ventana)
    # boton_zoom_out.dibujar(ventana)

    
    # Actualizar pantalla
    pygame.display.flip()
    
    # Controlar FPS
    reloj.tick(60)

pygame.quit()
sys.exit()