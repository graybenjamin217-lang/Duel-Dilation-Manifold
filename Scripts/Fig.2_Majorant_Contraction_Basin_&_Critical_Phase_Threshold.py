import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("figures", exist_ok=True)

def error_map(r):
    mu = 17.0 / 16.0
    return mu * (r**2 * (1.0 + 0.5 * r)) / (1.0 - r + 1e-12)

# Initial perturbation radius sweep
r_inits = [0.15, 0.20, 0.25, 0.27417, 0.30, 0.35]
iterations = 8

plt.figure(figsize=(8.5, 5.5))

for r0 in r_inits:
    r_history = [r0]
    r_curr = r0
    for _ in range(iterations):
        r_curr = error_map(r_curr)
        r_history.append(r_curr)
    
    style = 'o-' if r0 <= 0.27417 else 's--'
    label = f"$r_0 = {r0}$ (Stable)" if r0 <= 0.27417 else f"$r_0 = {r0}$ (Divergent)"
    plt.plot(range(iterations + 1), r_history, style, label=label)

plt.axhline(0.27417, color='red', linestyle=':', label=r"Critical Threshold $\delta \approx 0.27417$")
plt.yscale('log')
plt.title("Figure 2: Banach Fixed-Point Contraction Basin", fontsize=12, fontweight='bold')
plt.xlabel("Iteration Step ($n$)", fontsize=11)
plt.ylabel("Perturbation Norm $\|\hat{X}_n\|$ (Log Scale)", fontsize=11)
plt.legend(fontsize=9, loc='center right')
plt.grid(True, which="both", linestyle=':', alpha=0.6)
plt.tight_layout()

plt.savefig("figures/fig2_contraction_basin.png", dpi=300)
plt.show()

print("Status: Figure 2 saved to 'figures/fig2_contraction_basin.png'")
