import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("figures", exist_ok=True)

x_vals = np.linspace(0.0, 0.25, 100)

# Theoretical Taylor Expansion Terms
first_order = np.zeros_like(x_vals)                  # D\hat{\Omega}_G(I) = 0
second_order = x_vals**2                            # Quadratic Shear
full_residual = x_vals**2 - 1.5 * (x_vals**3)       # Full Error Operator Norm

plt.figure(figsize=(8, 5))

plt.plot(x_vals, first_order, 'r--', linewidth=2, label=r"Linear Term $\mathcal{O}(\|\hat{X}\|) = 0$ (Vanishing)")
plt.plot(x_vals, second_order, 'g-', linewidth=2, label=r"Quadratic Term $\mathcal{O}(\|\hat{X}\|^2)$ (Shear Threshold)")
plt.plot(x_vals, full_residual, 'b-.', linewidth=2, label=r"Full Fréchet Residual $\|\mathcal{E}(\hat{X})\|$")

plt.title("Figure 3: Non-Abelian Shear Suppression vs Perturbation Norm", fontsize=12, fontweight='bold')
plt.xlabel("Perturbation Strength $\|\hat{X}\|$", fontsize=11)
plt.ylabel("Residual Operator Output", fontsize=11)
plt.legend(fontsize=10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()

plt.savefig("figures/fig3_shear_suppression.png", dpi=300)
plt.show()

print("Status: Figure 3 saved to 'figures/fig3_shear_suppression.png'")
