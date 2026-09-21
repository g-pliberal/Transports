# Les pictogrammes du site

Ils viennent tous de **[Lucide](https://lucide.dev) 1.46.0**, sous licence ISC
(`LICENSE`, à côté). Une seule grille — 24 × 24, trait de 2, extrémités et
jointures arrondies —, et rien qui soit dessiné à la main : c'est ce qui les
fait tenir ensemble à toutes les tailles, ce qu'un emoji ou un caractère
Unicode ne font pas, leur dessin changeant d'un système à l'autre.

**Les fichiers de ce dossier sont les originaux.** Le site ne les charge pas :
le gabarit écrit leur tracé DANS la page (`ICONES`, dans
`src/transports/gabarit.py`), parce que la page ne demande aucune ressource à
un tiers — un témoin du dépôt l'exige.

`../icone.svg` est l'icône du site elle-même : la même grille, le même trait,
le tracé de `train-front` posé sur un carré à l'arrondi de la charte.

## Les tracés employés

| Fichier | Où il sert |
| --- | --- |
| `train-front.svg` | l'icône du site, et le nom dans le bandeau — où la feuille de style lui préfère le carré de la charte et le masque |
| `chevron-down.svg` | les sections repliées |
| `triangle-alert.svg` | les avertissements et les réserves |

## Une réserve, et elle est écrite ici plutôt que tue

Les fichiers sont recopiés sans retouche depuis le dépôt de Lucide (et, pour
les deux communs aux autres volets, depuis le site
[Santé](https://github.com/g-pliberal/sante), qui les en tenait). Leur licence
ISC exige que la mention de droit d'auteur accompagne le code : elle est dans
`LICENSE`, et l'en-tête `@license` de chaque fichier n'a pas été retiré.
