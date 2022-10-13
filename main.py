import time
import curses
import asyncio
import random

TIC_TIMEOUT = 0.1


def stars_generator(width, height, value=50):
    for star in range(value):
        column = random.randint(1, width - 2)
        raw = random.randint(1, height - 2)
        symbol = random.choice(['+', '*', '.', ':'])
        yield column, raw, symbol


def draw(canvas):
    canvas.border()
    curses.curs_set(False)
    height, width = canvas.getmaxyx()

    coroutines = [
        blink(canvas, raw, column, symbol, random.randint(0, 3)) for column, raw, symbol in stars_generator(width, height)
    ]
    shot_start_raw = height - 2
    shot_start_column = width / 2
    coroutines.append(fire(canvas, shot_start_raw, shot_start_column))

    while True:
        for coroutine in coroutines:
            coroutine.send(None)
            canvas.refresh()
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
            

async def fire(canvas, start_row, start_column, rows_speed=-0.3, columns_speed=0):
    """Display animation of gun shot, direction and speed can be specified."""

    row, column = start_row, start_column

    canvas.addstr(round(row), round(column), '*')
    await asyncio.sleep(0)

    canvas.addstr(round(row), round(column), 'O')
    await asyncio.sleep(0)
    canvas.addstr(round(row), round(column), ' ')

    row += rows_speed
    column += columns_speed

    symbol = '-' if columns_speed else '|'

    rows, columns = canvas.getmaxyx()
    max_row, max_column = rows - 1, columns - 1

    curses.beep()

    while 0 < row < max_row and 0 < column < max_column:
        canvas.addstr(round(row), round(column), symbol)
        await asyncio.sleep(0)
        canvas.addstr(round(row), round(column), ' ')
        row += rows_speed
        column += columns_speed


if __name__ == '__main__':
    curses.wrapper(draw)
    curses.update_lines_cols()

