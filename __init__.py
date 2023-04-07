from datetime import datetime
import pandas as pd

def log(filename, message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)

    full_message = timestamp + ', ' + message

    with open(f'{filename}.log', 'a') as f:
        f.write(full_message + '\n')

    print(full_message)