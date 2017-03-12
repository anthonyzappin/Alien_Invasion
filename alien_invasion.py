import pygame
import game_functions as gf
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from bullet import Bullet
from button import Button
from scoreboard import Scoreboard

def run_game():

    #Initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make the Play Button
    play_button = Button(ai_settings, screen, "Play")

    #Make a ship
    ship = Ship(ai_settings, screen)

    #Make an alien ship
    alien = Alien(ai_settings, screen)

    #Make a group to store bullets and alien ships
    bullets = Group()
    aliens = Group()

    #Create a fleet of alien ships
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Create an instance of GameStats to store game statistis and create a Scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #Main loop for the game
    while True:

        #Watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            #Update ship movements
            ship.update()

            #Update bullets
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)

            #Update alien ships
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        #Delete bullets that have disappeared
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        #Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)

        ##Update aliens
        gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        #Update screen movements
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

        #Make the most recently drawn screen visible
        pygame.display.flip()


run_game()
