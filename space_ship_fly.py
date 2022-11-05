import asyncio
import itertools

from curses_tools import draw_frame, read_controls, get_frame_size


async def get_ship_fly(
        canvas, frames, location_y=4, location_x=4, y_max=10, x_max=10):
    border_size = 1
    for current_frame in itertools.cycle(frames):
        ship_size_y, ship_size_x = get_frame_size(current_frame)
        ship_field_y_max = y_max - ship_size_y - border_size
        ship_field_x_max = x_max - ship_size_x - border_size
        ship_field_y_min, ship_field_x_min = border_size, border_size

        displacement_y, displacement_x, _ = read_controls(canvas)

        location_y += displacement_y
        location_y = min(location_y, ship_field_y_max)
        location_y = max(location_y, ship_field_y_min)
        location_x += displacement_x
        location_x = min(location_x, ship_field_x_max)
        location_x = max(location_x, ship_field_y_min)

        draw_frame(canvas, location_y, location_x, current_frame)

        #for tic in range(2):
        await asyncio.sleep(0)

        draw_frame(canvas, location_y, location_x, current_frame, negative=True)
