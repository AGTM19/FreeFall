import pandas as pd
import matplotlib.pyplot as plt

# Read Data in
df = pd.read_csv('flug3.csv', encoding='utf_16_le', delimiter=";")

# Create new Dataframe with cleaner Data
accel = pd.DataFrame()
accel["x"] = df["X [g]"].str.replace(",", ".")
accel["y"] = df["Y [g]"].str.replace(",", ".")
accel["z"] = df["Z [g]"].str.replace(",", ".")
accel["height"] = df["Höhe [m]"].str.replace(",", ".")
accel = accel.astype("float")

# Additional Information
start = accel["height"].argmax()
stop = accel["height"].argmin()
accel["abs"] = (accel["x"]**2 + accel["y"]**2 + accel["z"]**2)**(1/2)*9.81*10-9.81*10
title=["measured"]
# Plot
accel.iloc[start:6700].plot(x="abs", y="height", style="-", legend=False, markersize=4, linewidth=0.7,
                            xlabel=" Load [N]", ylabel = "Altitude [m]", title="Droptest",
                            xlim=[-40,1500], ylim=[-40,620])
plt.grid()
plt.savefig(title[0] + ".pdf")
plt.show()

