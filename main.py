#!/usr/bin/env python 3

"""
Created by: Yoochan Han
Created on: Jun 2025
This program is the "Space Aliens" program on the PyBadge
"""

import stage
import ugame


def game_scene() -> None:
    """This function is the main game game_scene"""

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # set the background to image 0 in the image bank
    #  and the size ( 10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    # a sprite that will be updated every frame
    ship = stage.Sprite(image_bank_background, 10, 8)

    # create a stage for the background to show up on
    #  and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)

    # set the layers of all sprites, item show up in order
    game.layers = [] + [background]

    # render all sprites
    #  most likely u will only render the bg once per game scn
    game.render_block()

    #  loop
    while True:
        # get user input

        # update logic

        # redraw Sprite
        game.render_sprites([ship])
        game.tick()  # wait until refresh rate finishes

if __name__ == "__main__":
    game_scene
