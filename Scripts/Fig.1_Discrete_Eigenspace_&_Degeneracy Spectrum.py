import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("figures", exist_ok=True)

# 1. Construct 16D Basis Characters (+1, -1)
P = np.array([1, -1])
D = np.array([1, -1])
A = np.array([1, -1])
S = np.array([1, -1])

# Build 16-dimensional tensor states
states = []
for p in P:
    for d in D:
        for a in A:
            for s in S:
                states.append((p, d, a, s))
states = np.array(states)

# 2. Build Master Operator Matrix \hat{\Omega}_G
E_vac = 1.0
E_0 = 1.0
kappa = 1.0 / 16.0

# Evaluate diagonal elements for x = P*D and y = A*S
x = states[:, 0] * states[:, 1]
y = states[:, 2] * states[:, 3]
diag_elements = E_vac + kappa * E_0 * (x + y)

Omega_G = np.diag(diag_elements)
eigenvalues = np.linalg.eigvalsh(Omega_G)

# Plot Eigenspectrum Histogram
plt.figure(figsize=(8, 5))
unique_ev, counts = np.unique(np.round(eigenvalues, 5), return_counts=True)

plt.bar(unique_ev, counts, width=0.03, color='indigo', alpha=0.8, edgecolor='black')
for ev, count in zip(unique_ev, counts):
    plt.text(ev, count + 0.3, f"Degeneracy: {count}\n$\lambda = {ev:.3f}$", ha='center', fontsize=9)

plt.title("Figure 1: Discrete Point Spectrum & Eigenspace Degeneracy (4:8:4)", fontsize=12, fontweight='bold')
plt.xlabel("Eigenvalue ($\lambda_k$)", fontsize=11)
plt.ylabel("State Multiplicity (Degeneracy $g_k$)", fontsize=11)
plt.ylim(0, 10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()

plt.savefig("figures/fig1_manifold_spectrum.png", dpi=300)
plt.show()

print("Status: Figure 1 saved to 'figures/fig1_manifold_spectrum.png'")
