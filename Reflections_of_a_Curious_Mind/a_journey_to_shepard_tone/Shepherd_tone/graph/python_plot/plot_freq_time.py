import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# ===============================
# Global academic style settings
# ===============================

rcParams["font.family"] = "serif"
rcParams["font.serif"] = ["Times New Roman"]
rcParams["font.size"] = 11
rcParams["axes.labelsize"] = 11
rcParams["xtick.labelsize"] = 11
rcParams["ytick.labelsize"] = 11
rcParams["legend.fontsize"] = 11
rcParams["lines.linewidth"] = 1.1
rcParams["figure.dpi"] = 120

# ===============================
# Load data
# ===============================

data = np.loadtxt(
    r"E:\BrokenFate\github_files\Reflections_of_a_Curious_Mind\graph\frequency_vs_time.txt"
)

time = data[:, 0]
freq = data[:, 1]
channel = data[:, 2]

# ===============================
# Break polyline at discontinuities
# ===============================

def break_polyline(t, f, drop_threshold=-50):
    t_out = [t[0]]
    f_out = [f[0]]

    for i in range(1, len(f)):
        if f[i] - f[i - 1] < drop_threshold:
            t_out.append(np.nan)
            f_out.append(np.nan)

        t_out.append(t[i])
        f_out.append(f[i])

    return np.array(t_out), np.array(f_out)

# Channel separation
mask1 = channel == 1
mask2 = channel == 2

t1, f1 = break_polyline(time[mask1], freq[mask1])
t2, f2 = break_polyline(time[mask2], freq[mask2])

# ===============================
# Plot
# ===============================

fig, ax = plt.subplots(figsize=(5, 3))

# ax.step(t1, f1, where="post", color="red", label="Lower sweep")
# ax.step(t2, f2, where="post", color="blue", label="Upper sweep")
ax.step(t1, f1, where="post", color="red")
ax.step(t2, f2, where="post", color="blue")

ax.set_xlabel("Time (s)")
ax.set_ylabel("Frequency (Hz)")

ax.set_xlim(0, 60)
ax.set_ylim(100, 750)

ax.legend(frameon=False)

fig.tight_layout()

# ===============================
# Save (publication quality)
# ===============================

fig.savefig(
    "freq_vs_time_Shepard_sine_177-343Hz_343-687Hz.svg",
    format="svg"
)

plt.show()
