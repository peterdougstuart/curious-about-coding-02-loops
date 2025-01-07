import pygame


class GameWindow:

    instance = None

    @classmethod
    def initialize(cls, screen_width, screen_height, bat_width, bat_height):
        if not cls.instance:
            cls.instance = cls(screen_width, screen_height, bat_width, bat_height)

    @classmethod
    def has_quit(cls):
        if not cls.instance:
            raise ValueError("GameWindow not initialized")
        return cls.instance._has_quit()

    @classmethod
    def get_keys_pressed(cls):
        if not cls.instance:
            raise ValueError("GameWindow not initialized")
        return cls.instance._get_keys_pressed()

    @classmethod
    def check_collision(cls, left_bat_y, right_bat_y, ball_x, ball_y):
        if not cls.instance:
            raise ValueError("GameWindow not initialized")
        return cls.instance._check_collision(left_bat_y, right_bat_y, ball_x, ball_y)

    @classmethod
    def draw_game(cls, left_bat_y, right_bat_y, ball_x, ball_y):
        if not cls.instance:
            raise ValueError("GameWindow not initialized")
        cls.instance._draw_game(left_bat_y, right_bat_y, ball_x, ball_y)

    @classmethod
    def pause(cls):
        if not cls.instance:
            raise ValueError("GameWindow not initialized")
        cls.instance._pause()

    @classmethod
    def quit(cls):
        if not cls.instance:
            raise ValueError("GameWindow not initialized")
        cls.instance._quit()

    def __init__(self, screen_width, screen_height, bat_width, bat_height):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.bat_width = bat_width
        self.bat_height = bat_height

        # Initialize screen
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Two-Player Pong")
        self.background_color = (0, 0, 0)
        self.ball_color = (255, 255, 255)
        self.bat_color = (255, 255, 255)

        # Game state
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.quit_game = False

    def _has_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game = True
        return self.quit_game

    def _get_keys_pressed(self):
        keys = pygame.key.get_pressed()
        up_press = keys[pygame.K_UP]
        down_press = keys[pygame.K_DOWN]
        w_press = keys[pygame.K_w]
        s_press = keys[pygame.K_s]
        return up_press, down_press, w_press, s_press

    def _check_collision(self, left_bat_y, right_bat_y, ball_x, ball_y):

        # Check collision with top and bottom walls
        if ball_y - 10 <= 0:
            return "top_wall"
        if ball_y + 10 >= self.screen_height:
            return "bottom_wall"

        # Check collision with left bat
        if (
            ball_x - 20 <= self.bat_width
            and left_bat_y <= ball_y <= left_bat_y + self.bat_height
        ):
            return "left_bat"

        # Check collision with right bat
        if (
            ball_x + 20 >= self.screen_width - self.bat_width
            and right_bat_y <= ball_y <= right_bat_y + self.bat_height
        ):
            return "right_bat"

        # Check if ball goes out of bounds
        if ball_x < 0 or ball_x > self.screen_width:
            return "game_over"

        return None

    def _draw_game(self, left_bat_y, right_bat_y, ball_x, ball_y):
        self.screen.fill(self.background_color)

        # Draw left bat
        pygame.draw.rect(
            self.screen,
            self.bat_color,
            (10, left_bat_y, self.bat_width, self.bat_height),
        )

        # Draw right bat
        pygame.draw.rect(
            self.screen,
            self.bat_color,
            (
                self.screen_width - 10 - self.bat_width,
                right_bat_y,
                self.bat_width,
                self.bat_height,
            ),
        )

        # Draw ball
        pygame.draw.circle(self.screen, self.ball_color, (ball_x, ball_y), 10)

        pygame.display.flip()

    def _pause(self):
        self.clock.tick(self.fps)

    def _quit(self):
        pygame.quit()
