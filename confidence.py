import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def calculate_confidence(embedding, cluster_embeddings):

    cluster_embeddings = np.array(cluster_embeddings)

    sims = cosine_similarity([embedding], cluster_embeddings)[0]

    return round(float(np.mean(sims) * 100), 2)