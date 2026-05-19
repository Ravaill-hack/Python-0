
import os


def find_width(len: int, logs_len: int) -> int:
    total_width = os.get_terminal_size()[0]
    line_width = total_width - logs_len
    if (line_width <= 0):
        line_width = 1
    return line_width


def progress_stamp(value: int) -> str:
    if (value < 10):
        progress_str = f"  {value}%"
    elif (value < 100):
        progress_str = f" {value}%"
    else:
        progress_str = f"{value}%"
    return (progress_str)


def line(i: int, total: int, width: int, ratio: int) -> str:
    full = int(width * ratio)
    empty = width - full
    line_str = '█' * full + '░' * empty
    return (line_str)


def time_stamp(i: int, total: int, start_time, max_width: int) -> str:
    current_time = os.times()[4]
    elapsed_time = current_time - start_time
    if (elapsed_time != 0):
        speed = i / elapsed_time
    else:
        speed = 0

    elapsed_min = int(elapsed_time) // 60
    min_str = "00"
    if (elapsed_min < 10 and elapsed_min != 0):
        min_str = f"0{elapsed_min:1d}"
    elif (elapsed_min != 0):
        min_str = f"{elapsed_min:2d}"

    elapsed_sec = (int(elapsed_time) % 60)
    sec_str = "00"
    if (elapsed_sec < 10 and elapsed_sec != 0):
        sec_str = f"0{elapsed_sec:1d}"
    elif (elapsed_sec != 0):
        sec_str = f"{elapsed_sec:2d}"

    raw_str = f"{i}/{total} [{min_str}:{sec_str}<00:00, {speed:.2f}it/s]"
    if (max_width != 1000):
        truncated_str = raw_str[0: max_width]
    else:
        truncated_str = raw_str
    return (truncated_str)


def ft_tqdm(lst: range) -> None:
    screen_width = os.get_terminal_size()[0]
    total = len(lst)
    start_time = os.times()[4]
    logs_len = len(f"100%|| {total}/{total} [00:00<00:00, 1000.00it/s]")
    max_width = 1000

    line_width = find_width(total, logs_len)
    if ((logs_len + 1) > screen_width):
        max_width = screen_width - line_width - 7

    for i, item in enumerate(lst, start=1):
        ratio = (i + 1) / total
        progress_value = int(ratio * 100)

        prog_str = progress_stamp(progress_value)
        line_str = line(i, total, line_width, ratio)
        time_stamp_str = time_stamp(i, total, start_time, max_width)

        print(f"\r{prog_str}|{line_str}| {time_stamp_str}", end="", flush=True)
        yield item
