from datetime import datetime
import csv
from collections import defaultdict
import numpy as np
import json

ORIGINAL_DATE_FORMAT = "%d.%m.%Y %H:%M"
DATE_FORMAT = "%d.%m.%Y"

def parse_csv_weather_data(file_path):
  grouped_temp_data = defaultdict(lambda: defaultdict(list))

  with open(file_path, 'rb') as csvfile:
    d_reader = csv.DictReader(csvfile, fieldnames=['datetime', 'temperature'], delimiter=';')
    d_reader.next() # Switching to the second line from header
    
    cur_day = defaultdict(list)

    for idx, row in enumerate(d_reader):
      if not row['temperature'] or not row['datetime']:
        continue #skipping invalid data row

      info_date = datetime.strptime(row['datetime'], ORIGINAL_DATE_FORMAT).strftime(DATE_FORMAT)
      if not cur_day:
        cur_day[info_date].append(float(row['temperature']))
      elif cur_day.keys()[0] == info_date:
        cur_day[info_date].append(float(row['temperature']))
      else:
        year = datetime.strptime(cur_day.keys()[0], DATE_FORMAT).strftime('%Y')
        month = datetime.strptime(cur_day.keys()[0], DATE_FORMAT).strftime('%m')
        grouped_temp_data[int(year)][int(month) - 1].append(np.mean(cur_day.values()))

        cur_day.clear()
        cur_day[info_date].append(float(row['temperature']))

  return grouped_temp_data