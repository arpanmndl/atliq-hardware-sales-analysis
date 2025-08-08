import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os
import numpy as pd

# Create output directory
output_path = '/mnt/data/powerbi_etl_flowchart.png'
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Define figure and axis
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 12)
ax.axis('off')

# Define box properties
box_props = dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightblue")
narrow_box_props = dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightgreen")

# Define steps and positions
steps = [
    ("Install Power BI Desktop", (5, 11), box_props),
    ("Connect to MySQL\nusing Get Data", (5, 9.5), box_props),
    ("Build Data Model:\nStar Schema", (5, 8), box_props),
    ("Transform Data\nin Power Query", (5, 6.5), box_props),
    ("Filter non-Indian markets\nfrom Market table", (2, 5), narrow_box_props),
    ("Remove rows with\nsales_amount <= 0\nfrom Transactions", (5, 5), narrow_box_props),
    ("Add column 'sales_amount_INR'\nwith currency normalization", (8, 5), narrow_box_props),
    ("Replace outdated columns\nwith transformed versions", (5, 3.5), box_props),
    ("Apply Changes:\nClose & Apply", (5, 2), box_props),
    ("Load cleaned data\ninto Power BI", (5, 0.5), box_props)
]

# Draw boxes
for text, (x, y), props in steps:
    ax.text(x, y, text, ha='center', va='center', bbox=props, fontsize=10)

# Draw arrows
arrow_style = dict(arrowstyle="->", color="black")
narrow_connections = [
    ((5, 11), (5, 9.7)),
    ((5, 9.5), (5, 8.2)),
    ((5, 8), (5, 6.7)),
    ((5, 6.5), (2, 5.2)),
    ((5, 6.5), (5, 5.2)),
    ((5, 6.5), (8, 5.2)),
    ((5, 5), (5, 3.7)),
    ((5, 3.5), (5, 2.2)),
    ((5, 2), (5, 0.7))
]
for start, end in narrow_connections:
    ax.annotate('', xy=end, xytext=start, arrowprops=arrow_style)

# Save the flowchart
plt.tight_layout()
plt.savefig(output_path)
plt.close()

print("Flowchart saved to:", output_path)
