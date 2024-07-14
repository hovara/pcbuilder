from pyray import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400

game_name = 'pc_builder'
game_state = 'prototype'
game_version = 0.001


def main():
    init_window(WINDOW_WIDTH, WINDOW_HEIGHT, game_state + ' - ' + game_name + ' version: ' + str(game_version))
    set_target_fps(60)

    camera = Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0) 
    while not window_should_close():
        update_camera(camera, CAMERA_ORBITAL)
        begin_drawing()
        clear_background(RAYWHITE)
        begin_mode_3d(camera)
        draw_grid(20, 1.0)
        end_mode_3d()
        draw_text('Journey begins!', int(WINDOW_WIDTH / 2), int(WINDOW_HEIGHT / 2), 20, VIOLET)
        end_drawing()
        
if __name__ == "__main__":
    main()