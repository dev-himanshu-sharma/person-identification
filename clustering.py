import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def cluster_faces(embeddings, threshold=0.60):

    embeddings = np.array(embeddings)

    similarity = cosine_similarity(embeddings)

    n = len(embeddings)

    visited = [False] * n
    labels = [-1] * n

    cluster_id = 0

    for i in range(n):

        if visited[i]:
            continue

        stack = [i]
        visited[i] = True
        labels[i] = cluster_id

        while stack:

            node = stack.pop()

            for j in range(n):

                if not visited[j] and similarity[node][j] >= threshold:

                    visited[j] = True
                    labels[j] = cluster_id
                    stack.append(j)

        cluster_id += 1

    return labels