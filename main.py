from loops.game import Game

# Initialize the game window
game = Game.get(
    screen_width=800,
    screen_height=400,
    bat_width=10,
    bat_height=100,
)

running = True

# initialise variables for speeds and positions

bat_speed = 5

left_bat_y = 100
right_bat_y = 100

ball_x = 400
ball_y = 200

ball_speed_x = 4
ball_speed_y = 4

right_bat_score = 0
left_bat_score = 0


while running:

    if game.has_quit():
        running = False

    # Player 1 (left bat) uses W (up) and S (down) keys.
    # Player 2 (right bat) uses arrow keys (UP and DOWN).

    up_press, down_press, w_press, s_press, space_press = game.get_keys_pressed()

    # Step 1 implement bat movement

    # Step 2 implement ball movements

    # Step 3 implement collision (update ball speed)

    # collision can be:
    # "top_wall",
    # "bottom_wall",
    # "left_bat",
    # "right_bat",
    # "left_score",
    # "right_score"

    collision = game.check_collision(
        left_bat_y=left_bat_y,
        right_bat_y=right_bat_y,
        ball_x=ball_x,
        ball_y=ball_y,
    )

    message = f"{left_bat_score}-{right_bat_score}"

    # Draw everything
    game.draw_game(
        left_bat_y=left_bat_y,
        right_bat_y=right_bat_y,
        ball_x=ball_x,
        ball_y=ball_y,
        message=message,
    )

    # ensure frame rate not too high
    game.pause()

game.quit()
