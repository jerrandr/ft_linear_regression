# 🚗 ft_linear_regression

> Un projet d'introduction au **Machine Learning** de l'École 42 visant à prédire le prix d'un véhicule selon son kilométrage via un algorithme de régression linéaire entraîné par descente de gradient.

---

## 📌 À propos du projet

La **régression linéaire** est un modèle statistique qui établit la relation entre une variable d'entrée $x$ (le kilométrage) et une variable de sortie $y$ (le prix).

### 📐 Modèle mathématique

L'objectif est de trouver la droite optimale définie par la fonction d'hypothèse :

$$f(x) = \theta_0 + \theta_1 x$$

* **$\theta_0$** : Ordonnée à l'origine (*bias*)
* **$\theta_1$** : Pente (*weight*)

L'algorithme de **descente de gradient** ajuste progressivement les paramètres ($\theta_0, \theta_1$) en minimisant la fonction de coût (l'erreur entre les prédictions et les données réelles).

---

## 🚀 Installation & Exécution

Toutes les commandes d'administration et d'exécution sont centralisées dans le `Makefile`.

### 🛠️ Commandes principales

| Commande | Étape | Description |
| :--- | :--- | :--- |
| `make install` | 📦 **Configuration** | Crée l'environnement virtuel `.venv` et installe les dépendances requises. |
| `make train` | 🧠 **Entraînement** | Calcule les paramètres optimaux ($\theta_0, \theta_1$) et sauvegarde le modèle. |
| `make prediction` | 🔮 **Prédiction** | Prédit le prix d'un véhicule à partir d'un kilométrage saisi par l'utilisateur. |
| `make all` | ⚡ **Complet** | Enchaîne l'entraînement du modèle et le lancement du script de prédiction. |

---

## 🎁 Fonctionnalités Bonus

| Commande | Description |
| :--- | :--- |
| `make bonus` | Exécute à la fois l'interface graphique et l'évaluation globale du modèle. |
| `make precision` | Calcule et affiche les métriques d'évaluation du modèle (ex: $R^2$, MSE). |
| `make interface` | Ouvre l'interface visuelle (affichage de la droite de régression et des points de données). |