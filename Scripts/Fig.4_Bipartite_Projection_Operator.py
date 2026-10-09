import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("figures", exist_ok=True)

# Build 16D single-manifold character diagonal
states_1d = []
for p in [1, -1]:
    for d in [1, -1]:
        for a in [1, -1]:
            for s in [1, -1]:
                states_1d.append((p, d, a, s))
states_1d = np.array(states_1d)

# Construct 256D Bipartite States
bipartite_P = np.outer(states_1d[:, 0], states_1d[:, 0])
bipartite_D = np.outer(states_1d[:, 1], states_1d[:, 1])

# Parity Preservation Condition: (P1 + P2) mod 2 == 0 and D1*D2 == +1
Pi_64 = np.zeros((256, 256))

idx = 0
for i in range(16):
    for j in range(16):
        p1, d1 = states_1d[i, 0], states_1d[i, 1]
        p2, d2 = states_1d[j, 0], states_1d[j, 1]
        
        # Diagonal invariant subspace filter
        if (p1 == p2) and (d1 * d2 == 1):
            Pi_64[idx, idx] = 1.0
        idx += 1

rank_Pi = int(np.trace(Pi_64))

plt.figure(figsize=(7, 6))
im = plt.imshow(Pi_64, cmap='binary', origin='upper')

plt.title(f"Figure 4: Bipartite Projection Matrix $\hat{{\Pi}}_{{64}}$ (Rank = {rank_Pi})", fontsize=12, fontweight='bold')
plt.xlabel("Bipartite Basis State Index ($1 \dots 256$)", fontsize=11)
plt.ylabel("Bipartite Basis State Index ($1 \dots 256$)", fontsize=11)
plt.colorbar(im, label="Projection Weight")
plt.tight_layout()

plt.savefig("figures/fig4_bipartite_projection.png", dpi=300)
plt.show()

print(f"Status: Figure 4 saved to 'figures/fig4_bipartite_projection.png' (Calculated Rank: {rank_Pi})")
