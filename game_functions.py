import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def fire_bullets(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_key_down_events(ai_settings, screen, event, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        pygame.mixer.music.load('sounds/gunshot2.mp3')
        pygame.mixer.music.play()
        fire_bullets(ai_settings, screen, ship, bullets)
    elif event.key== pygame.K_q:
        sys.exit()

def check_key_up_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_play_button(ai_settings,screen, ship, bullets, aliens, stat, play_button, mouse_x, mouse_y, sb):
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stat.game_active:
        stat.game_active = True
        stat.reset_stat()
        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        pygame.mouse.set_visible(False)
        ai_settings.initialize_dynamic_settings()

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        

def check_events(ai_settings, screen, ship, bullets, aliens, stat, play_button, sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(ai_settings, screen, event, ship, bullets)
                
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen, ship, bullets, aliens, stat, play_button, mouse_x, mouse_y, sb)

def update_bullets(ai_settings, screen, ship, bullets, aliens, stat, sb):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens,stat, sb)

def check_high_score(stat, sb):
    if stat.score > stat.high_score:
        stat.high_score = stat.score
        sb.prep_high_score()

        with open('scores.txt', 'a') as obj:
            obj.write(' '+str(stat.score))

def check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens, stat, sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        pygame.mixer.music.load('sounds/explosion2.mp3')
        pygame.mixer.music.play()
        for alien in collisions.values():
            stat.score+=ai_settings.alien_points * len(alien)
            sb.prep_score()
        check_high_score(stat, sb)
    if len(aliens)==0:
        create_fleet(ai_settings, screen, ship, aliens)
        bullets.empty()
        ai_settings.increase_speed()
        stat.level+=1
        stat.ship_left = ai_settings.ship_limit
        sb.prep_level()
        sb.prep_ships()

def update_screen(ai_settings, screen, ship, bullets, aliens, stat, play_button, sb):

    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    sb.draw_scoreboard()
    sb.draw_level()
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    if stat.game_active==False:
        play_button.draw_button()
    pygame.display.flip()

def get_number_alien_x(ai_settings, screen):
    alien = Alien(ai_settings, screen)
    available_space_x = ai_settings.screen_width - 2*alien.rect.width
    number_alien_x = int(available_space_x / (2*alien.rect.width))
    return number_alien_x

def get_number_rows(ai_settings, screen, ship_height):
    alien = Alien(ai_settings, screen)
    available_space_y = ai_settings.screen_height - 3*alien.rect.height - ship_height;
    number_rows = int(available_space_y / (2*alien.rect.height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, number_row):
    alien = Alien(ai_settings, screen)
    alien.x = alien.rect.width + 2*alien.rect.width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*number_row
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    number_alien_x = get_number_alien_x(ai_settings, screen)
    number_rows = get_number_rows(ai_settings, screen, ship.rect.height)
    for number_row in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen, aliens, alien_number, number_row)

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges()==True:
            change_fleet_direction(ai_settings, aliens)
            break

def hit_ship(ai_settings, screen, ship, bullets, aliens, stat, sb):
    if stat.ship_left>0:
        stat.ship_left -= 1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        sleep(3)
    else:
        stat.game_active=False
        pygame.mouse.set_visible(True)
        

def check_aliens_bottom(ai_settings, screen, ship, bullets, aliens, stat, sb):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            hit_ship(ai_settings, screen, ship, bullets, aliens, stat, sb)
            break;
    
def update_aliens(ai_settings, screen, ship, bullets, aliens, stat, sb):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        hit_ship(ai_settings, screen, ship, bullets, aliens, stat, sb)
    check_aliens_bottom(ai_settings, screen, ship, bullets, aliens, stat, sb)
        
    













    








    
