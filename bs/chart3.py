import matplotlib.pyplot as plt
import numpy as np

transmitter_power = [100, 80, 60, 40, 20]
transmission_time = [77.43, 90.53, 109.31, 113.39, 115.95]
transmission_speed = [31, 26.51, 21.96, 21.17, 20.70]
average_response_time = [9.542, 18.625, 18.635, 17.569, 17.520]
max_response_time = [17.881, 29.959, 28.174, 28.054, 29.209]

x = np.arange(len(transmitter_power))

plt.figure(figsize=(12, 10))

plt.subplot(221)
plt.plot(x, transmission_time, marker='o', color='blue', label='Время передачи (сек)')
plt.xticks(x, transmitter_power)
plt.ylabel('Время передачи (сек)')
plt.title('Время передачи в зависимости от мощности передатчика')
plt.grid()
for i, value in enumerate(transmission_time):
    plt.annotate(f'{value}', (x[i], transmission_time[i]), textcoords="offset points", xytext=(0, 10), ha='center')

plt.subplot(222)
plt.plot(x, transmission_speed, marker='o', color='orange', label='Скорость передачи (Мбит/с)')
plt.xticks(x, transmitter_power)
plt.ylabel('Скорость передачи (Мбит/с)')
plt.title('Скорость передачи в зависимости от мощности передатчика')
plt.grid()
for i, value in enumerate(transmission_speed):
    plt.annotate(f'{value}', (x[i], transmission_speed[i]), textcoords="offset points", xytext=(0, 10), ha='center')

plt.subplot(223)
plt.plot(x, average_response_time, marker='o', color='green', label='Среднее время отклика (мс)')
plt.xticks(x, transmitter_power)
plt.ylabel('Среднее время отклика (мс)')
plt.title('Среднее время отклика в зависимости от мощности передатчика')
plt.grid()
for i, value in enumerate(average_response_time):
    plt.annotate(f'{value}', (x[i], average_response_time[i]), textcoords="offset points", xytext=(0, 10), ha='center')

plt.subplot(224)
plt.plot(x, max_response_time, marker='o', color='red', label='Максимальное время отклика (мс)')
plt.xticks(x, transmitter_power)
plt.ylabel('Максимальное время отклика (мс)')
plt.title('Максимальное время отклика в зависимости от мощности передатчика')
plt.grid()
for i, value in enumerate(max_response_time):
    plt.annotate(f'{value}', (x[i], max_response_time[i]), textcoords="offset points", xytext=(0, 10), ha='center')

plt.tight_layout()
plt.show()