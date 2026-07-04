import cv2
import numpy as np
from insightface.app import FaceAnalysis

app = FaceAnalysis(
    name="buffalo_l",
    providers=["CPUExecutionProvider"]
)

app.prepare(ctx_id=0, det_size=(640, 640))


def get_embedding(image_path):

    img = cv2.imread(image_path)

    if img is None:
        return None

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    faces = app.get(img)

    if len(faces) == 0:
        print("No face detected:", image_path)
        return None

    face = max(
        faces,
        key=lambda f:
        (f.bbox[2]-f.bbox[0]) *
        (f.bbox[3]-f.bbox[1])
    )

    emb = face.embedding
    emb = emb / np.linalg.norm(emb)

    return emb