import time

def progress_bar(part, total, lenght=30):
    frac = part / total
    completed  = int(frac * lenght)
    missing = lenght - completed

    bar = f"[{'#' * completed}{'-' * missing}]{frac:.2%}"
    return bar

n = 30

for i in range(n + 1):
    print( progress_bar(i, n, 35), end='\r' )
    time.sleep(0.2)