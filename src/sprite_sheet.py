import pygame

class SpriteSheet:
    def __init__(self, filename):
        """Cargar la hoja de sprites desde un archivo."""
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()
    
    def get_image(self, x, y, width, height, scale=1):
        """Extraer un frame de la hoja de sprites y escalarlo."""
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
        """Inicializar la animación con una lista de frames y una duración por frame."""
        self.frames = frames
        self.frame_duration = frame_duration  # Duración de cada frame en milisegundos
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()
    
    def update(self):
        """Actualizar el frame actual de la animación."""
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_duration:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
    
    def get_current_frame(self):
        """Obtener el frame actual de la animación."""
        return self.frames[self.current_frame]