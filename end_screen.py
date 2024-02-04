import pygame
from config import *
from utils import Utils

class EndScreen():

    def __init__(self) -> None:
        self.hiscores_data = {}
        self.width = 300
        self.section_gap = 10
        self.title_bar = None
        self.hiscores = None
        self.try_again = None
    
        self.top_pos = UI_HEIGHT + self.section_gap
        self.title_bar_height = 50
        self.hiscores_height = 200
        self.try_again_height = 50

        self.try_again_rect = None

    def initialise(self) -> None:
        self.title_bar = pygame.Surface((self.width, self.title_bar_height))
        self.title_bar.fill(pygame.Color(UI_BG_COLOUR))
        self.hiscores = pygame.Surface((self.width, self.hiscores_height))
        self.hiscores.fill(pygame.Color(UI_BG_COLOUR))
        self.try_again = pygame.Surface((self.width, self.try_again_height))
        self.try_again.fill(pygame.Color(UI_BG_COLOUR))

    def set_icons(self, icons) -> None:
        self.icons = icons

    def render(self, game_state) -> None:
        screen = pygame.display.get_surface()
        screen_width = pygame.display.get_window_size()[0]
        left_pos = screen_width / 2 - self.width / 2
        title_bar_rect = screen.blit(self.title_bar, (left_pos, self.top_pos))
        hiscore_rect = screen.blit(self.hiscores, (left_pos, self.top_pos+self.section_gap+self.title_bar_height))
        self.try_again_rect = screen.blit(self.try_again, 
                    (left_pos, self.top_pos+self.section_gap+self.title_bar_height+self.section_gap+self.hiscores_height))

        # text and icons
        font = pygame.font.SysFont(None, 24)
        if (game_state == GAME_STATE_GAMEOVER):
            title_str = TITLE_GAMEOVER
            subtitle_str = SUBTITLE_GAMEOVER
            title_icon = self.icons[ICON_MINE] # mine if you lose
        else:
            title_str = TITLE_YOUWIN
            subtitle_str = SUBTITLE_YOUWIN
            title_icon = self.icons[ICON_FLAG] # flag if you win

        # title bar
        title_icon_lp = left_pos + 10
        title_icon_tp = title_bar_rect[1]+ (self.title_bar_height/2 - 15)

        title_icon_rect = screen.blit(
            pygame.transform.smoothscale(title_icon, (30,30)), (title_icon_lp, title_icon_tp))
       
        title_txt = font.render(title_str, True, "white")
        title_text_left_pos = title_icon_rect[0] + 35
        title_text_top_pos = title_bar_rect[1]+ (self.title_bar_height/2 - title_txt.get_height()/2 + 2)
        
        screen.blit(title_txt, (title_text_left_pos, title_text_top_pos))

        # hiscores
        hiscore_vpadding = 20
        hiscore_hpadding = 35
        subtitle_str_text = font.render(subtitle_str, True, "white")
        subtitle_str_text_lp = hiscore_rect[0] + hiscore_hpadding
        subtitle_str_text_tp = hiscore_rect[1] + hiscore_vpadding
        
        screen.blit(subtitle_str_text, (subtitle_str_text_lp, subtitle_str_text_tp))

        utils = Utils()
        easy_hiscore = utils.milliseconds_to_display_text(self.hiscores_data[LEVEL_EASY])
        medium_hiscore = utils.milliseconds_to_display_text(self.hiscores_data[LEVEL_MEDIUM])
        hard_hiscore = utils.milliseconds_to_display_text(self.hiscores_data[LEVEL_HARD])

        easy_hiscore_text = font.render(easy_hiscore, True, "white")
        easy_text = font.render(LEVEL_EASY, True, "white")
        medium_hiscore_text = font.render(medium_hiscore, True, "white")
        medium_text = font.render(LEVEL_MEDIUM, True, "white")
        hard_hiscore_text = font.render(hard_hiscore, True, "white")
        hard_text = font.render(LEVEL_HARD, True, "white")

        easy_text_lp = hiscore_rect[0] + hiscore_hpadding
        easy_text_tp = subtitle_str_text_tp + subtitle_str_text.get_height() + hiscore_vpadding
        easy_hiscore_text_lp = easy_text_lp + easy_text.get_width() + hiscore_hpadding
       
        medium_text_lp = hiscore_rect[0] + hiscore_hpadding
        medium_text_tp = easy_text_tp + easy_text.get_height() + hiscore_vpadding
        medium_hiscore_text_lp = easy_text_lp + easy_text.get_width() + hiscore_hpadding
        
        hard_text_lp = hiscore_rect[0] + hiscore_hpadding
        hard_text_tp = medium_text_tp + medium_text.get_height() + hiscore_vpadding
        hard_hiscore_text_lp = hard_text_lp + hard_text.get_width() + hiscore_hpadding
        
        screen.blit(easy_text, (easy_text_lp, easy_text_tp))
        screen.blit(easy_hiscore_text, (easy_hiscore_text_lp, easy_text_tp))

        screen.blit(medium_text, (medium_text_lp, medium_text_tp))
        screen.blit(medium_hiscore_text, (medium_hiscore_text_lp, medium_text_tp))

        screen.blit(hard_text, (hard_text_lp, hard_text_tp))
        screen.blit(hard_hiscore_text, (hard_hiscore_text_lp, hard_text_tp))

        # try again button
        try_again_text = font.render(TRY_AGAIN, True, "white")
        try_again_lp = self.try_again_rect[0] + self.width / 2 - try_again_text.get_width() / 2 - 5
        try_again_tp = self.try_again_rect[1] + self.try_again_height / 2 - 5

        screen.blit(try_again_text, (try_again_lp, try_again_tp))
        if (self.try_again_rect.collidepoint(pygame.mouse.get_pos())):    
            self.try_again.fill(pygame.Color(TRY_AGAIN_HOVER))
        else:
            self.try_again.fill(pygame.Color(UI_BG_COLOUR))

    def try_again_clicked(self, coords) -> bool:
        return self.try_again_rect.collidepoint(coords)
    
    def set_hiscores(self, hiscores) -> None:
        self.hiscores_data = hiscores