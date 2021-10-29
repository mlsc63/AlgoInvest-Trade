# AlgoInvest-Trade
## Résumé

Algoinvest, permet de définir la meilleure stratégie d'investissement avec une somme définis, et la contraite de ne pouvoir prendre qu'une fois l'action.
Les fichiers ou les actions sont stockées avec leurs valeurs et leurs profits, sont dans le répértoir data.
L'algorithme se compose en deux parties et repose sur le problème du sac à dos:
- Première partie -> Brute force: On essaie toutes les combinaisons possibles.
  L'emnssemble des combinaisons ce calcul par la formule 2^n, soit dans notre exemple 2^20=1048576 combinaisons.
- Deuxiéme partie -> Optimisation, voir la ressource https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_sac_%C3%A0_dos. 


### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `https://github.com/mlsc63/Python-OC-Lettings-FR-master.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter

- `cd /path/to/AlgoInvest-Trade`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `SacADos-BrutForce/main.py`
- `optimized/main.py`


