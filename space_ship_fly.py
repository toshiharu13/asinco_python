import curses
import asyncio
import time


def get_frame_from_file(file):
    with open(file, 'r') as file:
        return file.read()


async def ship_fly(canvas, row=4, column=4):
    frame_1 = get_frame_from_file('frames/rocket_frame_1.txt ')
    frame_2 = get_frame_from_file('frames/rocket_frame_2.txt ')


