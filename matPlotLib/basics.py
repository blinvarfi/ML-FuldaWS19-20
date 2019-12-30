# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 21:29:24 2019

@author: Blin
"""

from matplotlib import pyplot as plt

print(plt.style.available)
plt.style.use('dark_background')

ages_x = [2, 4, 5, 6, 9, 12, 15, 25, 30]
dev_y = [150, 250, 300, 125, 645, 340, 55, 450, 320]
py_dev_y = [250, 650, 400, 925, 445, 540, 155, 250, 320]
js_dev_y = [550, 750, 600, 525, 645, 540, 255, 350, 220]

plt.plot(ages_x, dev_y, color='#eeeeee', linewidth=3, linestyle='--', marker='.', label='All Devs')
plt.plot(ages_x, py_dev_y, color='b', marker='.', label='Py Devs')
plt.plot(ages_x, js_dev_y, color='y', marker='.', label='Js Devs')

plt.xlabel('Ages')
plt.ylabel('Salary')
plt.title('Median Salary (USD) by Age')

plt.bar(ages_x, dev_y)
plt.bar(ages_x, py_dev_y)
plt.bar(ages_x, js_dev_y)

plt.scatter(ages_x, dev_y)
plt.scatter(ages_x, py_dev_y)
plt.scatter(ages_x, js_dev_y)
#plt.legend(['All devs', 'Python'])
plt.legend()
plt.show()