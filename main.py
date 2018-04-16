from wheather_data_aggregator import parse_csv_weather_data
import matplotlib.pyplot as plt
import itertools
from months import MONTHS

aggregated_weather_data = parse_csv_weather_data('data/minsk_2007-2018.csv')

def add_month_ticks(plt, yeat_data):
  day_lengths = [0] + [len(m_days) for m_days in yeat_data.values()[0: len(yeat_data.values()) - 1]]
  day_labels_coords = [sum(day_lengths[0:i+1]) for i in range(0, len(day_lengths))]
  plt.xticks(day_labels_coords, MONTHS.values(), rotation='vertical')

for year in sorted(aggregated_weather_data.keys()):
  year_wheather_data = aggregated_weather_data[year]
  temp_data = list(itertools.chain(*year_wheather_data.values()))
  days = [i for i in range(0, len(temp_data))]
  plt.plot(days, temp_data, label=year)

add_month_ticks(plt, aggregated_weather_data.values()[0])

plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=6, mode="expand", borderaxespad=0.)
plt.show()