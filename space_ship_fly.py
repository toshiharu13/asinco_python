import asyncio
import itertools

from curses_tools import draw_frame, read_controls, get_frame_size


async def ship_fly(
        canvas, frames, location_y=4, location_x=4, y_max=10, x_max=10):
    frames_cycle = itertools.cycle(frames)
    current_frame = next(frames_cycle)
    ship_size_y, ship_size_x = get_frame_size(current_frame)
    ship_field_y_max = y_max - ship_size_y - 1
    ship_field_x_max = x_max - ship_size_x - 1
    ship_field_y_min, ship_field_x_min = 1, 1

    while True:
        displacement_y, displacement_x, _ = read_controls(canvas)

        location_y += displacement_y
        location_y = min(location_y, ship_field_y_max)
        location_y = max(location_y, ship_field_y_min)
        location_x += displacement_x
        location_x = min(location_x, ship_field_x_max)
        location_x = max(location_x, ship_field_y_min)

        draw_frame(canvas, location_y, location_x, current_frame)
        canvas.refresh()

        for tic in range(2):
            await asyncio.sleep(0)

        draw_frame(canvas, location_y, location_x, current_frame, negative=True)

        current_frame = next(frames_cycle)


