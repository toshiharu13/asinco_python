import asyncio
import itertools
import pathlib

from curses_tools import draw_frame


async def ship_fly(canvas, frames, row=4, column=4):
    frames_cycle = itertools.cycle(frames)
    current_frame = next(frames_cycle)
    while True:
        draw_frame(canvas, row, column, current_frame)
        canvas.refresh()
        await asyncio.sleep(0)

        draw_frame(canvas, row, column, current_frame, negative=True)
        current_frame = next(frames_cycle)


