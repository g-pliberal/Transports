#!/usr/bin/env python3
"""Écrit le site : sept pages HTML, et le paquet de données du simulateur.

    python3 scripts/construire_site.py

Rien à installer : le script n'utilise que la bibliothèque standard, et écrit
à la racine du dépôt les fichiers que GitHub Pages sert tels quels. Les pages
engendrées ne doivent jamais être corrigées à la main — la construction
suivante effacerait la correction. Le texte est dans
``src/transports/pages.py``, les chiffres dans ``src/transports/donnees.py``.
"""

from __future__ import annotations

import json
import pathlib
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "src"))

from transports import donnees, gabarit, pages  # noqa: E402  (après sys.path)

# Chaque page : son fichier, son titre d'onglet, sa description pour les
# moteurs de recherche et les aperçus de partage, et la fonction qui l'écrit.
# L'ordre est celui de la navigation.
PAGES = (
    ("index.html",
     "Transports : le programme du Parti libéral français",
     "Votre billet de train régional paie le quart de votre trajet ; le reste "
     "vient de la région, de l'État et des employeurs, sans que vous le "
     "voyiez jamais. Notre programme : mettre chaque contrat en concurrence, "
     "publier le coût de chaque ligne, payer l'usage de la route plutôt que "
     "sa possession, et tarifer les nuisances au lieu d'interdire les "
     "véhicules.",
     pages.programme),
    ("diagnostic.html",
     "Le système de transport actuel — qui paie, et ce que chacun voit",
     "Comment fonctionnent les transports français, qui les finance, et les "
     "six défauts qui se tiennent : un prix qui ne dit plus rien, des "
     "contrats sans prix de référence, la dette comme mode de financement, "
     "l'évaluation après la décision, l'entretien sacrifié, l'interdiction "
     "à la place du prix.",
     pages.diagnostic),
    ("comparaisons.html",
     "Ailleurs : cinq systèmes de transport, dont un qui a échoué",
     "Suisse, Allemagne, Italie, Royaume-Uni, Japon : financement affecté, "
     "appels d'offres régionaux, concurrence sur la grande vitesse, "
     "privatisation — et l'échec britannique des franchises, cité contre "
     "notre propre thèse.",
     pages.comparaisons),
    ("reforme.html",
     "La réforme, en six mesures",
     "Mettre chaque contrat d'exploitation en appel d'offres, publier le coût "
     "de chaque ligne, payer l'usage de la route plutôt que sa possession, "
     "tarifer les nuisances, contre-expertiser les grands projets avant de "
     "les voter, libérer l'offre de mobilité.",
     pages.reforme),
    ("simulateur.html",
     "Ce que vos déplacements vous coûtent vraiment — le simulateur",
     "Taxes sur le carburant, péages, abonnement, subvention de vos propres "
     "trajets, concours publics, versement mobilité : six flux, dont quatre "
     "invisibles. Le simulateur les additionne dans votre navigateur, sans "
     "rien envoyer nulle part.",
     pages.simulateur),
    ("objections.html",
     "Les dix objections, y compris les bonnes",
     "Fiasco britannique, fermeture des petites lignes, rentabilité, vie "
     "privée, ruraux, zones à faibles émissions, conditions de travail, "
     "absence de chiffrage : les dix objections les plus sérieuses à ce "
     "programme, et nos réponses — y compris quand elles sont incomplètes.",
     pages.objections),
    ("donnees.html",
     "Données et sources",
     "Tous les chiffres cités sur ce site, avec leur source, leur millésime "
     "et leur degré de fiabilité — publié, ordre de grandeur, ou à vérifier.",
     pages.page_donnees),
)

# Le simulateur est la seule page qui charge un second module : les autres se
# lisent sans JavaScript, et doivent continuer de le faire.
SCRIPTS = {
    "simulateur.html": '\n<script type="module" src="moteur/js/simulateur.js"></script>',
}


def paquet_donnees() -> dict[str, object]:
    """Ce que le simulateur lit au chargement : ses paramètres et ses réserves.

    Il est écrit depuis ``donnees.py`` pour la même raison que le reste : une
    hypothèse qui vaut 20 % dans la page Données et 25 % dans le calcul ne
    serait découverte par personne.
    """
    return {
        "avertissement": "Écrit par scripts/construire_site.py depuis "
                         "src/transports/donnees.py. Ne pas modifier à la "
                         "main.",
        "parametres": donnees.PARAMETRES_SIMULATEUR,
        "reserves": [
            {"parametre": cle, "texte": texte}
            for cle, texte in donnees.RESERVES_SIMULATEUR
        ],
    }


def construire() -> int:
    ecrits = 0
    for fichier, titre, description, rendu in PAGES:
        corps = rendu()
        html = gabarit.page(fichier, titre, description, corps,
                            SCRIPTS.get(fichier, ""))
        (RACINE / fichier).write_text(html, encoding="utf-8")
        print(f"  {fichier:22} {len(html):>7} octets")
        ecrits += 1

    chemin = RACINE / "moteur" / "donnees.json"
    chemin.write_text(
        json.dumps(paquet_donnees(), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"  {'moteur/donnees.json':22} {chemin.stat().st_size:>7} octets")

    # Les pages de la navigation et les pages construites doivent être les
    # mêmes : un onglet qui pointe vers un fichier qui n'existe pas est une
    # erreur qu'aucun test d'apparence ne rattrape.
    manquantes = set(gabarit.PAGES) - {fichier for fichier, *_ in PAGES}
    if manquantes:
        raise SystemExit(f"navigation vers des pages non construites : {manquantes}")

    print(f"\n{ecrits} pages écrites dans {RACINE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(construire())
