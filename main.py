import time
import curses
import asyncio
import random

TIC_TIMEOUT = 0.1


def stars_generator(y, x, value=50):
    for star in range(value):
        column = random.randint(1, y-2)
        raw = random.randint(1, x-2)
        yield column, raw


def draw(canvas):
    canvas.border()
    curses.curs_set(False)
    y, x = canvas.getmaxyx()

    coroutines = [blink(canvas, raw, column) for column, raw in stars_generator(y, x)]
    while True:
        for coroutine in coroutines:
            coroutine.send(None)
            canvas.refresh()
        time.sleep(TIC_TIMEOUT)


async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        for tic in range(20):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for tic in range(3):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for tic in range(5):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for tic in range(3):
            await asyncio.sleep(0)


if __name__ == '__main__':
    curses.wrapper(draw)
    curses.update_lines_cols()

