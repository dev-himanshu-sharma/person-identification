📌 Person Identification / Face Clustering Project
👁️ Overview
[Preview] (
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
    <div class='cluster'><h2>Cluster_0</h2><img src='Cluster_0/person1_img1.png'><img src='Cluster_0/person1_img2.png'><img src='Cluster_0/person1_img3.png'></div><div class='cluster'><h2>Cluster_1</h2><img src='Cluster_1/person10_img1.png'><img src='Cluster_1/person10_img2.png'><img src='Cluster_1/person9_img3.png'><img src='Cluster_1/person9_img4.png'></div><div class='cluster'><h2>Cluster_2</h2><img src='Cluster_2/person2_img1.png'><img src='Cluster_2/person2_img2.png'><img src='Cluster_2/person2_img3.png'></div><div class='cluster'><h2>Cluster_3</h2><img src='Cluster_3/person3_img1.png'><img src='Cluster_3/person3_img2.png'><img src='Cluster_3/person3_img3.png'><img src='Cluster_3/person3_img4.png'><img src='Cluster_3/person3_img5.png'><img src='Cluster_3/person3_img6.png'><img src='Cluster_3/person4_img1.png'><img src='Cluster_3/person4_img2.png'><img src='Cluster_3/person4_img3.png'></div><div class='cluster'><h2>Cluster_4</h2><img src='Cluster_4/person5_img1.png'><img src='Cluster_4/person5_img2.png'></div><div class='cluster'><h2>Cluster_5</h2><img src='Cluster_5/person6_img1.png'><img src='Cluster_5/person6_img2.png'></div><div class='cluster'><h2>Cluster_6</h2><img src='Cluster_6/person7_img1.png'><img src='Cluster_6/person7_img2.png'></div><div class='cluster'><h2>Cluster_7</h2><img src='Cluster_7/person8_img1.png'><img src='Cluster_7/person8_img2.png'></div><div class='cluster'><h2>Cluster_8</h2><img src='Cluster_8/person9_img1.png'><img src='Cluster_8/person9_img2.png'></div></body></html>)

This project performs face clustering and person identification by grouping similar face images into clusters. Each cluster represents images belonging to the same identity based on similarity features.

The final results are visualized using an HTML report.

📁 Project Structure
person_identification/
│
├── Cluster_0/
├── Cluster_1/
├── Cluster_2/
├── Cluster_3/
│
├── output/
│     └── results.html   # Final clustering visualization
│
├── index.html
└── README.md
📊 Output Visualization

The final clustering result is available at:

👉 output/results.html

Open it in any web browser to view grouped face clusters.

🖼️ Preview

If supported, the output looks like a structured HTML page showing:

Multiple clusters
Faces grouped by identity
Each cluster containing similar images

⚠️ If preview does not load on GitHub, download or open results.html manually in a browser.

🚀 How to Run
1. Clone the repository
git clone https://github.com/dev-himanshu-sharma/person-identification.git
2. Move into project folder
cd person-identification
3. Open results

Open the file:

output/results.html

in your browser.

OR use VS Code Live Server for better experience.

⚙️ Features
Face image clustering
Grouping similar identities
HTML-based visualization
Organized cluster-wise output
Easy browser viewing

🧠 Technologies Used
HTML & CSS (Visualization)
Python (Clustering logic - if used)
Face embeddings / feature extraction
Machine learning clustering methods (e.g., KMeans / DBSCAN)
📌 Use Cases
Face recognition systems
Photo organization by person
Security and surveillance analysis
AI/ML learning project
📈 Future Improvements
Real-time face recognition integration
Improved clustering using deep learning (FaceNet / ArcFace)
Interactive UI dashboard
Search feature for individuals
Web deployment (GitHub Pages / Netlify)
👨‍💻 Author

Himanshu Sharma
GitHub: https://github.com/dev-himanshu-sharma

📄 License

This project is intended for educational and research purposes.

⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!
