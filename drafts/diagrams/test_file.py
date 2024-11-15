import numpy as np
import matplotlib.pyplot as plt
import openpyxl

# Открываем файл xlsx, при необходимости с путем
wb = openpyxl.load_workbook('угол и уровень.xlsx')
# получаем активный лист
sheet = wb.active
A = np.array([[i.value for i in j] for j in sheet['A2':'B37']])
# замыкаем кривую
A = np.vstack((A, A[0, :]))
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(np.radians(A[:, 0]), A[:, 1])
ax.set_rmin(-20)
ax.set_rticks([0, -10, -20])  # Less radial ticks
ax.grid(True)
ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()
wb.close()