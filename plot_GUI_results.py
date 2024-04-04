import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes 
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
import pandas as pd

def mean_absolute_error(actual, predicted):
    errors = [abs(a - p) for a, p in zip(actual, predicted)]
    mae = sum(errors) / len(errors)
    return mae

def mean_squared_error(actual, predicted):
    return np.mean((np.array(actual) - np.array(predicted))**2)

def root_mean_squared_error(actual_values, predicted_values):
    mse = np.mean((actual_values - predicted_values)**2)
    rmse = np.sqrt(mse)
    return rmse

data = pd.read_csv('data_files/data_gui.csv')
# print(data.head())

mse = [mean_squared_error(data['X_Kinematics'], data['X_GUI']), mean_squared_error(data['Y_Kinematics'], data['Y_GUI']), mean_squared_error(data['Z_Kinematics'], data['Z_GUI'])]
rmse = [root_mean_squared_error(data['X_Kinematics'], data['X_GUI']), root_mean_squared_error(data['Y_Kinematics'], data['Y_GUI']), root_mean_squared_error(data['Z_Kinematics'], data['Z_GUI'])]
mae = [mean_absolute_error(data['X_Kinematics'], data['X_GUI']), mean_absolute_error(data['Y_Kinematics'], data['Y_GUI']), mean_absolute_error(data['Z_Kinematics'], data['Z_GUI'])]
print('MSE:', mse)
print('RMSE:', rmse)
print('MAE:', mae)


color2 = 'tab:orange'
color1 = 'tab:cyan'


# ------- Plot the data X -------

fig = plt.figure(figsize=(7,5))
ax = plt.axes()
ax.plot(data['Time'], data['X_Kinematics'], label='Kinematics calculation', c=color1)
ax.plot(data['Time'], data['X_GUI'], label='GUI reproduction', c=color2)
ax.set_ylim(900, 1850)
leg = ax.legend(loc=3, fontsize=12)

plt.xlabel('Time [s]', fontsize=12)
plt.ylabel('Position [mm]', fontsize=12)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

axins = zoomed_inset_axes(ax, 10, loc=4) # zoom = 10
axins.plot(data['Time'], data['X_Kinematics'], label='X_Kinematics', c=color1)
axins.plot(data['Time'], data['X_GUI'], label='X_GUI', c=color2)
axins.set_xlim(7.7, 8.1)
axins.set_ylim(1195, 1220)
plt.xticks(visible=False)
plt.yticks(visible=False)
mark_inset(ax, axins, loc1=2, loc2=1, fc="none", ec="0.25")
plt.draw()
plt.show()


# ------- Plot the data Y -------

fig = plt.figure(figsize=(7,5))
ax = plt.axes()
ax.plot(data['Time'], data['Y_Kinematics'], label='Kinematics calculation', c=color1)
ax.plot(data['Time'], data['Y_GUI'], label='GUI reproduction', c=color2)
leg = ax.legend(fontsize=12)

plt.xlabel('Time [s]', fontsize=12)
plt.ylabel('Position [mm]', fontsize=12)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

axins = zoomed_inset_axes(ax, 10, loc=1)
axins.plot(data['Time'], data['Y_Kinematics'], label='Y_Kinematics', c=color1)
axins.plot(data['Time'], data['Y_GUI'], label='Y_GUI', c=color2)
axins.set_xlim(6.4, 6.8)
axins.set_ylim(500, 530)
plt.xticks(visible=False)
plt.yticks(visible=False)
mark_inset(ax, axins, loc1=3, loc2=4, fc="none", ec="0.25")
plt.draw()
plt.show()


# ------- Plot the data Z -------

fig = plt.figure(figsize=(7,5))
ax = plt.axes()
ax.plot(data['Time'], data['Z_Kinematics'], label='Kinematics calculation', c=color1)
ax.plot(data['Time'], data['Z_GUI'], label='GUI reproduction', c=color2)
leg = ax.legend(fontsize=12)

ax.set_ylim(0, 2500)

plt.xlabel('Time [s]', fontsize=12)
plt.ylabel('Position [mm]', fontsize=12)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

axins = zoomed_inset_axes(ax, 10, loc=4)
axins.plot(data['Time'], data['Z_Kinematics'], label='Z_Kinematics', c=color1)
axins.plot(data['Time'], data['Z_GUI'], label='Z_GUI', c=color2)
axins.set_xlim(7.9, 8.3)
axins.set_ylim(1490, 1550)
plt.xticks(visible=False)
plt.yticks(visible=False)
mark_inset(ax, axins, loc1=2, loc2=1, fc="none", ec="0.25")
plt.draw()
plt.show()