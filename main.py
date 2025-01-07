from loops.game import GameWindow

# Initialize the game window
GameWindow.initialize(
    screen_width=800,
    screen_height=400,
    bat_width=10,
    bat_height=100,
)

running = True

bat_speed = 5

left_bat_y = 100
right_bat_y = 100

ball_x = 400
ball_y = 200

base_ball_speed_x = 4
base_ball_speed_y = 4

ball_speed_x = base_ball_speed_x
ball_speed_y = base_ball_speed_y

while running:

    if GameWindow.has_quit():
        running = False

    # Player 1 (left bat) uses W (up) and S (down) keys.
    # Player 2 (right bat) uses arrow keys (UP and DOWN).

    up_press, down_press, w_press, s_press = GameWindow.get_keys_pressed()

    # collision can be "top_wall", "bottom_wall", "left_bat", "right_bat", "game_over"

    collision = GameWindow.check_collision(
        left_bat_y=left_bat_y,
        right_bat_y=right_bat_y,
        ball_x=ball_x,
        ball_y=ball_y,
    )

    # Draw everything
    GameWindow.draw_game(
        left_bat_y=left_bat_y,
        right_bat_y=right_bat_y,
        ball_x=ball_x,
        ball_y=ball_y,
    )

    # ensure frame rate not too high
    GameWindow.pause()

GameWindow.quit()
