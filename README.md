# Transports — le programme du Parti libéral français

Un site de sept pages qui fait deux choses : **décrire la politique française
des transports telle qu'elle est**, et **proposer une alternative libérale**,
mesure par mesure, avec ses chiffres, ses sources, ses objections et ses
limites.

C'est le volet transports d'un programme dont le volet retraites est
[retraitecomptenotionelle](https://github.com/g-pliberal/retraitecomptenotionelle)
et le volet santé [sante](https://github.com/g-pliberal/sante), et il en
reprend l'apparence : même affiche vert profond, mêmes capitales massives, même
or pour ce qui compte. Les volets d'un même programme doivent se reconnaître au
premier coup d'œil.

## Les pages

| Fichier | Ce qu'elle fait |
| --- | --- |
| `index.html` | Le programme : quatre engagements, la réforme en trois gestes, ce qu'elle change |
| `diagnostic.html` | Le système actuel : qui paie, ce que chacun voit, les six défauts qui se tiennent, et ce qu'il ne faut pas casser |
| `comparaisons.html` | Suisse, Allemagne, Italie, Royaume-Uni, Japon — cinq systèmes, dont un qui a échoué |
| `reforme.html` | Les six mesures, chacune avec son mécanisme, son effet, et l'objection la plus sérieuse qu'on lui oppose |
| `simulateur.html` | Ce que vos déplacements coûtent réellement, et par quels guichets |
| `objections.html` | Dix objections et leurs réponses, y compris les deux auxquelles nous répondons mal |
| `donnees.html` | Tous les chiffres du site, avec leur source, leur millésime et leur degré de fiabilité |

## Construire le site

```sh
python3 scripts/construire_site.py
```

Rien à installer : le script n'utilise que la bibliothèque standard, et écrit à
la racine les sept fichiers HTML que GitHub Pages sert tels quels.

**Les fichiers `*.html` de la racine sont engendrés.** Une correction faite
directement dans l'un d'eux disparaîtrait à la construction suivante : le texte
est dans `src/transports/pages.py`, les chiffres dans
`src/transports/donnees.py`, et le gabarit dans `src/transports/gabarit.py`. Un
témoin et une action GitHub vérifient que les pages du dépôt sont bien celles
que le script écrirait.

Pour le regarder dans un navigateur, il faut un serveur : le module JavaScript
et le paquet de données ne se chargent pas depuis `file://`.

```sh
python3 -m http.server 8765   # puis http://localhost:8765/
```

## Les témoins

```sh
python3 -m unittest discover -s tests
```

Ils vérifient ce qu'un site de programme politique ne peut pas se permettre de
rater : qu'aucune page engendrée n'a divergé de son texte, qu'aucun onglet ne
mène nulle part, que chaque chiffre cité paraît sur la page Données avec sa
source — **et qu'aucun chiffre écrit au fil d'une phrase n'échappe à la
table**, que chaque pays comparé porte son millésime et sa réserve, que toutes
les hypothèses du simulateur sont publiées et qu'il n'en cache aucune dans son
code, que chaque définition du glossaire sert quelque part, et qu'aucune page
ne charge de ressource tierce.

## Comment c'est fait

```
src/transports/donnees.py   les chiffres, leurs sources, leur fiabilité, les pays comparés
src/transports/gabarit.py   tout ce que le site écrit : bandeau, affiche, cartes, tableaux
src/transports/pages.py     le texte des sept pages
scripts/construire_site.py  assemble les pages et écrit moteur/donnees.json
moteur/style.css            la feuille de style, reprise du site retraites
moteur/js/site.js           le glossaire dépliable — tout le reste se lit sans JavaScript
moteur/js/simulateur.js     le seul calcul du site, dans le navigateur
moteur/polices/             Public Sans et Instrument Serif (OFL), servies par le dépôt
moteur/icones/              les pictogrammes originaux de Lucide (ISC)
```

Trois règles tiennent l'ensemble :

1. **Un chiffre n'existe qu'une fois.** Les pages l'appellent par sa clé ; la
   page « Données et sources » est engendrée par la même table. Un chiffre ne
   peut donc pas dire une chose ici et une autre là.
2. **Le site ne charge rien d'un tiers.** Polices, pictogrammes, feuille de
   style : tout vient du dépôt. Une requête vers un serveur extérieur
   emporterait l'adresse IP du lecteur, et la page du simulateur promet le
   contraire.
3. **Le simulateur calcule dans le navigateur.** Aucune saisie n'est
   transmise, enregistrée ni mesurée.

## Sur les chiffres

**Les chiffres marqués « à vérifier » sont de seconde main et doivent être
confrontés à leur source avant toute reprise publique.** Ils sont nombreux, et
c'est propre au domaine : en matière de transports, les périmètres comptables
varient d'une publication à l'autre — « le coût du ferroviaire » n'a pas le
même sens selon qu'on y compte l'infrastructure, la dette reprise ou les
retraites du régime spécial. Le site le dit lui-même, sur chaque rangée
concernée de la page Données, plutôt que dans une note que personne n'ouvre.
Les trois degrés de fiabilité sont définis en tête de
`src/transports/donnees.py` :

- **publié** — recopié d'une publication officielle nommée ;
- **ordre de grandeur** — arrondi, agrégé ou reconstitué ;
- **à vérifier** — de seconde main, à confronter à la source.

Le site ne chiffre pas la réforme à l'échelle du pays, et
[il explique pourquoi](reforme.html) : un tel chiffrage exigerait un modèle des
coûts d'exploitation ligne par ligne que personne ne publie — et que la
première mesure du programme vise précisément à rendre possible. Une économie
annoncée sans ce modèle serait inventée.

## Licences

- Code : Apache 2.0 (`LICENSE`).
- Textes et contenus du site : CC BY-SA 4.0.
- Polices : SIL Open Font License (`moteur/polices/`).
- Pictogrammes : [Lucide](https://lucide.dev), ISC (`moteur/icones/LICENSE`).
