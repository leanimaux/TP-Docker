V1: 
app-opti     v1        8311d8204551   1.73GB
V2(changemen de version node + sans copy de tout):  app-opti        v2        70cd30d1dd20   224MB
V3(changement de node env):
app-opti        v3        502f0259c136   240MB
V4(ajout d'un .dockerignore):
app-opti        v4        a85b7fe73646   224MB
V5(ajout d'1 utilisateur):
app-opti        v5        70178e877cc5   248MB

A faire:
    - Ne pas mettre latest en version
    - Ne pas copier tout node. Copier seulement les fichiers nécessaires à l'installation des deps, run, puis copy du reste.
    - Ne pas mettre node env deploiement: installe des dépendances inutiles. Mettre prod
    - Ajouter un .dockerignore pour empêcher Docker de copier des fichiers inutiles dans l’image.
    - Ajoute un utilisatuer pour que le container lance le serveur grâce à cet utilisateur qui n'est pas admin (faille de sécu) 