import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

data = pd.read_csv('data_files/data_trajectory.csv')
# print(data.head())

# ------- Plot jerk data -------

fig = plt.figure(figsize=(7,5))
ax = plt.axes()
ax.plot(data['Time'], data['Jerk'], label='Jerk [mm/s³]')
ax.plot(data['Time'], data['Acceleration'], label='Acceleration [mm/s²]')
ax.plot(data['Time'], data['Velocity'], label='Velocity [mm/s]')
ax.plot(data['Time'], data['Position'], label='Position [mm]')

ax.set_ylim(-1250, 1350)
plt.yticks([-1000, -500, 0, 400, 500, 1000, 1200])
leg = ax.legend()

plt.axhline(y = 1200, xmin = 0.0, xmax = 0.95, color = 'grey', linestyle = ':', linewidth = 1)
plt.axhline(y = 1000, xmin = 0.0, xmax = 0.05, color = 'grey', linestyle = ':', linewidth = 1)
plt.axhline(y = 400, xmin = 0.0, xmax = 0.31, color = 'grey', linestyle = ':', linewidth = 1)
plt.axhline(y = 500, xmin = 0.0, xmax = 0.15, color = 'grey', linestyle = ':', linewidth = 1)
plt.axhline(y = -500, xmin = 0.0, xmax = 0.79, color = 'grey', linestyle = ':', linewidth = 1)
plt.axhline(y = -1000, xmin = 0.0, xmax = 0.22, color = 'grey', linestyle = ':', linewidth = 1)

plt.xlabel('Time [s]', fontsize=12)
plt.xticks(np.arange(0, data['Time'].iloc[-1]+data['Time'].iloc[-1]/5, data['Time'].iloc[-1]/5))
plt.show()

# print("Time: " + str(data['Time'].iloc[-1]))


# ------- Plot joint data -------

joints = [data['J1'], data['J2'], data['J3'], data['J4'], data['J5'], data['J6']]
nJoint = 1

for j in joints:
    fig = plt.figure(figsize=(8,5))
    ax = plt.axes()
    ax.plot(data['Time'], j, label='J1', linewidth=2.5)

    plt.yticks(np.arange(min(j), max(j)+1, (max(j)-min(j))/5))

    plt.xlabel('Time [s]', fontsize=25, labelpad=25)
    plt.ylabel('Joint angle [°]', fontsize=25, labelpad=10)
    plt.xticks(fontsize=20)
    plt.xticks(np.arange(0, data['Time'].iloc[-1]+data['Time'].iloc[-1]/5, data['Time'].iloc[-1]/5))
    plt.yticks(fontsize=20, rotation=45)
    plt.gca().yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))

    # name = "Export2\J" + str(nJoint) + ".svg"
    # plt.savefig(name, bbox_inches='tight')

    nJoint += 1
    plt.show()