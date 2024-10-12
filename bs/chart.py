import matplotlib.pyplot as plt
import numpy as np

standards = ['A', 'N', 'A+N', 'AC', 'N+AC', 'A+N+AC']
transmission_time = [115.57, 77.43, 104.95, 143.23, 85.03, 96.16]
transmission_speed = [20.77, 31, 22.87, 16.76, 28.22, 24.96]
average_response_time = [17.170, 9.542, 23.407, 64.338, 18.020, 19.803]
max_response_time = [29.644, 17.783, 35.724, 159.197, 30.948, 32.641]

x = np.arange(len(standards))

plt.figure(figsize=(12, 8))

plt.subplot(221)
plt.step(x, transmission_time, where='mid', label='Время передачи (сек)', marker='o')
plt.xticks(x, standards)
plt.ylabel('Время передачи (сек)')
plt.title('Время передачи по стандартам')
plt.grid()
for i, value in enumerate(transmission_time):
    plt.annotate(f'{value}', (x[i], transmission_time[i]), textcoords="offset points", xytext=(0, 10), ha='center')

plt.subplot(222)
plt.step(x, transmission_speed, where='mid', label='Скорость передачи (Мбит/с)', marker='o', color='orange')
plt.xticks(x, standards)
plt.ylabel('Скорость передачи (Мбит/с)')
plt.title('Скорость передачи по стандартам')
plt.grid()
for i, value in enumerate(transmission_speed):
    plt.annotate(f'{value}', (x[i], transmission_speed[i]), textcoords="offset points", xytext=(0, 10), ha='center')

plt.subplot(223)
plt.step(x, average_response_time, where='mid', label='Среднее время отклика (мс)', marker='o', color='green')
plt.xticks(x, standards)
plt.ylabel('Среднее время отклика (мс)')
plt.title('Среднее время отклика по стандартам')
plt.grid()
for i, value in enumerate(average_response_time):
    plt.annotate(f'{value}', (x[i], average_response_time[i]), textcoords="offset points", xytext=(0, 10), ha='center')

plt.subplot(224)
plt.step(x, max_response_time, where='mid', label='Максимальное время отклика (мс)', marker='o', color='red')
plt.xticks(x, standards)
plt.ylabel('Максимальное время отклика (мс)')
plt.title('Максимальное время отклика по стандартам')
plt.grid()
for i, value in enumerate(max_response_time):
    plt.annotate(f'{value}', (x[i], max_response_time[i]), textcoords="offset points", xytext=(0, 10), ha='center')

plt.tight_layout()
plt.show()
