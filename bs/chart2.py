import matplotlib.pyplot as plt
import numpy as np

channel_widths = [20, 40]
transmission_time = [82.77, 93.91]
transmission_speed = [29, 25.26]
average_response_time = [18.247, 26.377]
max_response_time = [27.899, 64.475]

x = np.arange(len(channel_widths))

plt.figure(figsize=(12, 8))

plt.subplot(221)
plt.step(x, transmission_time, where='mid', label='Время передачи (сек)', marker='o')
plt.xticks(x, channel_widths)
plt.ylabel('Время передачи (сек)')
plt.title('Время передачи по ширине канала')
plt.grid()
for i, value in enumerate(transmission_time):
    plt.annotate(f'{value}', (x[i], transmission_time[i]), textcoords="offset points", xytext=(0, 10), ha='center')

plt.subplot(222)
plt.step(x, transmission_speed, where='mid', label='Скорость передачи (Мбит/с)', marker='o', color='orange')
plt.xticks(x, channel_widths)
plt.ylabel('Скорость передачи (Мбит/с)')
plt.title('Скорость передачи по ширине канала')
plt.grid()
for i, value in enumerate(transmission_speed):
    plt.annotate(f'{value}', (x[i], transmission_speed[i]), textcoords="offset points", xytext=(0, 10), ha='center')

plt.subplot(223)
plt.step(x, average_response_time, where='mid', label='Среднее время отклика (мс)', marker='o', color='green')
plt.xticks(x, channel_widths)
plt.ylabel('Среднее время отклика (мс)')
plt.title('Среднее время отклика по ширине канала')
plt.grid()
for i, value in enumerate(average_response_time):
    plt.annotate(f'{value}', (x[i], average_response_time[i]), textcoords="offset points", xytext=(0, 10), ha='center')

plt.subplot(224)
plt.step(x, max_response_time, where='mid', label='Максимальное время отклика (мс)', marker='o', color='red')
plt.xticks(x, channel_widths)
plt.ylabel('Максимальное время отклика (мс)')
plt.title('Максимальное время отклика по ширине канала')
plt.grid()
for i, value in enumerate(max_response_time):
    plt.annotate(f'{value}', (x[i], max_response_time[i]), textcoords="offset points", xytext=(0, 10), ha='center')

plt.tight_layout()
plt.show()
