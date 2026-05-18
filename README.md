# 🗺️ Carte Interactive avec Python & Folium

Un projet Python permettant de générer une **carte interactive** avec des marqueurs cliquables, à partir de coordonnées GPS chargées depuis un fichier CSV.

---

## 📋 Prérequis

- Python 3.8+
- pip

---

## 📦 Installation

```bash
pip install folium pandas
```

---

## 📁 Structure du projet

```
mon_projet/
├── main.py        # Script principal
├── lieux.csv       # Données des points à afficher
└── map.html      # Carte générée (ouvrir dans un navigateur)
```

---

## 🚀 Utilisation

### 1. Préparer les données

Crée un fichier `lieux.csv` avec le format suivant :

```csv
nom,latitude,longitude,description
Tour Eiffel,48.8584,2.2945,Monument emblématique de Paris
Louvre,48.8606,2.3376,Le plus grand musée du monde
Notre-Dame,48.8530,2.3499,Cathédrale gothique
```

### 2. Lancer le script

```bash
python main.py
```

### 3. Ouvrir la carte

Ouvre le fichier `map.html` généré dans ton navigateur.

---

## 📚 Ressources

- [Documentation Folium](https://python-visualization.github.io/folium/)
- [Plugins Folium](https://python-visualization.github.io/folium/plugins.html)
- [Trouver des coordonnées GPS](https://www.latlong.net/)

---

## 📄 Licence

MIT
