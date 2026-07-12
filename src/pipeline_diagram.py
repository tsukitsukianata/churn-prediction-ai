import matplotlib.pyplot as plt
from pathlib import Path

steps = [
    "Raw Dataset\n(SQLite)",
    "Remove\ncustomerID",
    "Encode\nChurn (0/1)",
    "One-Hot Encode\nCategorical Features",
    "Train/Test Split\n(80/20)",
    "Scale Numerical\nFeatures",
    "ML-Ready Dataset\n(X_train, X_test,\ny_train, y_test)"
]

colors = [
    "#0F172A",
    "#1D4ED8",
    "#2563EB",
    "#3B82F6",
    "#60A5FA",
    "#93C5FD",
    "#1E3A8A"
]

# More vertical space
spacing = 1.5

fig, ax = plt.subplots(figsize=(8, 14), dpi=300)

ax.set_xlim(0, 1)
ax.set_ylim(0, len(steps) * spacing)
ax.axis("off")

x = 0.5

for i, step in enumerate(steps):

    y = (len(steps) - i - 0.5) * spacing

    ax.text(
        x,
        y,
        step,
        ha="center",
        va="center",
        fontsize=12,
        fontweight="bold",
        color="white",
        bbox=dict(
            boxstyle="round,pad=0.7",
            facecolor=colors[i],
            edgecolor="#1E293B",
            linewidth=1.5
        )
    )

    # Draw arrow between boxes
    if i < len(steps) - 1:
        ax.annotate(
            "",
            xy=(x, y - 0.95),      # arrow head
            xytext=(x, y - 0.55),  # arrow tail
            arrowprops=dict(
                arrowstyle="-|>",
                color="#475569",
                lw=2.5
            )
        )

plt.title(
    "Machine Learning Preprocessing Pipeline",
    fontsize=20,
    fontweight="bold",
    pad=25
)

output_dir = Path(__file__).parent.parent / "notebooks" / "images"
output_dir.mkdir(parents=True, exist_ok=True)

plt.savefig(
    output_dir / "ml_preprocessing_pipeline.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()