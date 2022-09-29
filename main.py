import time
import curses
import asyncio


'''def draw(canvas):
    while True:
        canvas.border()
        curses.curs_set(False)
        row, column = (5, 20)

        canvas.addstr(row, column, '*', curses.A_DIM)
        canvas.refresh()
        time.sleep(2)

        canvas.addstr(row, column, '*')
        canvas.refresh()
        time.sleep(0.3)

        canvas.addstr(row, column, '*', curses.A_BOLD)
        canvas.refresh()
        time.sleep(0.5)

        canvas.addstr(row, column, '*')
        canvas.refresh()
        time.sleep(0.3)'''


async def draw(canvas, row=5, column=20, symbol='*'):
    canvas.border()
    curses.curs_set(False)
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        canvas.refresh()
        time.sleep(1)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        canvas.refresh()
        time.sleep(0.3)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        canvas.refresh()
        time.sleep(0.5)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        canvas.refresh()
        time.sleep(0.3)
        await asyncio.sleep(0)


if __name__ == '__main__':
    coroutine = curses.wrapper(draw)

    while True:
        try:
            coroutine.send(None)
            curses.update_lines_cols()
        except StopIteration:
            break


