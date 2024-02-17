import pygame
from config import *
from utils import Utils

class EndScreen():

    def __init__(self) -> None:
        self.hiscores_data = {}
        self.is_hiscore = False
        
        self.title_bar = None
        self.hiscores = None
        self.try_again = None

        self.width = 300
        self.section_gap = 10
        self.top_pos = UI_HEIGHT + self.section_gap + 20
        self.title_bar_height = 50
        self.hiscores_height = 200
        self.try_again_height = 50
        self.hiscore_textbg_height = 30
        self.hiscore_vpadding = 16
        self.hiscore_hpadding = 35

        self.try_again_rect = None

    def initialise(self) -> None:
        self.title_bar = pygame.Surface((self.width, self.title_bar_height))
        self.title_bar.fill(pygame.Color(UI_BG_COLOUR))
        self.hiscores = pygame.Surface((self.width, self.hiscores_height))
        self.hiscores.fill(pygame.Color(UI_BG_COLOUR))
        self.try_again = pygame.Surface((self.width, self.try_again_height))
        self.try_again.fill(pygame.Color(UI_BG_COLOUR))

        hiscoretext_bg_w = self.width - (self.hiscore_hpadding*2)
        hiscoretext_bg_h = self.hiscore_textbg_height
        self.hiscore_text_bg = pygame.Surface((hiscoretext_bg_w, hiscoretext_bg_h))
        self.hiscore_text_bg.fill(pygame.Color(TEXT_BG_COLOUR))
        
    def set_icons(self, icons) -> None:
        self.icons = icons

    def new_hiscore(self) -> None:
        self.is_hiscore = True

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
            if self.is_hiscore:
                subtitle_str = SUBTITLE_NEWHISCORE    
            else:            
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

        # hiscore panel - subtitle
        subtitle_str_text = font.render(subtitle_str, True, "white")
        subtitle_str_text_lp = hiscore_rect[0] + self.hiscore_hpadding
        subtitle_str_text_tp = hiscore_rect[1] + self.hiscore_vpadding
        
        screen.blit(subtitle_str_text, (subtitle_str_text_lp, subtitle_str_text_tp))

        # hiscore panel - hiscores
        utils = Utils()
        easy_hiscore = utils.milliseconds_to_display_text(self.hiscores_data[LEVEL_EASY])
        medium_hiscore = utils.milliseconds_to_display_text(self.hiscores_data[LEVEL_MEDIUM])
        hard_hiscore = utils.milliseconds_to_display_text(self.hiscores_data[LEVEL_HARD])
        
        text_bg_padding = 10
        easy_txt_rect = screen.blit(self.hiscore_text_bg, (hiscore_rect[0] + self.hiscore_hpadding, subtitle_str_text_tp + subtitle_str_text.get_height() + self.hiscore_vpadding))
        medium_txt_rect = screen.blit(self.hiscore_text_bg, (hiscore_rect[0] + self.hiscore_hpadding, easy_txt_rect.bottom + self.hiscore_vpadding))
        hard_txt_rect = screen.blit(self.hiscore_text_bg, (hiscore_rect[0] + self.hiscore_hpadding, medium_txt_rect.bottom + self.hiscore_vpadding))
        
        screen.blit(
            pygame.transform.smoothscale(self.icons[ICON_TIMER], (28,28)), (easy_txt_rect.centerx, easy_txt_rect.top))
        screen.blit(
            pygame.transform.smoothscale(self.icons[ICON_TIMER], (28,28)), (medium_txt_rect.centerx, medium_txt_rect.top))
        screen.blit(
            pygame.transform.smoothscale(self.icons[ICON_TIMER], (28,28)), (hard_txt_rect.centerx, hard_txt_rect.top))

        easy_text = font.render(LEVEL_EASY, True, "black")
        easy_hiscore_text = font.render(easy_hiscore, True, "black")
        medium_text = font.render(LEVEL_MEDIUM, True, "black")
        medium_hiscore_text = font.render(medium_hiscore, True, "black")
        hard_text = font.render(LEVEL_HARD, True, "black")
        hard_hiscore_text = font.render(hard_hiscore, True, "black")  

        easy_text_lp = easy_txt_rect.left + text_bg_padding
        easy_text_tp = easy_txt_rect.top + easy_text.get_height()/2
        easy_hiscore_text_lp = easy_txt_rect.right - easy_hiscore_text.get_width() - text_bg_padding
       
        medium_text_lp = medium_txt_rect.left + text_bg_padding
        medium_text_tp = medium_txt_rect.top + medium_text.get_height()/2
        medium_hiscore_text_lp = medium_txt_rect.right - medium_hiscore_text.get_width() - text_bg_padding
        
        hard_text_lp = hard_txt_rect.left + text_bg_padding
        hard_text_tp = hard_txt_rect.top + hard_text.get_height()/2
        hard_hiscore_text_lp = hard_txt_rect.right - hard_hiscore_text.get_width() - text_bg_padding
        
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
        collides = False
        if (self.try_again_rect.collidepoint(coords)):
            collides = True
            self.is_hiscore = False
        return collides

    def set_hiscores(self, hiscores) -> None:
        self.hiscores_data = hiscores