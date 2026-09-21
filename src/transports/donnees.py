"""Les chiffres du site, et rien qu'eux.

Un site politique se juge à ses chiffres. Celui-ci en cite une soixantaine :
s'ils étaient écrits dans les pages, personne — ni l'auteur, ni le lecteur, ni
le contradicteur — ne saurait dire d'où ils viennent ni quand ils ont été
relevés. Ils sont donc TOUS ici, chacun avec sa source, son millésime et son
degré de fiabilité, et les pages ne font que les appeler par leur clé.

Trois conséquences, et c'est pour elles que ce module existe :

* un chiffre ne peut pas dériver d'une page à l'autre — il n'existe qu'une
  fois ;
* la page « Données et sources » est ENGENDRÉE par cette table, et ne peut donc
  pas être en retard sur le texte ;
* un chiffre dont la fiabilité est « à vérifier » le dit partout où il paraît,
  et non dans une note de bas de page que personne n'ouvre.

**Sur la fiabilité.** Trois niveaux, et ils sont honnêtes :

``"publie"``
    Chiffre publié tel quel par une source officielle nommée (loi de finances,
    code des impositions, INSEE, Cour des comptes, ART, UTP, OCDE). Il est
    recopié, pas calculé.
``"ordre"``
    Ordre de grandeur : le chiffre est arrondi, agrégé ou reconstitué à partir
    de plusieurs publications. Il dit une magnitude, pas une valeur exacte.
``"verifier"``
    Chiffre de mémoire ou de seconde main, qu'il faut confronter à la source
    avant toute publication ou tout débat. Le site l'affiche en le disant.

**Le transport est le domaine où cette précaution compte le plus.** Les
périmètres y sont piégeux : « le coût du ferroviaire » n'a pas le même sens
selon qu'on compte l'infrastructure, l'exploitation, les retraites du régime
spécial ou la dette reprise ; « la part des transports publics » change de
valeur selon qu'on mesure des déplacements ou des kilomètres. Chaque rangée
dit donc ce qu'elle mesure, et ce qu'elle ne mesure pas.

Aucun chiffre n'est ici le produit d'un modèle : ce site ne modélise rien, il
compare un système à un autre. Le seul calcul qu'il fait est celui du
simulateur, et il est écrit dans ``moteur/js/simulateur.js``, à ciel ouvert.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Chiffre:
    """Un chiffre, ce qu'il mesure, d'où il vient et ce qu'il vaut."""

    cle: str
    valeur: str
    """Le chiffre TEL QU'IL S'ÉCRIT dans la page, unité comprise.

    C'est une chaîne et non un nombre, et c'est voulu : « 0,60 € par litre »,
    « ≈ 17 Md€ » et « 39 millions » ne se formatent pas de la même façon, et
    aucun code de mise en forme ne rattrape un chiffre mal arrondi à la source.
    """

    libelle: str
    """Ce que le chiffre mesure, en une ligne — l'étiquette sous le nombre."""

    annee: str
    source: str
    fiabilite: str = "publie"
    precision: str = ""
    """Ce qu'il faut savoir avant de le citer : périmètre, réserve, définition."""

    lien: str = ""

    def __post_init__(self) -> None:
        if self.fiabilite not in ("publie", "ordre", "verifier"):
            raise ValueError(f"fiabilité inconnue : {self.fiabilite}")


@dataclass(frozen=True)
class Pays:
    """Un système de transport étranger, tel qu'il se compare au nôtre."""

    nom: str
    drapeau: str
    investissement: str
    """Ce que le pays met dans son réseau ferré, par habitant et par an."""

    usager: str
    """Part du coût du transport public couverte par ceux qui l'empruntent."""

    modele: str
    """Le mécanisme, en une phrase."""

    annee: str = ""
    source: str = ""
    fiabilite: str = "verifier"
    """D'où viennent ces deux chiffres, et de quand.

    Un tableau de comparaison internationale sans millésime ni source est la
    pièce la plus facile à retourner contre celui qui la publie : les
    périmètres comptables diffèrent d'un pays à l'autre, les éditions se
    succèdent, et deux chiffres vrais pris dans deux éditions différentes font
    un tableau faux.
    """

    detail: list[str] = field(default_factory=list)
    lecon: str = ""
    reserve: str = ""
    """Ce qui interdit de lire la ligne de ce pays comme une mesure exacte."""


# -- les chiffres ------------------------------------------------------------
#
# L'ordre est celui de la lecture : ce que le transport coûte au contribuable,
# ce qu'il prélève sur l'usager, ce que produit le réseau, et ce qui ne marche
# pas.

CHIFFRES: tuple[Chiffre, ...] = (
    # -- ce que la collectivité verse ---------------------------------------
    Chiffre(
        cle="concours_ferroviaire",
        valeur="≈ 17 Md€",
        libelle="de concours publics au système ferroviaire, par an",
        annee="2022",
        source="Cour des comptes, rapport sur les concours publics au "
        "transport ferroviaire",
        fiabilite="verifier",
        precision="Le total additionne les subventions d'exploitation versées "
        "par les régions pour les TER, les concours de l'État à SNCF Réseau, "
        "la compensation du régime spécial de retraite et les investissements "
        "d'infrastructure. Le périmètre retenu change le total du simple au "
        "double : une comparaison qui ne le précise pas ne vaut rien.",
        lien="https://www.ccomptes.fr/",
    ),
    Chiffre(
        cle="versement_mobilite",
        valeur="≈ 10 Md€",
        libelle="de versement mobilité payé par les employeurs, par an",
        annee="2023",
        source="URSSAF / Union des transports publics, données annuelles",
        fiabilite="verifier",
        precision="Le versement mobilité est un prélèvement assis sur la masse "
        "salariale des employeurs de onze salariés et plus, dont le taux est "
        "fixé par l'autorité organisatrice — jusqu'à 2,95 % en Île-de-France. "
        "C'est la première ressource des transports urbains, et elle "
        "n'apparaît sur aucun ticket.",
    ),
    Chiffre(
        cle="ticpe",
        valeur="≈ 30,5 Md€",
        libelle="de taxe sur les carburants (TICPE) perçus en un an",
        annee="2025",
        source="FIPECO, « Les taxes sur les carburants », d'après les comptes "
        "nationaux",
        fiabilite="ordre",
        precision="Quatrième impôt de l'État par le rendement. Contrairement "
        "à ce qui se dit souvent — et à ce que ce site a lui-même écrit avant "
        "de le vérifier —, ce produit ne part pas tout entier au budget "
        "général : l'État en conserve environ 16,3 Md€, les collectivités en "
        "reçoivent environ 12,1 Md€ et l'agence de financement des "
        "infrastructures environ 1,2 Md€. Ce qui reste vrai, c'est "
        "qu'aucune de ces fractions n'est liée à une dépense "
        "d'infrastructure identifiée : une recette affectée à un budget n'est "
        "pas une recette affectée à une route.",
        lien="https://www.fipeco.fr/fiche/Les-taxes-sur-les-carburants",
    ),
    Chiffre(
        cle="ticpe_gazole",
        valeur="0,5940 € par litre",
        libelle="de TICPE sur le gazole routier, tarif normal",
        annee="2026",
        source="Code des impositions sur les biens et services, art. L312-35 ; "
        "tarif 2026 relevé via FIPECO",
        fiabilite="publie",
        precision="Tarif de métropole hors régimes particuliers et hors "
        "majoration régionale, que les régions peuvent porter jusqu'à deux "
        "centimes et demi par litre. La TVA à 20 % s'applique ensuite sur un "
        "prix qui comprend déjà cette accise : l'impôt est donc taxé.",
        lien="https://www.legifrance.gouv.fr/codes/id/LEGITEXT000044595989/",
    ),
    Chiffre(
        cle="ticpe_essence",
        valeur="0,6829 € par litre",
        libelle="de TICPE sur l'essence SP95-E5, tarif normal",
        annee="2026",
        source="Code des impositions sur les biens et services, art. L312-35 ; "
        "tarif 2026 relevé via FIPECO",
        fiabilite="publie",
        precision="L'écart avec le gazole — près de neuf centimes par litre — "
        "est ce qui subsiste de l'avantage fiscal consenti au diesel.",
    ),
    Chiffre(
        cle="part_taxes_carburant",
        valeur="≈ 55 %",
        libelle="du prix du litre à la pompe, en taxes",
        annee="2024",
        source="Ministère de la transition écologique, prix hebdomadaires des "
        "carburants",
        fiabilite="ordre",
        precision="TICPE et TVA réunies, à un prix du baril moyen. La part "
        "varie mécaniquement avec le cours du pétrole : elle monte quand le "
        "brut baisse, et l'inverse.",
    ),
    Chiffre(
        cle="depense_publique_transports",
        valeur="≈ 30 Md€",
        libelle="de concours publics aux transports, tous réseaux confondus",
        annee="2023",
        source="Reconstitution : concours au ferroviaire, versement mobilité "
        "et subventions des collectivités aux réseaux urbains",
        fiabilite="verifier",
        precision="Agrégat reconstitué pour donner un ordre de grandeur par "
        "habitant, et rien de plus. Il additionne des sources qui ne "
        "partagent ni le même périmètre ni le même millésime, et il ne "
        "comprend ni l'entretien routier des collectivités, ni les dépenses "
        "fiscales.",
    ),
    Chiffre(
        cle="afit",
        valeur="≈ 4 Md€",
        libelle="de budget annuel de l'agence de financement des infrastructures",
        annee="2024",
        source="AFIT France, budget initial",
        fiabilite="verifier",
        precision="L'AFIT France finance la part de l'État dans les "
        "infrastructures de transport. Elle est alimentée par une fraction de "
        "TICPE, la taxe d'aménagement du territoire due par les "
        "concessionnaires d'autoroutes, le produit des radars et la taxe sur "
        "les infrastructures de transport de longue distance.",
    ),
    # -- ce que l'usager paie, et ce qu'il ne paie pas ----------------------
    Chiffre(
        cle="recettes_usagers_urbain",
        valeur="≈ 20 %",
        libelle="du coût des réseaux urbains de province payés par les billets",
        annee="2023",
        source="Union des transports publics, observatoire de la mobilité",
        fiabilite="verifier",
        precision="Le reste vient du versement mobilité et des budgets des "
        "collectivités. Le taux moyen a reculé depuis vingt ans, à mesure que "
        "l'offre et la gratuité progressaient plus vite que la "
        "fréquentation.",
    ),
    Chiffre(
        cle="recettes_usagers_ter",
        valeur="≈ 25 %",
        libelle="du coût d'un TER payé par le voyageur",
        annee="2023",
        source="Autorité de régulation des transports, rapport annuel sur le "
        "marché ferroviaire",
        fiabilite="verifier",
        precision="Les trois quarts restants sont versés par la région au "
        "titre du contrat d'exploitation. Le taux varie fortement d'une "
        "région et d'une ligne à l'autre : sur les lignes les moins "
        "fréquentées, la recette commerciale couvre moins d'un dixième du "
        "coût.",
    ),
    Chiffre(
        cle="idfm_budget",
        valeur="≈ 12 Md€",
        libelle="de budget annuel pour les transports d'Île-de-France",
        annee="2024",
        source="Île-de-France Mobilités, budget primitif",
        fiabilite="verifier",
        precision="Financé pour près de la moitié par le versement mobilité, "
        "pour environ un tiers par les voyageurs, le reste par les "
        "collectivités et des taxes affectées.",
    ),
    Chiffre(
        cle="part_budget_menages",
        valeur="≈ 14 %",
        libelle="du budget des ménages consacré aux transports",
        annee="2022",
        source="INSEE, comptes nationaux — consommation des ménages",
        fiabilite="ordre",
        precision="Deuxième poste après le logement. L'essentiel en est "
        "l'automobile : achat, carburant, entretien, assurance.",
    ),
    Chiffre(
        cle="cout_km_voiture",
        valeur="≈ 0,45 € par km",
        libelle="de coût de revient complet d'une voiture particulière",
        annee="2023",
        source="Barème kilométrique de l'administration fiscale, véhicule "
        "moyen",
        fiabilite="ordre",
        precision="Amortissement, carburant, entretien, assurance et "
        "réparations compris. Le barème fiscal en est une approximation "
        "conventionnelle, pas une mesure.",
    ),
    Chiffre(
        cle="peages_ca",
        valeur="≈ 11 Md€",
        libelle="de péages perçus par les concessionnaires d'autoroutes",
        annee="2023",
        source="Autorité de régulation des transports, rapport sur "
        "l'économie des concessions autoroutières",
        fiabilite="verifier",
        precision="Les concessions historiques arrivent à échéance entre 2031 "
        "et 2036. Ce qu'on en fera — nouvelle concession, régie, péage "
        "d'usage généralisé — est la décision de politique des transports la "
        "plus lourde de la décennie, et elle n'est pas prise.",
    ),
    # -- le réseau, ce qu'il est --------------------------------------------
    Chiffre(
        cle="reseau_ferre",
        valeur="≈ 27 000 km",
        libelle="de lignes ferroviaires exploitées",
        annee="2023",
        source="SNCF Réseau, chiffres clés du réseau",
        fiabilite="ordre",
        precision="Deuxième réseau d'Europe par la longueur, derrière "
        "l'Allemagne. Il en comptait près de 40 000 km au milieu du "
        "XXe siècle.",
    ),
    Chiffre(
        cle="petites_lignes",
        valeur="≈ 12 000 km",
        libelle="de lignes peu circulées (catégories UIC 7 à 9)",
        annee="2023",
        source="SNCF Réseau / rapport Philizot sur les petites lignes",
        fiabilite="verifier",
        precision="Près de la moitié du réseau, pour une faible part du "
        "trafic. Leur remise en état relève de contrats entre l'État et les "
        "régions, signés ligne par ligne et rarement financés jusqu'au bout.",
    ),
    Chiffre(
        cle="age_voies",
        valeur="≈ 29 ans",
        libelle="d'âge moyen des voies du réseau ferré national",
        annee="2022",
        source="SNCF Réseau, indicateurs de l'état du réseau",
        fiabilite="verifier",
        precision="Contre une quinzaine d'années sur les réseaux allemand et "
        "suisse. Un réseau vieillit quand on y investit moins qu'il ne "
        "s'use ; les ralentissements imposés pour cause de voie dégradée en "
        "sont la mesure la plus directe.",
    ),
    Chiffre(
        cle="ponts_degrades",
        valeur="≈ 25 000 ponts",
        libelle="en mauvais état structurel sur le réseau routier",
        annee="2019",
        source="Sénat, mission d'information sur la sécurité des ponts",
        fiabilite="verifier",
        precision="Sur un parc estimé entre 200 000 et 250 000 ouvrages, dont "
        "la plupart appartiennent aux communes et aux départements. Le "
        "rapport soulignait qu'aucune collectivité ne tient d'inventaire "
        "complet du sien.",
    ),
    Chiffre(
        cle="parc_automobile",
        valeur="≈ 39 millions",
        libelle="de voitures particulières en circulation",
        annee="2023",
        source="Service des données et études statistiques (SDES), parc "
        "automobile",
        fiabilite="ordre",
    ),
    Chiffre(
        cle="part_voiture_travail",
        valeur="≈ 74 %",
        libelle="des actifs qui vont travailler en voiture",
        annee="2021",
        source="INSEE, recensement de la population — déplacements "
        "domicile-travail",
        fiabilite="ordre",
        precision="Un actif sur six emprunte les transports en commun, et "
        "l'écart est d'abord géographique : la voiture domine partout hors "
        "des grandes agglomérations.",
    ),
    Chiffre(
        cle="fret_ferroviaire",
        valeur="≈ 9 %",
        libelle="des marchandises transportées par le rail en France",
        annee="2024",
        source="Autorité de régulation des transports, bilan du marché "
        "ferroviaire France-Europe 2024",
        fiabilite="publie",
        precision="Part du transport terrestre de marchandises mesurée en "
        "tonnes-kilomètres. Elle a été divisée par deux en vingt-cinq ans, "
        "alors qu'elle progressait en Allemagne et en Autriche sur la même "
        "période.",
        lien="https://www.autorite-transports.fr/wp-content/uploads/2026/06/"
        "art-bilan-ferroviaire-france-europe-2024.pdf",
    ),
    Chiffre(
        cle="fret_ue",
        valeur="≈ 16,9 %",
        libelle="la moyenne européenne du fret ferroviaire",
        annee="2024",
        source="Autorité de régulation des transports, bilan du marché "
        "ferroviaire France-Europe 2024, d'après Eurostat",
        fiabilite="publie",
        precision="La moyenne européenne recule elle aussi — de trois "
        "dixièmes de point en un an. La France ne décroche pas d'un peloton "
        "qui avance : elle est deux fois plus bas dans un peloton qui "
        "ralentit.",
        lien="https://www.autorite-transports.fr/wp-content/uploads/2026/06/"
        "art-bilan-ferroviaire-france-europe-2024.pdf",
    ),
    Chiffre(
        cle="emissions_transports",
        valeur="≈ 30 %",
        libelle="des émissions françaises de gaz à effet de serre",
        annee="2022",
        source="CITEPA, inventaire national Secten",
        fiabilite="ordre",
        precision="Premier secteur émetteur, et le seul dont les émissions "
        "n'avaient pas baissé entre 1990 et 2019. La voiture particulière en "
        "représente un peu plus de la moitié.",
    ),
    # -- ce qui ne marche pas ------------------------------------------------
    Chiffre(
        cle="dette_reprise",
        valeur="35 Md€",
        libelle="de dette de SNCF Réseau reprise par l'État",
        annee="2020-2022",
        source="Loi de finances pour 2020, article 178",
        fiabilite="publie",
        precision="Reprise en deux temps : 25 Md€ en 2020, puis 10 Md€ en "
        "2022. La reprise a soldé une dette née du financement des lignes "
        "à grande vitesse par emprunt. Elle n'a rien changé à ce qui l'avait "
        "produite : un gestionnaire d'infrastructure dont les recettes ne "
        "couvrent pas les charges, et qui emprunte la différence.",
        lien="https://www.legifrance.gouv.fr/",
    ),
    Chiffre(
        cle="grand_paris_express",
        valeur="≈ 36 Md€",
        libelle="de coût prévisionnel du Grand Paris Express",
        annee="2023",
        source="Société des grands projets, estimation actualisée",
        fiabilite="verifier",
        precision="L'estimation initiale, en 2010, était de l'ordre de "
        "20 Md€. Les révisions successives n'ont jamais donné lieu à un "
        "nouveau vote : le projet est financé par une dette adossée à des "
        "taxes affectées, remboursable jusque dans les années 2070.",
    ),
    Chiffre(
        cle="lyon_turin",
        valeur="≈ 26 Md€",
        libelle="de coût annoncé pour la liaison Lyon-Turin, accès compris",
        annee="2023",
        source="Cour des comptes, rapport sur la liaison ferroviaire "
        "Lyon-Turin",
        fiabilite="verifier",
        precision="Le tunnel de base transfrontalier en représente environ la "
        "moitié ; les voies d'accès françaises ne sont ni financées, ni "
        "décidées. La Cour relevait que les prévisions de trafic n'avaient "
        "jamais été réactualisées de façon contradictoire.",
    ),
    Chiffre(
        cle="cout_congestion",
        valeur="≈ 17 Md€",
        libelle="de coût annuel estimé de la congestion routière",
        annee="2018",
        source="Estimation de seconde main, reprise de travaux de conseil "
        "privés",
        fiabilite="verifier",
        precision="Ce type d'estimation valorise du temps perdu à un prix "
        "conventionnel : elle dit un ordre de grandeur, pas une dépense. "
        "Nous la citons pour situer l'enjeu, et elle ne fonde aucune de nos "
        "propositions.",
    ),
    Chiffre(
        cle="ponctualite_ter",
        valeur="≈ 91 %",
        libelle="des TER arrivés à l'heure",
        annee="2023",
        source="Autorité de régulation des transports, qualité de service",
        fiabilite="verifier",
        precision="Un train est compté à l'heure s'il arrive avec moins de "
        "cinq minutes de retard, et les trains supprimés ne sont pas comptés "
        "du tout — ce qui fait de cet indicateur le moins sévère des "
        "indicateurs possibles.",
    ),
    # -- ce que l'ouverture a produit ailleurs -------------------------------
    Chiffre(
        cle="baisse_couts_allemagne",
        valeur="≈ 25 %",
        libelle="de baisse du coût au train-kilomètre après mise en concurrence",
        annee="2015",
        source="Travaux académiques sur les appels d'offres régionaux "
        "allemands, cités de seconde main",
        fiabilite="verifier",
        precision="Mesure constatée sur les lots régionaux effectivement "
        "remis en concurrence, à service comparable. Ce chiffre a longtemps "
        "porté l'argumentaire de ce site ; il ne le porte plus. Depuis 2026, "
        "les résultats français des premiers lots TER sont publiés, et ils "
        "valent mieux qu'une référence étrangère de seconde main : c'est eux "
        "qu'il faut citer, et l'Allemagne ne sert plus ici qu'à montrer que "
        "le résultat n'est pas un accident français.",
    ),
    Chiffre(
        cle="baisse_prix_italie",
        valeur="≈ 40 %",
        libelle="de baisse du prix moyen sur Rome-Milan après l'ouverture",
        annee="2018",
        source="Autorité italienne des transports / travaux universitaires, "
        "cités de seconde main",
        fiabilite="verifier",
        precision="Mesurée entre 2012, date d'entrée du concurrent Italo, et "
        "la fin de la décennie, sur l'axe le plus fréquenté du pays. La "
        "fréquentation a plus que doublé sur la même période.",
    ),
    Chiffre(
        cle="cars_longue_distance",
        valeur="≈ 8 millions",
        libelle="de passagers annuels des autocars longue distance",
        annee="2019",
        source="Autorité de régulation des transports, marché du transport "
        "par autocar",
        fiabilite="verifier",
        precision="Ce marché n'existait pas avant la libéralisation de 2015 : "
        "les liaisons de plus de cent kilomètres y étaient interdites aux "
        "autocars pour protéger le train. Le trafic a reculé pendant "
        "l'épidémie, puis est reparti.",
    ),
    Chiffre(
        cle="ter_ouverts",
        valeur="≈ 20 %",
        libelle="de l'offre ferroviaire conventionnée attribuée après appel "
        "d'offres",
        annee="2026",
        source="Autorité de régulation des transports, étude annuelle sur "
        "l'ouverture à la concurrence des services ferroviaires, édition 2026",
        fiabilite="publie",
        precision="Part de l'offre, et non nombre de contrats : onze lots "
        "seulement ont été attribués, sur une soixantaine que la France doit "
        "remettre en concurrence d'ici au 25 décembre 2033. L'ouverture "
        "avance donc, mais par les plus gros lots et avec sept ans de retard "
        "sur son propre calendrier.",
        lien="https://www.autorite-transports.fr/communiques/"
        "ouverture-du-marche-ferroviaire-de-premiers-benefices-concrets-"
        "trois-defis-pour-les-perenniser/",
    ),
    # -- ce que l'ouverture a produit ICI ------------------------------------
    #
    # Ces rangées ont remplacé, en septembre 2026, l'argumentaire fondé sur
    # les seuls appels d'offres allemands. Un chiffre français, récent et
    # parlementaire vaut mieux qu'un chiffre étranger de seconde main — y
    # compris quand le rapport qui le porte est, au total, sévère.
    Chiffre(
        cle="baisse_couts_ter",
        valeur="20 à 30 %",
        libelle="de baisse des coûts de production sur les lots TER remis en "
        "concurrence",
        annee="2026",
        source="Sénat, rapport d'information n° 633 (2025-2026), "
        "« L'impact de la concurrence dans le ferroviaire sur les finances "
        "publiques », Marie-Claire Carrère-Gée et Hervé Maurey",
        fiabilite="publie",
        precision="Fourchette relevée par les rapporteurs sur les premiers "
        "lots attribués : −21 % sur l'étoile d'Amiens, −25 % en Pays de la "
        "Loire, −17 % de subvention en Nouvelle-Aquitaine, et une offre "
        "augmentée de 75 % à 100 % à coût constant en région Sud. Le même "
        "rapport conclut pourtant à un « bilan incertain » pour les finances "
        "publiques : les gains d'exploitation sont réels, les coûts de "
        "transition le sont aussi.",
        lien="https://www.senat.fr/rap/r25-633/r25-633_mono.html",
    ),
    Chiffre(
        cle="cout_transition_ter",
        valeur="50 à 70 M€",
        libelle="par atelier de maintenance neuf qu'impose un lot TER mis en "
        "concurrence",
        annee="2026",
        source="Sénat, rapport d'information n° 633 (2025-2026)",
        fiabilite="publie",
        precision="La région Sud anticipe environ 200 M€ à ce titre, la "
        "Nouvelle-Aquitaine environ 193 M€. S'y ajoutent l'indemnisation des "
        "candidats malheureux — jusqu'à 600 000 € par candidat — et le "
        "renforcement des services TER des régions, de l'ordre de dix "
        "spécialistes supplémentaires, soit 25 % à 30 % d'effectifs en plus. "
        "C'est le chiffre que ce site citait comme « réel et mal documenté » : "
        "il est désormais documenté, et il figure ici pour cette raison.",
        lien="https://www.senat.fr/rap/r25-633/r25-633_mono.html",
    ),
    Chiffre(
        cle="frequentation_ouverture",
        valeur="≈ 14 %",
        libelle="de hausse de la fréquentation ferroviaire depuis 2019",
        annee="2026",
        source="Autorité de régulation des transports, étude annuelle sur "
        "l'ouverture à la concurrence, édition 2026",
        fiabilite="publie",
        precision="Sur les lots conventionnés remis en concurrence, l'offre "
        "a augmenté de 30 % à 100 % à coûts identiques ou en baisse. "
        "L'ouverture n'a pas fait rouler moins de trains : elle en a fait "
        "rouler davantage pour le même argent.",
        lien="https://www.autorite-transports.fr/communiques/"
        "ouverture-du-marche-ferroviaire-de-premiers-benefices-concrets-"
        "trois-defis-pour-les-perenniser/",
    ),
    Chiffre(
        cle="prix_paris_lyon",
        valeur="≈ 10 %",
        libelle="de baisse du prix moyen sur Paris-Lyon depuis l'ouverture",
        annee="2026",
        source="Autorité de régulation des transports, étude annuelle sur "
        "l'ouverture à la concurrence, édition 2026",
        fiabilite="publie",
        precision="Mesurée entre 2019 et 2024 sur l'axe où un second "
        "opérateur fait rouler ses propres trains, quand les prix "
        "progressaient d'environ 10 % sur l'ensemble du réseau. La "
        "fréquentation de l'axe a augmenté de 20 % sur la même période. "
        "C'est l'équivalent français de ce que l'Italie a connu sur "
        "Rome-Milan, et il n'est plus nécessaire d'aller le chercher à "
        "l'étranger.",
        lien="https://www.autorite-transports.fr/communiques/"
        "ouverture-du-marche-ferroviaire-de-premiers-benefices-concrets-"
        "trois-defis-pour-les-perenniser/",
    ),
    Chiffre(
        cle="accise_electricite",
        valeur="0,0306 € par kWh",
        libelle="d'accise sur l'électricité, tarif normal des ménages",
        annee="2026",
        source="Bulletin officiel des finances publiques, tarifs d'accise "
        "applicables en 2026",
        fiabilite="publie",
        precision="Tarif applicable depuis le 1er août 2026, après 30,85 € "
        "par MWh de février à juillet. Un véhicule électrique acquitte cette "
        "accise sur ce qu'il consomme : rapporté au kilomètre, c'est environ "
        "six fois moins que ce qu'un véhicule thermique paie sur son "
        "carburant — pour une usure de la chaussée qui, elle, ne diffère pas. "
        "Ce site employait jusqu'en septembre 2026 le tarif du bouclier "
        "tarifaire, périmé depuis deux ans.",
        lien="https://bofip.impots.gouv.fr/bofip/14903-PGP.html",
    ),
    # -- ce que coûte une réforme ratée --------------------------------------
    Chiffre(
        cle="ecotaxe_cout",
        valeur="≈ 1 Md€",
        libelle="dépensés pour une écotaxe poids lourds qui n'a jamais rien "
        "perçu",
        annee="2017",
        source="Cour des comptes, rapport public annuel 2017",
        fiabilite="ordre",
        precision="Environ 958 M€ d'indemnités versées au consortium "
        "Ecomouv', et de l'ordre de 70 M€ engagés par les administrations. "
        "La taxe a été suspendue en octobre 2013 après la fronde des "
        "« bonnets rouges », le contrat résilié en octobre 2014, et les 174 "
        "portiques installés n'ont jamais servi. La Cour y a vu un « échec de "
        "politique publique » et un « gâchis patrimonial, social et "
        "industriel ».",
        lien="https://www.ccomptes.fr/",
    ),
    Chiffre(
        cle="astreinte_air",
        valeur="10 M€ par semestre",
        libelle="d'astreinte prononcée contre l'État pour la pollution de "
        "l'air",
        annee="2021-2023",
        source="Conseil d'État, contentieux Les Amis de la Terre "
        "(n° 428409)",
        fiabilite="verifier",
        precision="Montant record, ramené ensuite à 5 M€ par semestre. Les "
        "valeurs limites de dioxyde d'azote, qui devaient être respectées "
        "depuis 2010, le sont toujours dépassées à Paris et à Lyon. C'est ce "
        "contentieux, et non une lubie administrative, qui a rendu les zones "
        "à faibles émissions obligatoires : toute proposition de les "
        "supprimer doit dire ce qui tient leur place.",
        lien="https://www.conseil-etat.fr/",
    ),
    Chiffre(
        cle="concessions_investissements",
        valeur="≈ 10 Md€",
        libelle="d'investissements restant dus par les concessionnaires avant "
        "la fin des contrats",
        annee="2024",
        source="Autorité de régulation des transports, rapport sur "
        "l'économie des concessions autoroutières, troisième édition",
        fiabilite="verifier",
        precision="Les sept concessions historiques s'achèvent entre 2031 "
        "(Sanef) et 2036 (Area), en passant par Escota en 2032, la SAPN en "
        "2033, Cofiroute en 2034 et APRR en 2035. Le régulateur alerte sur "
        "les obligations de fin de contrat, qui décident de l'état dans "
        "lequel le réseau reviendra à l'État.",
        lien="https://www.autorite-transports.fr/",
    ),
)

# Ce que les pages ont le droit d'écrire sans rangée dans la table : des
# tournures, des bornes de formulaire, des chiffres cités pour être réfutés.
# Chaque tolérance porte sa raison, et un témoin vérifie qu'elle sert encore.
CHIFFRES_TOLERES: dict[str, str] = {
    "68 millions": "Population résidente de la France, employée pour ramener "
                   "un total national à un habitant. INSEE, bilan "
                   "démographique.",
    "20 %": "Taux normal de la TVA, qui s'applique aux carburants et aux "
            "péages. Il figure aussi comme hypothèse du simulateur, avec sa "
            "source.",
    "10 %": "Taux réduit de TVA applicable aux billets de train et aux "
            "transports de voyageurs.",
    "100 km": "Dénominateur d'une unité de consommation — « litres aux "
              "100 km », « kWh aux 100 km » —, et non une distance affirmée. "
              "Il paraît dans les hypothèses du simulateur.",
    "2,95 %": "Plafond légal du taux de versement mobilité en Île-de-France, "
              "cité dans la précision de la rangée « versement mobilité ».",
}


PAR_CLE: dict[str, Chiffre] = {chiffre.cle: chiffre for chiffre in CHIFFRES}


def chiffre(cle: str) -> Chiffre:
    """Le chiffre de clé donnée. Une clé inconnue est une erreur de rédaction."""
    if cle not in PAR_CLE:
        raise KeyError(f"chiffre inconnu : {cle} (voir src/transports/donnees.py)")
    return PAR_CLE[cle]


def valeur(cle: str) -> str:
    """Le chiffre seul, pour l'écrire au fil d'une phrase."""
    return chiffre(cle).valeur


# -- les pays comparés -------------------------------------------------------
#
# Six, et c'est un choix. Ce sont les pays qui ont fait, avant nous, l'une des
# deux choses que ce programme propose : ouvrir l'exploitation ferroviaire à
# d'autres opérateurs, ou faire payer l'usage de la route plutôt que la
# possession du véhicule. Le Royaume-Uni y figure parce qu'il a échoué sur une
# partie du chemin : une comparaison qui ne retiendrait que les succès ne
# servirait qu'à convaincre ceux qui le sont déjà.
#
# La France y figure pour la même raison, et c'est la ligne la plus importante
# du tableau : elle a tenté la mesure 3 de ce programme, en 2013, et s'est
# cassé les dents dessus pour un milliard d'euros. Un programme qui citerait la
# redevance suisse sans citer l'écotaxe française choisirait ses exemples, et
# le premier contradicteur venu le lui dirait.

PAYS: tuple[Pays, ...] = (
    Pays(
        nom="Suisse",
        drapeau="🇨🇭",
        investissement="le plus élevé d'Europe par habitant",
        usager="environ la moitié du coût",
        modele="Un fonds d'infrastructure ferroviaire alimenté par des "
               "recettes affectées et votées, et une redevance poids lourds "
               "au kilomètre parcouru.",
        annee="2023",
        source="Office fédéral des transports, rapports sur le fonds "
               "d'infrastructure ferroviaire (FIF) et la RPLP",
        fiabilite="verifier",
        detail=[
            "L'entretien et le développement du réseau sont financés par un "
            "fonds permanent, dont les recettes sont inscrites dans la "
            "Constitution : une part de TVA, une part des accises sur les "
            "carburants, une contribution des cantons et le produit de la "
            "redevance poids lourds.",
            "La redevance sur le trafic des poids lourds liée aux prestations "
            "(RPLP) fait payer chaque camion au kilomètre parcouru et selon "
            "son poids et ses émissions. Une partie de son produit finance le "
            "rail : la route paie le report modal qu'on attend d'elle.",
            "Chaque extension du réseau passe par un vote, avec son coût et "
            "son calendrier. Les projets ne sont pas lancés avant d'être "
            "financés.",
        ],
        lecon="Ce n'est pas la dépense qui fait la qualité suisse, c'est la "
              "règle de financement : de l'argent affecté, voté, et une route "
              "lourde qui paie son usage.",
        reserve="La Suisse est un petit pays dense et riche, dont les "
                "recettes affectées relèvent d'un régime constitutionnel sans "
                "équivalent en France. Son taux de couverture par l'usager "
                "dépend fortement du périmètre retenu.",
    ),
    Pays(
        nom="Allemagne",
        drapeau="🇩🇪",
        investissement="supérieur au nôtre, en hausse depuis 2020",
        usager="variable selon les Länder",
        modele="Les Länder achètent les services régionaux par appels "
               "d'offres depuis 1996 ; l'opérateur historique en a perdu une "
               "partie, et les coûts ont baissé.",
        annee="2023",
        source="Monopolkommission, rapports sectoriels sur le rail ; "
               "travaux académiques sur les appels d'offres régionaux",
        fiabilite="verifier",
        detail=[
            "L'ouverture porte sur la concurrence POUR le marché : le Land "
            "définit le service, les horaires et les tarifs, puis met le lot "
            "en appel d'offres. Le voyageur ne choisit pas son opérateur ; "
            "c'est l'autorité qui choisit, et elle peut changer.",
            "Les coûts au train-kilomètre ont reculé sur les lots remis en "
            "concurrence, et l'offre a augmenté à budget constant.",
            "L'opérateur historique reste très présent : il remporte une "
            "bonne part des appels d'offres, ce qui est le signe que la "
            "concurrence marche, pas qu'elle échoue.",
        ],
        lecon="On peut ouvrir un service public à la concurrence sans changer "
              "ce que l'usager reçoit : c'est l'acheteur public qui change, "
              "pas le service.",
        reserve="Le réseau allemand souffre d'un sous-investissement "
                "d'infrastructure qui a dégradé la ponctualité depuis 2018. "
                "L'appel d'offres régional n'y est pour rien, mais il ne l'a "
                "pas empêché.",
    ),
    Pays(
        nom="Italie",
        drapeau="🇮🇹",
        investissement="soutenu, porté par le plan de relance européen",
        usager="élevé sur la grande vitesse",
        modele="Deux opérateurs en concurrence libre sur la grande vitesse "
               "depuis 2012 : mêmes voies, mêmes gares, billets séparés.",
        annee="2023",
        source="Autorità di regolazione dei trasporti ; travaux "
               "universitaires sur l'entrée d'Italo",
        fiabilite="verifier",
        detail=[
            "C'est la concurrence SUR le marché, et non pour le marché : deux "
            "entreprises font rouler leurs propres trains sur les mêmes axes, "
            "chacune à ses tarifs et à ses risques.",
            "Les prix ont fortement baissé sur l'axe Rome-Milan, la "
            "fréquentation a plus que doublé, et l'avion y a perdu la "
            "majorité de son trafic intérieur.",
            "L'opérateur historique n'a pas disparu : il a baissé ses prix, "
            "densifié ses horaires et gagné des voyageurs.",
        ],
        lecon="Là où la demande est dense, la concurrence entre trains fait "
              "baisser les prix plus sûrement qu'aucun tarif administré.",
        reserve="Ce résultat vaut pour un axe à très forte demande. Rien ne "
                "dit qu'il se reproduirait sur une ligne régionale, et "
                "personne ne le prétend.",
    ),
    Pays(
        nom="Royaume-Uni",
        drapeau="🇬🇧",
        investissement="en hausse, après deux décennies de retard",
        usager="le plus élevé d'Europe",
        modele="Privatisation par franchises en 1994, fréquentation doublée, "
               "puis retour progressif à l'exploitation publique depuis 2020.",
        annee="2024",
        source="Office of Rail and Road ; Williams-Shapps Plan for Rail "
               "(2021)",
        fiabilite="verifier",
        detail=[
            "La fréquentation a doublé entre 1995 et 2019, après un demi-"
            "siècle de déclin continu. Ce fait est établi, et il est rarement "
            "cité par les adversaires de l'ouverture.",
            "Les subventions publiques n'ont pas baissé, la structure du "
            "secteur était d'une complexité coûteuse, et la fragmentation "
            "entre gestionnaire d'infrastructure et exploitants a pesé sur la "
            "sécurité avant la renationalisation de Railtrack en 2002.",
            "Depuis 2020, les franchises ont été remplacées par des contrats "
            "de gestion, puis par un retour à l'exploitation publique sous "
            "l'enseigne Great British Railways.",
        ],
        lecon="Une mauvaise architecture de marché coûte plus cher qu'un "
              "monopole bien tenu. Ce que le Royaume-Uni démontre, c'est "
              "qu'on ne privatise pas un réseau sans décider d'abord qui "
              "porte le risque.",
        reserve="Le bilan britannique est disputé par les deux camps, et les "
                "comparaisons de coût public y sont sensibles au traitement "
                "des investissements. Nous le citons contre notre propre "
                "thèse, pas pour elle.",
    ),
    Pays(
        nom="France",
        drapeau="🇫🇷",
        investissement="sans objet : le dispositif n'a jamais fonctionné",
        usager="aucun — la taxe n'a jamais rien perçu",
        modele="Une redevance kilométrique sur les poids lourds, votée à "
               "l'unanimité, construite, puis abandonnée en 2013 sous la "
               "pression, avant d'avoir perçu un euro.",
        annee="2013-2017",
        source="Cour des comptes, rapport public annuel 2017",
        fiabilite="ordre",
        detail=[
            "L'écotaxe poids lourds était la jumelle française de la "
            "redevance suisse : faire payer le kilomètre parcouru et affecter "
            "le produit aux infrastructures. Le principe en avait été voté "
            "sans opposition.",
            "Cent soixante-quatorze portiques ont été installés, un "
            "consortium payé pour construire et exploiter le dispositif, puis "
            "la taxe a été suspendue en octobre 2013 devant la fronde des "
            "« bonnets rouges », et le contrat résilié un an plus tard.",
            "Le contribuable a versé environ 1 Md€ — indemnités et frais "
            "d'administration — pour une taxe qui n'a rien perçu. Les "
            "portiques sont toujours en place, et l'État les entretient.",
        ],
        lecon="Une réforme du financement des transports ne meurt pas de son "
              "économie : elle meurt de son acceptabilité. L'écotaxe est "
              "tombée parce qu'elle arrivait sans contrepartie visible, "
              "parce qu'elle frappait d'abord une profession organisée, et "
              "parce que son produit n'était lisible pour personne. C'est la "
              "leçon la plus chère de ce tableau, et c'est la nôtre.",
        reserve="Nous inscrivons notre propre pays au titre de l'échec, et ce "
                "n'est pas une coquetterie : la troisième mesure de ce "
                "programme est une cousine de l'écotaxe. Quiconque nous "
                "l'oppose a raison de le faire, et cette mesure doit être "
                "jugée sur ce qu'elle en a tiré — pas sur la promesse que "
                "cette fois sera différente.",
    ),
    Pays(
        nom="Japon",
        drapeau="🇯🇵",
        investissement="porté par des opérateurs privés rentables",
        usager="la quasi-totalité du coût d'exploitation",
        modele="La compagnie nationale a été découpée en 1987 en sociétés "
               "régionales privatisées, qui exploitent le réseau et "
               "l'immobilier des gares.",
        annee="2023",
        source="Ministère japonais des transports (MLIT) ; rapports annuels "
               "des sociétés JR",
        fiabilite="verifier",
        detail=[
            "Les sociétés des zones denses — JR East, JR Central, JR West — "
            "sont rentables sans subvention d'exploitation, et financent "
            "elles-mêmes leur renouvellement.",
            "Celles des zones peu peuplées ne le sont pas, et vivent de "
            "dotations : la privatisation n'a pas rendu rentable ce qui ne "
            "l'était pas.",
            "La dette héritée de l'ancienne compagnie nationale a été reprise "
            "par l'État, comme en France trente ans plus tard.",
        ],
        lecon="Un opérateur ferroviaire peut vivre de ses recettes là où la "
              "demande est là — et nulle part ailleurs. La densité décide, "
              "pas le statut.",
        reserve="La densité urbaine japonaise et le rôle immobilier des "
                "opérateurs n'ont aucun équivalent français. C'est la "
                "comparaison la plus fragile de ce tableau.",
    ),
)


# -- le simulateur -----------------------------------------------------------
#
# Ses paramètres sont ici, et nulle part ailleurs : `scripts/construire_site.py`
# les dépose dans `moteur/donnees.json`, que la page lit au chargement. Le taux
# qu'affiche la page « Données et sources » et celui qu'applique le calcul sont
# donc le même nombre, et ne peuvent pas diverger. Un témoin vérifie qu'aucune
# constante ne s'est glissée dans le JavaScript.

PARAMETRES_SIMULATEUR: dict[str, object] = {
    "ticpe_gazole_litre": 0.5940,
    "ticpe_essence_litre": 0.6829,
    "tva": 0.20,
    "conso_gazole_100km": 5.8,
    "conso_essence_100km": 6.8,
    "accise_electricite_kwh": 0.0306,
    "conso_electrique_100kwh": 17.0,
    "population": 68_000_000.0,
    "actifs_occupes": 28_000_000.0,
    "concours_publics_transports": 30_000_000_000.0,
    # Ces deux derniers ne sont PAS additionnés au reste par le simulateur, et
    # ne peuvent pas l'être : voir RESERVES_SIMULATEUR et le commentaire de
    # `reperesCollectifs` dans moteur/js/simulateur.js.
    "versement_mobilite_total": 10_000_000_000.0,
    "part_recettes_usagers_urbain": 0.20,
    "part_recettes_usagers_ter": 0.25,
    "redevance_usage_km": 0.04,
}

# Chaque paramètre porte son unité et la phrase qui le décrit : la page
# « Données et sources » est engendrée depuis cette table, et un paramètre
# ajouté au calcul sans description casse la construction. Un simulateur dont
# une hypothèse ne figure pas dans la page qui prétend les donner toutes n'est
# pas vérifiable.
DESCRIPTIONS_SIMULATEUR: dict[str, tuple[str, str]] = {
    "ticpe_gazole_litre": ("euros_litre", "Accise sur le gazole routier, "
                           "tarif normal de métropole"),
    "ticpe_essence_litre": ("euros_litre", "Accise sur l'essence SP95-E5, "
                            "tarif normal de métropole"),
    "tva": ("part", "Taux normal de TVA, qui s'applique au prix du carburant "
            "accise comprise"),
    "conso_gazole_100km": ("litres", "Consommation moyenne retenue pour une "
                           "voiture au gazole <strong>(ordre de "
                           "grandeur)</strong>"),
    "conso_essence_100km": ("litres", "Consommation moyenne retenue pour une "
                            "voiture à essence <strong>(ordre de "
                            "grandeur)</strong>"),
    "accise_electricite_kwh": ("euros_litre", "Accise sur l'électricité, par "
                               "kilowattheure <strong>(ordre de "
                               "grandeur)</strong>"),
    "conso_electrique_100kwh": ("litres", "Consommation moyenne retenue pour "
                                "une voiture électrique, en kWh aux 100 km "
                                "<strong>(ordre de grandeur)</strong>"),
    "population": ("personnes", "Population résidente, qui sert à ramener un "
                   "total national à un habitant"),
    "actifs_occupes": ("personnes", "Actifs occupés, qui servent à ramener le "
                       "versement mobilité à un salarié <strong>(ordre de "
                       "grandeur)</strong>"),
    "concours_publics_transports": ("euros", "Concours publics annuels aux "
                                    "transports, tous réseaux confondus "
                                    "<strong>(agrégat reconstitué, qui "
                                    "COMPREND le versement mobilité et les "
                                    "subventions d'exploitation : il ne "
                                    "s'additionne donc à aucun des deux)"
                                    "</strong>"),
    "versement_mobilite_total": ("euros", "Produit annuel du versement "
                                 "mobilité payé par les employeurs"),
    "part_recettes_usagers_urbain": ("part", "Part du coût d'un réseau urbain "
                                     "couverte par les billets"),
    "part_recettes_usagers_ter": ("part", "Part du coût d'un TER couverte par "
                                  "le voyageur"),
    "redevance_usage_km": ("euros_litre", "Redevance kilométrique de "
                           "remplacement, par kilomètre parcouru "
                           "<strong>(hypothèse de travail)</strong>"),
}


def _francais(nombre: float, decimales: int) -> str:
    texte = f"{nombre:,.{decimales}f}".replace(",", " ").replace(".", ",")
    return texte.rstrip("0").rstrip(",") if decimales else texte


def parametre_affiche(cle: str) -> str:
    """La valeur d'un paramètre, TELLE QU'ELLE SE LIT dans la page.

    Elle est calculée depuis le paramètre lui-même, et non recopiée : une
    valeur recopiée à la main dans un tableau est une valeur qui finira par
    dire autre chose que le calcul.
    """
    valeur_lue = float(PARAMETRES_SIMULATEUR[cle])  # type: ignore[arg-type]
    unite = DESCRIPTIONS_SIMULATEUR[cle][0]
    if unite == "part":
        return _francais(valeur_lue * 100, 2) + " %"
    if unite == "euros":
        return _francais(valeur_lue / 1e9, 1) + " Md€"
    if unite == "euros_litre":
        return _francais(valeur_lue, 4) + " €"
    if unite == "personnes":
        return _francais(valeur_lue / 1e6, 1) + " millions"
    return _francais(valeur_lue, 1)


# Ce qu'il faut savoir avant de citer un résultat du simulateur. Une hypothèse
# de travail n'est pas une mesure, et une page qui les mélangerait tromperait
# son lecteur même en disant vrai partout ailleurs.
RESERVES_SIMULATEUR: tuple[tuple[str, str], ...] = (
    (
        "concours_publics_transports",
        "Le total des concours publics aux transports est un AGRÉGAT "
        "RECONSTITUÉ : il additionne des sources qui n'ont ni le même "
        "périmètre ni le même millésime, et il ne comprend ni l'entretien "
        "routier des collectivités ni les dépenses fiscales. Il sert à donner "
        "un ordre de grandeur par habitant, et rien de plus. Surtout : il "
        "COMPREND le versement mobilité et les subventions d'exploitation qui "
        "paient vos propres trajets. L'ajouter à ces deux montants "
        "compterait le même euro deux ou trois fois — ce que ce simulateur a "
        "fait jusqu'en septembre 2026, et ne fait plus. Il est désormais "
        "affiché comme repère, à côté du calcul, et jamais dedans.",
    ),
    (
        "redevance_usage_km",
        "La redevance kilométrique de remplacement est une HYPOTHÈSE DE "
        "TRAVAIL, calibrée sur ce qu'un véhicule THERMIQUE MOYEN acquitte "
        "aujourd'hui au kilomètre. Elle a donc une conséquence qu'il faut "
        "dire plutôt que la laisser découvrir : appliquée telle quelle, elle "
        "multiplierait par plus de six ce qu'un véhicule électrique paie "
        "aujourd'hui, qui est presque rien. C'est la logique même d'un prix "
        "d'usage — la route s'use sous un véhicule électrique comme sous un "
        "autre —, mais c'est aussi une hausse brutale pour des acheteurs qui "
        "ont choisi leur véhicule sous un autre régime fiscal. Le programme "
        "propose pour cette raison une entrée progressive, et le simulateur "
        "affiche l'écart sans l'adoucir. Son niveau réel dépendrait du "
        "périmètre retenu, de la modulation par zone et par heure, et d'un "
        "débat qui n'a pas eu lieu.",
    ),
    (
        "part_recettes_usagers_urbain",
        "Le taux de couverture par les billets varie du simple au double "
        "d'un réseau à l'autre, et la moyenne employée ici écrase cette "
        "différence. Un réseau gratuit a un taux nul ; le vôtre peut être "
        "très loin de la moyenne.",
    ),
    (
        "conso_gazole_100km",
        "Les consommations retenues sont des moyennes de parc. La vôtre "
        "dépend de votre véhicule, de votre trajet et de votre conduite : le "
        "simulateur ne la connaît pas, et ne cherche pas à la deviner.",
    ),
)
