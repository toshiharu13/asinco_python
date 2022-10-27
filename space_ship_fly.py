import asyncio
import pathlib

from curses_tools import draw_frame


def get_frame_from_file(file):
    with open(file, 'r') as file:
        return file.read()


async def ship_fly(canvas, row=4, column=4):
    frame_1_path = pathlib.Path.cwd()/'frames'/'rocket_frame_1.txt'
    frame_2_path = pathlib.Path.cwd() / 'frames' / 'rocket_frame_2.txt'
    frame_1 = get_frame_from_file(frame_1_path)
    frame_2 = get_frame_from_file(frame_2_path)

    while True:
        draw_frame(canvas, row, column, frame_1)
        canvas.refresh()
        await asyncio.sleep(0)

        draw_frame(canvas, row, column, frame_1, negative=True)

        draw_frame(canvas, row, column, frame_2)
        canvas.refresh()
        await asyncio.sleep(0)


