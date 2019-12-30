# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 22:15:23 2019

@author: Blin
"""

from matplotlib import pyplot as plt

plt.style.use('dark_background')

ages_x = [2, 4, 5, 6, 9, 12, 15, 25, 30]
dev_y = [150, 250, 300, 125, 645, 340, 55, 450, 320]
py_dev_y = [250, 650, 400, 925, 445, 540, 155, 250, 320]
js_dev_y = [550, 750, 600, 525, 645, 540, 255, 350, 220]

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)
print(fig)
print(ax1)
print(ax2)

ax1.plot(ages_x, dev_y, color='#eeeeee', linewidth=3, linestyle='--', marker='.', label='All Devs')
ax1.plot(ages_x, py_dev_y, color='b', marker='.', label='Py Devs')
ax1.plot(ages_x, js_dev_y, color='y', marker='.', label='Js Devs')

ax2.bar(ages_x, dev_y)
ax2.bar(ages_x, py_dev_y)
ax2.bar(ages_x, js_dev_y)

ax2.set_xlabel('Ages')
ax2.set_ylabel('Salary')
ax2.set_title('Median Salary (USD) by Age')

plt.legend()
plt.show()