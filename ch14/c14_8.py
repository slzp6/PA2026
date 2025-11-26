"""c14_8.py"""

import matplotlib.pyplot as plt

labels = ["10", "20", "30", "40", "50", "60", "70"]
values = [2847, 13953, 11994, 14685, 16510, 11504, 9448]
fig, ax = plt.subplots()
ax.pie(x=values, labels=labels, autopct="%.2f%%", \
       startangle=45, counterclock=False)
ax.set_title("undergraduate students (2024)")
# plt.show()
plt.savefig("c14_8.png")
