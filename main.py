import time
import curses
import asyncio


def draw(canvas):
    canvas.border()
    curses.curs_set(False)
    row = 5
    coroutines = [blink(canvas, row, column, '*') for column in range(15, 40, 5)]
    while True:
        for coroutine in coroutines:
            coroutine.send(None)
            canvas.refresh()
        time.sleep(0.5)




async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)


if __name__ == '__main__':
    curses.wrapper(draw)
    curses.update_lines_cols()

