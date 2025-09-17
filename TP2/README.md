# Optimisation d’une application Node.js avec Docker

## Objectif
L’objectif est d’apprendre à construire, analyser et **optimiser progressivement** l’image Docker d’une application Node.js.  
Chaque étape correspond à une nouvelle version (`v1`, `v2`, etc.).

---

## Versions et évolutions

### **V1 – Image initiale**
- **Base** : `node:latest`  
- **Actions** : copie complète du projet, installation des dépendances.  
- **Résultat** : **1.73 GB**  
- **Problèmes** : image énorme, pas de gestion d’environnement, mauvaises pratiques (copie inutile, `latest` non figé, etc.).

---

### **V2 – Réduction de l’image**
- **Base** : `node:18-alpine` (plus légère que `latest`)  
- **Actions** : copie uniquement des fichiers `package*.json` avant l’installation.  
- **Résultat** : **224 MB**  
- **Impact** : gain massif de place (~1.5 GB économisés).

---

### **V3 – Ajustement de NODE_ENV**
- **Actions** : passage de `NODE_ENV=development` à `NODE_ENV=production`.  
- **Résultat** : **240 MB**  
- **Impact** : évite l’installation de dépendances inutiles (ex : `nodemon`).

---

### **V4 – Ajout d’un `.dockerignore`**
- **Actions** : exclusion de fichiers inutiles (`node_modules/`, `logs/`, `.git/`, etc.).  
- **Résultat** : **224 MB**  
- **Impact** : image plus propre, build plus rapide.

---

### **V5 – Sécurité (utilisateur non-root)**
- **Actions** : ajout d’un utilisateur dédié pour exécuter l’application.  
- **Résultat** : **248 MB**  
- **Impact** : meilleure sécurité (évite que le conteneur tourne en root).

---

### **V6 – Multi-stage build**
- **Actions** : séparation en deux étapes :  
  1. **build** → installation des dépendances et build complet  
  2. **runtime** → image finale plus légère avec uniquement ce qui est nécessaire à l’exécution.  
- **Résultat** : **222 MB**  
- **Impact** : image plus petite, plus sécurisée, meilleure maintenabilité.

---

## Bonnes pratiques appliquées
- Ne pas utiliser `latest` (toujours fixer une version, ex: `node:18-alpine`).  
- Ne pas copier tout le projet : copier d’abord `package*.json`, installer, puis copier le reste.  
- Toujours définir `NODE_ENV=production` en déploiement.  
- Ajouter un `.dockerignore` pour éviter les fichiers inutiles.  
- Créer un utilisateur non-root pour exécuter l’application.  
- Utiliser un **multi-stage build** pour séparer build et exécution.

---

## Résumé des tailles d’image
| Version | Taille  | Optimisation clé |
|---------|---------|------------------|
| v1      | 1.73 GB | Image brute (mauvaises pratiques) |
| v2      | 224 MB  | Base alpine + copie sélective |
| v3      | 240 MB  | `NODE_ENV=production` |
| v4      | 224 MB  | `.dockerignore` |
| v5      | 248 MB  | Utilisateur non-root |
| v6      | 222 MB  | Multi-stage build |

---

## Conclusion
Grâce à ces optimisations successives :  
- La taille de l’image est passée de **1.73 GB → 222 MB**.  
- L’image est **plus rapide à construire**, **plus sécurisée**, et **plus adaptée à la production**.  
