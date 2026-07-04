import os
import shutil
import pandas as pd

from embedding import get_embedding
from clustering import cluster_faces
from confidence import calculate_confidence
from visualization import generate_html

DATASET = "dataset"
OUTPUT = "output"

os.makedirs(OUTPUT, exist_ok=True)

print("Loading images...")

image_paths = []
embeddings = []

for root, _, files in os.walk(DATASET):

    for file in files:

        if file.lower().endswith((".png", ".jpg", ".jpeg")):

            path = os.path.join(root, file)

            emb = get_embedding(path)

            if emb is not None:
                image_paths.append(path)
                embeddings.append(emb)

print("Total images:", len(image_paths))

labels = cluster_faces(embeddings, threshold=0.60)

cluster_map = {}

results = []

for path, emb, label in zip(image_paths, embeddings, labels):

    person = os.path.basename(os.path.dirname(path))

    filename = f"{person}_{os.path.basename(path)}"

    cluster_folder = os.path.join(OUTPUT, f"Cluster_{label}")
    os.makedirs(cluster_folder, exist_ok=True)

    shutil.copy(path, os.path.join(cluster_folder, filename))

    if label not in cluster_map:
        cluster_map[label] = []

    cluster_map[label].append(emb)

    confidence = calculate_confidence(emb, cluster_map[label])

    results.append([filename, person, label, confidence])

df = pd.DataFrame(results, columns=[
    "Image", "Actual Person", "Cluster", "Confidence"
])

csv_path = os.path.join(OUTPUT, "results.csv")
df.to_csv(csv_path, index=False)

print("CSV saved:", csv_path)

# ⭐ HTML GENERATION (IMPORTANT FIX)
generate_html(OUTPUT)

print("DONE ✔")