import time
import curses
import asyncio


def draw(canvas):
    canvas.border()
    curses.curs_set(False)
    row, column = (5, 20)
    coroutine = blink(canvas, row, column, '* * * * *')
    while True:
        coroutine.send(None)
        canvas.refresh()
        time.sleep(1)


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

    '''while True:
        try:
            coroutine.send(None)
            curses.update_lines_cols()
        except StopIteration:
            break'''


