🚇 **Metro Navigator**

A Python–Tkinter based Metro Route Finder that calculates:

✔️ All possible paths between two stations

✔️ Shortest route using Dijkstra’s algorithm

✔️ Distance (km)

✔️ Estimated travel time

✔️ Clean GUI with dropdown menus

✔️ Attractive image banner & custom icon

📸 **Preview**

(Add screenshots inside assets/README_images/)

![Interface](assets/README_images/ui_preview.png)

⚡ **Features**
🟦 Graph Algorithms

DFS (Depth-First Search) — to find all possible paths

Dijkstra Algorithm — to compute shortest path & distance

🎨 **GUI**

Built using Tkinter

Dropdown menu for selecting stations

Dynamic result display

Image banner + Metro icon

Hover effects on button

🗂️ **Folder Structure**
MetroNavigator/
│
├── src/
│   └── metro_navigator.py
│
├── assets/
│   ├── metro.ico
│   ├── banner.jpg
│   └── README_images/
│
├── requirements.txt
├── README.md
└── .gitignore

🚀 **Installation & Running**
1. Clone this repository
git clone https://github.com/your-username/MetroNavigator.git
cd MetroNavigator

2. Install dependencies
pip install -r requirements.txt

3. Run the app
python src/metro_navigator.py

📊 **Algorithms Used**
⭐ Depth-First Search (DFS)

Used to enumerate every possible path between source and destination.

⭐ Dijkstra’s Algorithm

Used to find the shortest path + total distance.

