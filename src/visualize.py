import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from etl_sql import churn_by
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from pathlib import Path

output_dir = Path(__file__).parent.parent / "notebooks" / "images"
output_dir.mkdir(parents=True, exist_ok=True)


def plot_churn(df, category_col, rate_col="churn_rate"):

    plt.figure(figsize=(10, 6), dpi=300)

    # Professional blue
    bars = plt.bar(
        df[category_col],
        df[rate_col],
        color="#2563EB",
        edgecolor="black",
        linewidth=0.6,
        width=0.65
    )

    plt.title(
        f"Customer Churn Rate by {category_col}",
        fontsize=20,
        fontweight="bold",
        pad=20
    )

    plt.xlabel(category_col, fontsize=13)
    plt.ylabel("Churn Rate", fontsize=13)

    # Display y-axis as percentages
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))

    plt.grid(
        axis="y",
        linestyle="--",
        alpha=0.3
    )

    plt.xticks(rotation=0, fontsize=11)
    plt.yticks(fontsize=11)

    # Remove unnecessary borders
    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # Percentage labels
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + 0.01,
            f"{height:.1%}",
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="bold"
        )

    plt.tight_layout()

    # Save high-quality image
    plt.savefig(
        f"{category_col.lower().replace(' ', '_')}_churn.png",
        dpi=300,
        bbox_inches="tight"
    )

    #plt.show()

listi = ["InternetService", "TechSupport", "OnlineSecurity", "PaymentMethod"]
for i in listi: 
    contract_df = churn_by(i)
    plot_churn(contract_df, i)

    plt.savefig(
        output_dir / f"churn_by_{i.lower().replace(' ', '_')}.png",
        dpi=300,
        bbox_inches="tight"
    )