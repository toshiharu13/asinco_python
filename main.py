import pathlib
import time
import curses
import asyncio
import random

from space_ship_fly import get_ship_fly

TIC_TIMEOUT = 0.1


def get_frame_from_file(file):
    with open(file, 'r') as file:
        return file.read()


def stars_generator(width, height, value=50):
    for star in range(value):
        column = random.randint(1, width - 2)
        raw = random.randint(1, height - 2)
        symbol = random.choice(['+', '*', '.', ':'])
        yield column, raw, symbol


def draw(canvas):
    canvas.border()
    curses.curs_set(False)
    canvas.nodelay(True)
    height, width = canvas.getmaxyx()
    frame_1_path = pathlib.Path.cwd()/'frames'/'rocket_frame_1.txt'
    frame_2_path = pathlib.Path.cwd() / 'frames' / 'rocket_frame_2.txt'
    frame_1 = get_frame_from_file(frame_1_path)
    frame_2 = get_frame_from_file(frame_2_path)
    frames = (frame_1, frame_2)

    coroutines = [
        blink(canvas, raw, column, symbol, random.randint(0, 3)) for column, raw, symbol in stars_generator(width, height)
    ]
    # TODO add shutting func

    coroutines.append(
        get_ship_fly(canvas, frames, height / 2, width / 2, height, width))

    while True:
        for coroutine in coroutines:
            try:
                coroutine.send(None)
            except StopIteration:
                coroutines.remove(coroutine)
            canvas.refresh()
        if len(coroutines) == 0:
            break
        time.sleep(TIC_TIMEOUT)


def add_offset(count):
    if count >= 3:
        return 0
    return count + 1


async def blink(canvas, row, column, symbol='*', offset=0):
    while True:
        if offset == 0:
            canvas.addstr(row, column, symbol, curses.A_DIM)
            for tic in range(20):
                await asyncio.sleep(0)
            offset = add_offset(offset)
        if offset == 1:
            canvas.addstr(row, column, symbol)
            for tic in range(3):
                await asyncio.sleep(0)
            offset = add_offset(offset)
        if offset == 2:
            canvas.addstr(row, column, symbol, curses.A_BOLD)
            for tic in range(5):
                await asyncio.sleep(0)
            offset = add_offset(offset)
        if offset == 3:
            canvas.addstr(row, column, symbol)
            for tic in range(3):
                await asyncio.sleep(0)
            offset = add_offset(offset)


if __name__ == '__main__':
    curses.wrapper(draw)
    curses.update_lines_cols()
