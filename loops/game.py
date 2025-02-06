import pygame


class GameWindow:

    instance = None

    @classmethod
    def get(
        cls,
        screen_width,
        screen_height,
        bat_width,
        bat_height,
        background_color=(0, 0, 0),
        ball_color=(255, 255, 255),
        bat_color=(255, 255, 255),
    ):
        if not cls.instance:
            cls.instance = cls(
                screen_width,
                screen_height,
                bat_width,
                bat_height,
                background_color,
                ball_color,
                bat_color,
            )

        return cls.instance

    def __init__(
        self,
        screen_width,
        screen_height,
        bat_width,
        bat_height,
        background_color,
        ball_color,
        bat_color,
    ):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.bat_width = bat_width
        self.bat_height = bat_height

        # Initialize screen
        self.screen = pygame.display.set_mode(
            (
                self.screen_width,
                self.screen_height,
            )
        )

        pygame.display.set_caption("Two-Player Pong")
        self.background_color = background_color
        self.ball_color = ball_color
        self.bat_color = bat_color

        # Game state
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.quit_game = False

    def has_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game = True
        return self.quit_game

    def get_keys_pressed(self):
        keys = pygame.key.get_pressed()
        up_press = keys[pygame.K_UP]
        down_press = keys[pygame.K_DOWN]
        w_press = keys[pygame.K_w]
        s_press = keys[pygame.K_s]
        space_press = keys[pygame.K_SPACE]
        return up_press, down_press, w_press, s_press, space_press

    def check_collision(self, left_bat_y, right_bat_y, ball_x, ball_y):

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

        if ball_x > self.screen_width:
            return "left_score"

        if ball_x < 0:
            return "right_score"

        return None

    def draw_game(self, left_bat_y, right_bat_y, ball_x, ball_y, message):
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

        font = pygame.font.Font(None, 36)
        text = font.render(message, 1, (255, 255, 255))
        textpos = text.get_rect(centerx=self.screen.get_width() / 2)
        self.screen.blit(text, textpos)

        pygame.display.flip()

    def pause(self):
        self.clock.tick(self.fps)

    def quit(self):
        pygame.quit()
