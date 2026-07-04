import os

def generate_html(output_folder):

    html = """
    <html>
    <head>
    <title>Face Clusters</title>

    <style>
    body { font-family: Arial; background: #f5f5f5; }
    .cluster { background: white; margin: 20px; padding: 15px; border-radius: 10px; }
    img { width: 150px; height: 150px; margin: 5px; object-fit: cover; }
    </style>

    </head>
    <body>

    <h1 style="text-align:center;">Face Clustering Results</h1>
    """

    for folder in sorted(os.listdir(output_folder)):

        path = os.path.join(output_folder, folder)

        if not os.path.isdir(path):
            continue

        html += f"<div class='cluster'><h2>{folder}</h2>"

        for img in os.listdir(path):

            if img.endswith((".png", ".jpg", ".jpeg")):

                # IMPORTANT FIX (relative path)
                img_path = f"{folder}/{img}"

                html += f"<img src='{img_path}'>"

        html += "</div>"

    html += "</body></html>"

    with open(os.path.join(output_folder, "results.html"), "w", encoding="utf-8") as f:
        f.write(html)