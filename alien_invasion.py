import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from pygame.sprite import Group
import game_functions as gf


def run_game():
    # 初始化游戏和设置并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个用于存储外星人的编组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            # 更新飞船位置
            ship.update()
            # 更新子弹位置,删除已消失的子弹
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            # 更新外星人位置
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            # 每次循环时都重绘屏幕并让屏幕可见
            gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets)


run_game()

