# Nutrition Converter

Un outil Streamlit simple pour comparer les apports nutritionnels de différents aliments et estimer la dépense énergétique journalière (DEJ).

---

## Fonctionnalités

* **Convertisseur Macronutriments** :

  * Choix de la catégorie (glucides ou protéines).
  * Objectif (glucides, protéines ou calories).
  * Sélection d’un aliment de référence et d’une quantité en grammes (cru).
  * Option cuisson avec ajout d’huile (+90 kcal).
  * Affichage d’une fiche par aliment de la même catégorie avec quantité crue/cuite, macros et kcal.

* **Calculateur DEJ** :

  * Formule de Harris & Benedict révisée.
  * Paramètres : sexe, âge, taille, poids, facteur d’activité.
  * Résultat affiché sous forme de métrique.

---

## Prérequis

* Python 3.9+
* Conda (ou tout autre gestionnaire d’env.)

---

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/elValentinoCode/ConvertisseurMacronutriment.git
   cd ConvertisseurMacronutriment
   ```

2. Créez et activez l’environnement Conda :

   ```bash
   conda env create -f environment.yml
   conda activate nutrition_app
   ```

3. (Optionnel) Installez d’autres dépendances :

   ```bash
   pip install typing_extensions
   ```

---

## Lancement de l’application

```bash
streamlit run streamlit_app.py
```

* L’application s’ouvre automatiquement dans votre navigateur.
* Le logo apparaît dans l’onglet et la barre latérale.

---

## Génération d’un exécutable Windows

1. Convertissez votre logo PNG en ICO :

   ```bash
   # Avec ImageMagick
   convert logo.png logo.ico
   ```

2. Utilisez PyInstaller :

   ```bash
   pyinstaller \
     --onefile \
     --windowed \
     --name NutritionConverter \
     --icon logo.ico \
     --add-data "logo.png;." \
     --hidden-import=streamlit.web.bootstrap \
     streamlit_app.py
   ```

3. Récupérez l’exécutable dans `dist/NutritionConverter.exe`.

---

## Structure du projet

```
├── environment.yml      # Environnment Conda
├── logo.png             # Logo PNG
├── logo.ico             # Icône Windows (pour PyInstaller)
├── streamlit_app.py     # Script principal
├── README.md            # Documentation du projet
└── dist/                # Exécutables générés
```

---

## Licence

Ce projet est distribué sous la licence MIT. Vous êtes libre d’utiliser, copier ou modifier ce code.

