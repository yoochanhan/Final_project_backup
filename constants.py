#!/usr/bin/env python 3

"""
Created by: Yoochan Han
Created on: Jun 2025
This program is the "Space Aliens" program on the PyBadge
"""

# Pybadge screen size is 160x128 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ALIENS = 5
FPS = 60
SPRITE_MOVEMENT_SPEED = 1

# Using forbutton state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released",
}
# pallets for filled text
WHITE_BLACK_PALETTE = (
    b"\xf8\x1f\x00\x00\xcey\xff\xff\xf8\x1f\x00\x19\xfc\xe0\xfd\xe0"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
)
RED_PALETTE = (
    b"\xff\xff\x00\x00\xcey\x66\xff\xff\xff\xff\xff\xff\xff\xfd\xe0"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
)
BLUE_PALETTE = (
    b"\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff"
    b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
)