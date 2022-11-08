import asyncio
import itertools

from curses_tools import draw_frame, get_frame_size, read_controls


async def Animate_spaceship(
        canvas, frames, location_y=4, location_x=4, y_max=10, x_max=10):
    border_size = 1
    for frame in itertools.cycle(frames):
        ship_size_y, ship_size_x = get_frame_size(frame)
        ship_field_y_max = y_max - ship_size_y - border_size
        ship_field_x_max = x_max - ship_size_x - border_size

        displacement_y, displacement_x, _ = read_controls(canvas)

        location_y += displacement_y
        location_y = min(location_y, ship_field_y_max)
        location_y = max(location_y, border_size)
        location_x += displacement_x
        location_x = min(location_x, ship_field_x_max)
        location_x = max(location_x, border_size)

        draw_frame(canvas, location_y, location_x, frame)

        await asyncio.sleep(0)

        draw_frame(canvas, location_y, location_x, frame, negative=True)
