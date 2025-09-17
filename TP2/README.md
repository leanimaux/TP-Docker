V1 : 
app-opti     v1        8311d8204551   26 minutes ago   1.73GB
V2(changemen de version node + sans copy de tout):  app-opti        v2        70cd30d1dd20   2 minutes ago   224MB
V3(changement de node env):
app-opti        v3        502f0259c136   2 minutes ago    240MB


Mauvaises pratiques:
    - Mettre latest en version
    - copier tout node. Copier seulement les fichiers nécessaires à l'installation des deps, run, puis copy du reste.
    - node env deploiement: installe des dépendances inutiles. Mettre prod
    - 