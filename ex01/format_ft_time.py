import time

time_now = time.time()
seconds_time = f"{time_now:,.4f}"
scientific_time = f"{time_now:.3e}"
text_bef = "Seconds since January 1, 1970: "
text_aft = " in scientific notation"
print(f"{text_bef}{seconds_time} or {scientific_time}{text_aft}")
print(time.ctime(time_now))
