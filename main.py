import time
import curses
import asyncio

TIC_TIMEOUT = 0.1


def draw(canvas):
    canvas.border()
    curses.curs_set(False)
    row = 5
    coroutines = [blink(canvas, row, column, '*') for column in range(15, 40, 5)]
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

