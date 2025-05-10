import matplotlib.pyplot as plt
import numpy as np

years = [2019, 2020, 2021, 2022]

LFPRate = [61.3, 59.5, 63.3, 64.7]
EmploymentRate = [94.9, 89.7, 92.2, 94.6]
UnderemploymentRate = [13.8, 16.2, 15.9, 14.2]
UnemploymentRate = [5.1, 10.3, 7.8, 5.4]

y = np.arange(len(years))
bar_height = 0.2

y1 = y - 1.5 * bar_height
y2 = y - 0.5 * bar_height
y3 = y + 0.5 * bar_height
y4 = y + 1.5 * bar_height

plt.figure(figsize=(10, 6))
plt.barh(y1, LFPRate, bar_height, color='skyblue', label='Labor Force Participation Rate')
plt.barh(y2, EmploymentRate, bar_height, color='green', label='Employment Rate',)
plt.barh(y3, UnderemploymentRate, bar_height, color='orange', label='Underemployment Rate')
plt.barh(y4, UnemploymentRate, bar_height, color='red', label='Unemployment Rate')


plt.xlabel('Year')
plt.ylabel('Rate (%)')
plt.title('Key Labor and Employment Indicators (2019-2022)')
plt.yticks(y, years)
plt.legend(loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
