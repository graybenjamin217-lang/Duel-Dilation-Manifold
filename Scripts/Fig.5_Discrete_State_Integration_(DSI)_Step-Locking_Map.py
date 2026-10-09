import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("figures", exist_ok=True)

# Continuous Input Phase Shift Sweep
continuous_phase = np.linspace(-0.6, 0.6, 500)
threshold = 0.27417

# Apply DSI Step-Locking Filter
quantized_output = np.zeros_like(continuous_phase)

for idx, phi in enumerate(continuous_phase):
    if abs(phi) < threshold:
        # Quadratically suppressed to zero state
        quantized_output[idx] = 0.0
    elif phi >= threshold:
        # Phase-locked upper state
        quantized_output[idx] = 0.5
    else:
        # Phase-locked lower state
        quantized_output[idx] = -0.5

plt.figure(figsize=(8.5, 5))

plt.plot(continuous_phase, continuous_phase, 'r--', label="Continuous Linear Drift (Unfiltered)")
plt.plot(continuous_phase, quantized_output, 'b-', linewidth=2.5, label="Discrete State Integration (DSI Locked)")

plt.axvline(threshold, color='green', linestyle=':', label=r"Threshold $+\delta$")
plt.axvline(-threshold, color='green', linestyle=':', label=r"Threshold $-\delta$")

plt.title("Figure 5: Discrete State Integration (DSI) Holonomy Locking", fontsize=12, fontweight='bold')
plt.xlabel("Continuous Input Phase Perturbation $\hat{H}(t)$", fontsize=11)
plt.ylabel("Filtered State Output $\hat{\Omega}_G^n(I + \hat{H}(t))$", fontsize=11)
plt.legend(fontsize=9, loc='upper left')
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()

plt.savefig("figures/fig5_dsi_locking.png", dpi=300)
plt.show()

print("Status: Figure 5 saved to 'figures/fig5_dsi_locking.png'")
