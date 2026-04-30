import time

time_now = time.time()
seconds_time = f"{time_now:,.4f}"
scientific_time = f"{time_now:.3e}"
print(f"Seconds since January 1, 1970: {seconds_time} or {scientific_time} in scientific notation")
print(time.ctime(time_now))