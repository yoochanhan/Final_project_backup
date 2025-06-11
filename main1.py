#!/usr/bin/env python 3

"""
Created by: Yoochan Han
Created on: Jun 2025
This program is the "Space Aliens" program on the PyBadge
"""

import constants
import stage
import ugame


def game_scene() -> None:
    """This function is the main game game_scene"""

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("pew.wav", "rb")
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    # set the background to image 0 in the image bank
    #  and the size ( 10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    # a sprite that will be updated every frame
    ship = stage.Sprite(
        image_bank_background, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    alien = stage.Sprite(
        image_bank_sprites,
        9,int(constants.SCREEN_GRID_X / 2 - constants.SPRITE_SIZE / 2),
        16,
    )
    # create a stage for the background to show up on
    #  and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)

    # set the layers of all sprites, item show up in order
    game.layers = [ship] + [alien] + [background]

    # render all sprites
    #  most likely u will only render the bg once per game scn
    game.render_block()

    #  loop
    while True:
        # get user input
        key = ugame.buttons.get_pressed()
        
        if key & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["buttom_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        if key & ugame.K_O != 0:
            if b_button == constants.button_state["button_up"]:
                b_button = constants.button_state["button_just_pressed"]
            elif b_button == constants.button_state["buttom_just_pressed"]:
                b_button = constants.button_state["button_still_pressed"]
        else:
            if b_button == constants.button_state["button_still_pressed"]:
                b_button = constants.button_state["button_released"]
            else:
                b_button = constants.button_state["button_up"]
        if key & ugame.K_START:
            print("Start")
        if key & ugame.K_SELECT:
            print("Select")
        if key & ugame.K_RIGHT != 0:
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move((constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)
        if key & ugame.K_RIGHT != 0:
            if ship.x > 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(0, ship.y)
        if key & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
        if key & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)
        # update logic
        # play sound if A was just button_just_pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # redraw Sprite
        game.render_sprites([ship] + [alien])
        game.tick()  # wait until refresh rate finishes

game_scene()
