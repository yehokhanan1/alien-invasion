import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # inicializa o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Cria uma espaçonave
    ship = Ship(ai_settings, screen)
    # Cria um grupo no qual serão armazenados os projéteis
    bullets = Group()
    # grupo de alienigenas
    aliens = Group()

    # Cria a frota de alienigenas
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # define a cor de fundo
    bg_color = (230,230,230)

    # Cria um alienigena
    

    # Inicia o laço principal do jogo
    while True:
        # observa eventos de teclado e de mouse
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        
run_game()