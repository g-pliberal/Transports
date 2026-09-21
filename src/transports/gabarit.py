"""Le gabarit : tout ce que le site écrit, il l'écrit d'ici.

Le site est fait de sept pages statiques. Elles n'ont ni cadre commun, ni
serveur, ni bibliothèque : ce module tient lieu des trois. Chaque fragment de
page — le bandeau, l'affiche, une carte, un tableau — n'existe qu'ici, en un
seul exemplaire, et ``scripts/construire_site.py`` les assemble en fichiers
HTML que l'on peut ouvrir à la main, sans rien installer.

La mise en forme, elle, est celle du site *retraitecomptenotionelle* : mêmes
classes, même feuille de style, mêmes pictogrammes. Ce n'est pas une économie,
c'est le propos — les volets d'un même programme doivent se reconnaître.
"""

from __future__ import annotations

from html import escape as echapper

from . import donnees

DEPOT = "https://github.com/g-pliberal/Transports"
SITE_PARENT = "https://partiliberalfrancais.fr/"
SITE_RETRAITES = "https://github.com/g-pliberal/retraitecomptenotionelle"
SITE_SANTE = "https://github.com/g-pliberal/sante"

NOM_DU_SITE = "Transports : payer ce qu'on utilise"

# La navigation par FONCTION, et non par page : le constat, l'alternative, la
# preuve, la confiance. C'est l'ordre dans lequel un électeur pose ses
# questions — « qu'est-ce qui ne va pas ? », « que proposez-vous ? », « qu'est-ce
# que ça me fait ? », « d'où sortez-vous vos chiffres ? ».
GROUPES_NAVIGATION: tuple[tuple[str, tuple[tuple[str, str], ...]], ...] = (
    ("Le programme", (("index.html", "Programme"),)),
    ("Le constat", (("diagnostic.html", "Le système actuel"),
                    ("comparaisons.html", "Ailleurs"))),
    ("L'alternative", (("reforme.html", "La réforme"),
                       ("simulateur.html", "Ce que vous payez"),
                       ("objections.html", "Objections"))),
    ("La confiance", (("donnees.html", "Données et sources"),)),
)

PAGES = tuple(chemin for _, liens in GROUPES_NAVIGATION for chemin, _ in liens)


# -- pictogrammes ------------------------------------------------------------
#
# Tous de Lucide 1.46.0, sous licence ISC (voir moteur/icones/). Une seule
# grille — 24 × 24, trait de 2, extrémités arrondies —, et le tracé est écrit
# DANS la page : le site ne demande aucune ressource à un tiers, et une requête
# vers un serveur d'icônes emporterait l'adresse IP du lecteur.

ICONES: dict[str, str] = {
    "train-front": '<path d="M8 3.1V7a4 4 0 0 0 8 0V3.1" />'
                   '<path d="m9 15-1-1" /><path d="m15 15 1-1" />'
                   '<path d="M9 19c-2.8 0-5-2.2-5-5v-4a8 8 0 0 1 16 0v4c0 '
                   '2.8-2.2 5-5 5Z" />'
                   '<path d="m8 19-2 3" /><path d="m16 19 2 3" />',
    "chevron-down": '<path d="m6 9 6 6 6-6" />',
    "triangle-alert": '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 '
                      '4 21h16a2 2 0 0 0 1.73-3" /><path d="M12 9v4" />'
                      '<path d="M12 17h.01" />',
}

_ENVELOPPE = ('viewBox="0 0 24 24" fill="none" stroke="currentColor" '
              'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"')


def icone(nom: str, titre: str = "") -> str:
    """Un pictogramme dans la page.

    Sans ``titre``, il est décoratif : le texte à côté dit déjà ce qu'il dit, et
    le répéter ferait entendre deux fois la même chose à une synthèse vocale.
    """
    if nom not in ICONES:
        raise KeyError(f"pictogramme inconnu : {nom}")
    if titre:
        return (f'<svg class="icone" {_ENVELOPPE} role="img">'
                f"<title>{echapper(titre)}</title>{ICONES[nom]}</svg>")
    return (f'<svg class="icone" {_ENVELOPPE} aria-hidden="true" '
            f'focusable="false">{ICONES[nom]}</svg>')


# -- squelette ---------------------------------------------------------------


def navigation(page_active: str) -> str:
    def liens_du_groupe(liens: tuple[tuple[str, str], ...]) -> str:
        return "".join(
            f'<a href="{chemin}"'
            + (' aria-current="page"' if chemin == page_active else "")
            + f">{echapper(libelle)}</a>"
            for chemin, libelle in liens
        )

    return "".join(
        f'<span class="groupe"><span class="etiquette">{echapper(etiquette)}</span>'
        f'<span class="liens">{liens_du_groupe(liens)}</span></span>'
        for etiquette, liens in GROUPES_NAVIGATION
    )


def entete(page_active: str) -> str:
    """Le bandeau de tête, précédé du lien d'évitement.

    Le lien d'évitement est le premier élément parcouru au clavier : sans lui,
    atteindre le contenu depuis la barre d'adresse impose de traverser les sept
    onglets à chaque page.
    """
    return f"""<a class="evitement" href="#contenu">Aller au contenu</a>
<header class="bandeau"><div class="interieur">
  <p class="nom"><a href="index.html">{icone('train-front')}<span>{echapper(NOM_DU_SITE)}</span></a></p>
  <nav aria-label="Navigation principale">{navigation(page_active)}</nav>
</div></header>"""


def affiche(surtitre: str, titre: str, chapeau: str) -> str:
    """Le bloc de tête d'une page : sur-titre, titre massif, chapeau.

    C'est l'unité qui fait de chaque page une affiche, et elle est la même
    partout pour que les sept se reconnaissent comme un seul site. Le titre est
    mis en capitales par le STYLE, jamais dans le texte : une capitale écrite
    dans le texte se lit lettre par lettre sous certaines synthèses vocales.
    """
    return (f'<div class="affiche"><p class="surtitre">{echapper(surtitre)}</p>'
            f'<h1>{titre}</h1><p class="chapeau">{chapeau}</p></div>')


def pied() -> str:
    """Le pied de page : ce qu'il faut savoir avant de citer un chiffre d'ici."""
    return f"""<footer>
  <p><strong>Ce site est un document politique, pas une source officielle.</strong>
  Il compare la politique française des transports à une alternative libérale ;
  il ne vaut ni information tarifaire, ni conseil pour vos trajets. Pour ceux-ci,
  voir votre autorité organisatrice et
  <a href="https://www.service-public.fr/">service-public.fr</a>.</p>
  <p>Tous les chiffres cités sont rassemblés, datés et sourcés sur la page
  <a href="donnees.html">Données et sources</a>, avec leur degré de fiabilité.
  Ceux marqués « à vérifier » doivent être confrontés à leur source avant
  d'être repris dans un débat. Textes et code sur
  <a href="{DEPOT}">GitHub</a> (code sous licence Apache 2.0, textes sous
  <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.fr">CC BY-SA 4.0</a>).</p>
  <p class="retour-site">Un document du
  <a href="{SITE_PARENT}" target="_top">Parti libéral français</a>. Les autres
  volets du programme : <a href="{SITE_RETRAITES}">retraites</a> et
  <a href="{SITE_SANTE}">santé</a>.</p>
</footer>"""


def page(fichier: str, titre: str, description: str, corps: str,
         scripts: str = "") -> str:
    """Une page entière, de ``<!doctype>`` au pied.

    ``scripts`` porte les modules propres à la page — seule la page du
    simulateur en charge un. Les autres ne chargent que le script commun, qui
    ne fait qu'ouvrir les définitions du glossaire : une page de texte doit se
    lire sans JavaScript, et toutes le font.
    """
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- La couleur du bandeau de tête : sur un téléphone, la barre du navigateur
     la reprend, et la page commence où elle commence. -->
<meta name="theme-color" content="#0b3d3a">
<title>{echapper(titre)}</title>
<meta name="description" content="{echapper(description)}">
<link rel="icon" href="moteur/icone.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="moteur/icone.svg">
<link rel="stylesheet" href="moteur/style.css">
<!-- Écrit par scripts/construire_site.py depuis src/transports/. Ne pas
     modifier ici : la prochaine construction effacerait la correction. -->
</head>
<body>
{entete(fichier)}
<main id="contenu" tabindex="-1">
{corps}
</main>
{pied()}
<script type="module" src="moteur/js/site.js"></script>{scripts}
</body>
</html>
"""


# -- fragments ---------------------------------------------------------------


def surtitre(texte: str) -> str:
    return f'<p class="surtitre">{echapper(texte)}</p>'


def cle_texte(texte: str) -> str:
    """Ce qui compte dans une phrase, en or."""
    return f'<strong class="cle-texte">{texte}</strong>'


def mot(terme_affiche: str, definition: str) -> str:
    """Un mot de jargon, et sa définition dépliable sur place.

    Le site s'adresse à des gens qui n'ont pas lu le code des transports.
    « Versement mobilité », « open access », « AOM » sont pour eux des mots
    opaques, et les définir dans le corps du texte l'allonge d'autant pour tous
    les autres. La définition est donc posée SOUS le mot, et ne s'ouvre que si
    on la demande.

    Ce n'est pas un attribut ``title`` : une infobulle de survol ne s'ouvre ni
    au clavier, ni au doigt, ni sous une synthèse vocale. Ce n'est pas non plus
    un ``<details>``, qui refermerait le ``<p>`` en cours au milieu d'une
    phrase. C'est un ``<span role="button">``, qui est du contenu de phrase.
    """
    return ('<span class="mot"><span class="terme" role="button" tabindex="0" '
            f'aria-expanded="false">{echapper(terme_affiche)}</span>'
            f'<span class="bulle" role="note" hidden>{echapper(definition)}</span></span>')


GLOSSAIRE: dict[str, str] = {
    "AOM": "Autorité organisatrice de la mobilité : la collectivité qui "
           "décide du service de transport sur son territoire — les lignes, "
           "les horaires, les tarifs — et le paie. C'est la région pour les "
           "TER, l'intercommunalité pour les bus urbains, Île-de-France "
           "Mobilités en région parisienne.",
    "versement mobilité": "Un prélèvement assis sur la masse salariale des "
                          "employeurs d'au moins onze salariés, perçu au "
                          "profit de l'autorité organisatrice. C'est la "
                          "première ressource des transports urbains : il "
                          "finance plus de trajets que les billets, et "
                          "n'apparaît sur aucun ticket.",
    "TICPE": "Taxe intérieure de consommation sur les produits énergétiques : "
             "l'accise sur les carburants. Elle est due au litre, quel que "
             "soit l'endroit et l'heure où l'on roule, et son produit va au "
             "budget général — elle ne finance donc pas les routes.",
    "péage ferroviaire": "La redevance que l'exploitant d'un train verse au "
                         "gestionnaire de l'infrastructure pour emprunter la "
                         "voie. En France, elle est parmi les plus élevées "
                         "d'Europe, et c'est l'un des obstacles à l'entrée de "
                         "nouveaux opérateurs.",
    "open access": "La concurrence SUR le marché : un opérateur fait rouler "
                   "ses propres trains, à ses tarifs et à ses risques, sans "
                   "contrat avec une autorité. C'est ainsi que Trenitalia et "
                   "la Renfe sont entrées en France, et Italo en Italie.",
    "délégation de service public": "La concurrence POUR le marché : "
                                    "l'autorité définit le service, met le "
                                    "contrat en appel d'offres, et l'attribue "
                                    "pour quelques années. L'usager ne choisit "
                                    "pas l'opérateur ; l'autorité choisit à sa "
                                    "place, et peut en changer.",
    "obligation de service public": "Un service que le marché ne rendrait pas "
                                    "seul — un train tôt le matin, un arrêt "
                                    "dans un bourg — et que l'autorité achète "
                                    "explicitement, en le payant. C'est la "
                                    "forme honnête de la solidarité "
                                    "territoriale : elle est écrite, chiffrée "
                                    "et votée.",
    "ART": "Autorité de régulation des transports : le régulateur indépendant "
           "du ferroviaire, des autoroutes concédées, des autocars et des "
           "aéroports. Elle contrôle l'accès au réseau et publie les données "
           "que les opérateurs préféreraient garder.",
    "évaluation socio-économique": "Le calcul qui compare ce qu'un projet "
                                   "coûte à ce qu'il rapporte à la "
                                   "collectivité — temps gagné, accidents "
                                   "évités, émissions. Elle est obligatoire "
                                   "pour les grands projets, et son résultat "
                                   "n'a presque jamais empêché une décision "
                                   "déjà prise.",
    "ZFE": "Zone à faibles émissions : un périmètre urbain où la circulation "
           "est interdite aux véhicules trop anciens, classés par vignette. "
           "L'interdiction porte sur l'âge du véhicule, pas sur l'usage qu'on "
           "en fait : rouler mille kilomètres par an dans une vieille voiture "
           "y est interdit, en faire trente mille dans une neuve ne l'est "
           "pas.",
    "part modale": "La part d'un mode de transport dans l'ensemble des "
                   "déplacements ou des tonnes transportées. Elle change de "
                   "valeur selon qu'on compte des trajets, des kilomètres ou "
                   "des tonnes : une comparaison qui ne le précise pas ne "
                   "veut rien dire.",
    "train-kilomètre": "L'unité de production ferroviaire : un train qui "
                       "parcourt un kilomètre. Les coûts d'exploitation se "
                       "comparent d'un réseau à l'autre en euros par "
                       "train-kilomètre, à service comparable.",
}


def terme(mot_affiche: str, cle: str = "") -> str:
    """Un mot du glossaire, écrit au fil du texte."""
    definition = GLOSSAIRE[cle or mot_affiche]
    return mot(mot_affiche, definition)


_FIABILITES = {
    "publie": ("Chiffre publié", "Recopié d'une publication officielle nommée."),
    "ordre": ("Ordre de grandeur", "Arrondi ou reconstitué : il dit une "
                                   "magnitude, pas une valeur exacte."),
    "verifier": ("À vérifier", "De seconde main : à confronter à la source "
                               "avant toute citation."),
}


def etiquette_fiabilite(niveau: str) -> str:
    libelle, explication = _FIABILITES[niveau]
    return (f'<span class="etiquette-fiabilite" title="{echapper(explication)}">'
            f"{echapper(libelle)}</span>")


def fiche(etiquette: str, valeur: str, precision: str = "",
          definition: str = "") -> str:
    """Un chiffre, ce qu'il mesure, et au besoin la phrase qui le situe."""
    suite = f'<div class="precision">{precision}</div>' if precision else ""
    nom = mot(etiquette, definition) if definition else echapper(etiquette)
    return (f'<div class="fiche"><div class="valeur">{valeur}</div>'
            f'<div class="etiquette">{nom}</div>{suite}</div>')


def fiches(cles: list[str], reperes: bool = False) -> str:
    """Une rangée de chiffres du module ``donnees``, avec leur précision.

    Les chiffres ne sont jamais écrits dans les pages : elles les appellent par
    leur clé, et la table est seule à les porter.
    """
    classe = "fiches reperes" if reperes else "fiches"
    corps = "".join(
        fiche(
            donnees.chiffre(cle).libelle,
            donnees.chiffre(cle).valeur,
            f'<a href="donnees.html#{cle}">{echapper(donnees.chiffre(cle).annee)} · '
            f"{echapper(donnees.chiffre(cle).source.split(',')[0])}</a>",
        )
        for cle in cles
    )
    return f'<div class="{classe}">{corps}</div>'


def points(entrees: list[tuple[str, str]]) -> str:
    """Quelques idées, une par bloc, titre puis phrase.

    C'est la forme que prend une proposition quand elle doit se lire en dix
    secondes : des blocs de même poids, côte à côte. Une liste à puces dirait
    la même chose, mais elle se lit de haut en bas et donne au premier point
    une importance que les autres n'ont pas.
    """
    corps = "".join(
        f'<div class="point"><h3>{echapper(titre)}</h3><p>{texte}</p></div>'
        for titre, texte in entrees
    )
    return f'<div class="points">{corps}</div>'


def note(texte: str, genre: str = "") -> str:
    """Une réserve, un avertissement, un résumé — selon ``genre``.

    Le texte est TOUJOURS enveloppé dans un bloc à lui : l'avertissement est
    une rangée souple — le pictogramme, puis le texte — et un texte de
    plusieurs paragraphes s'y rangerait sinon en colonnes, un paragraphe par
    colonne. Le ``<p>`` n'est ajouté que si le texte n'ouvre pas déjà un bloc.
    """
    classe = f"note {genre}" if genre else "note"
    prefixe = icone("triangle-alert", "Attention") if genre == "avertissement" else ""
    corps = texte if texte.lstrip().startswith("<p") else f"<p>{texte}</p>"
    return f'<div class="{classe}">{prefixe}<div>{corps}</div></div>'


def sommaire(texte: str) -> str:
    return f'<summary>{icone("chevron-down")}<span>{texte}</span></summary>'


def depliant(titre: str, corps: str, identifiant: str = "") -> str:
    """Une section repliée : son titre se lit, son contenu s'ouvre si on veut.

    Le temps du lecteur n'est pas gratuit. Tout ce qu'une page doit pouvoir
    justifier doit être là, sans quoi la page n'est pas honnête ; mais rien
    n'oblige à le lui faire traverser pour atteindre le résultat.
    """
    cible = f' id="{echapper(identifiant)}"' if identifiant else ""
    return (f'<details class="section"{cible}>{sommaire(echapper(titre))}'
            f'<div class="dedans">{corps}</div></details>')


def cle(question: str, reponse: str, corps: str = "", source: str = "",
        identifiant: str = "") -> str:
    """Une question, sa réponse en une phrase, et ce qui la montre.

    C'est l'unité de lecture des pages longues, et elle est faite pour deux
    lecteurs à la fois : celui qui n'a pas le temps lit la question et la
    réponse et s'arrête là ; celui qui veut voir descend d'un cran.
    """
    fin = f'<p class="source">{source}</p>' if source else ""
    cible = f' id="{echapper(identifiant)}" tabindex="-1"' if identifiant else ""
    return (f'<section class="cle"{cible}><h3>{echapper(question)}</h3>'
            f'<p class="reponse">{reponse}</p>{corps}{fin}</section>')


def tableau(entetes: list[str], lignes: list[list[str]],
            classes_colonnes: list[str] | None = None, titre: str = "",
            premiere_colonne_entete: bool = True) -> str:
    """Un tableau, dans un cadre qui défile plutôt que de déborder la page."""
    classes = classes_colonnes or [""] * len(entetes)

    def attribut(classe: str) -> str:
        # Les classes vont par paires — « long texte » réserve la largeur ET
        # aligne à gauche —, et un attribut sans guillemets se coupe au premier
        # espace. Il est donc toujours écrit entre guillemets.
        return f' class="{classe}"' if classe else ""

    tete = "".join(
        f'<th scope="col"{attribut(classe)}>{valeur}</th>'
        for valeur, classe in zip(entetes, classes)
    )
    corps = []
    for ligne in lignes:
        cellules = []
        for index, (valeur, classe) in enumerate(zip(ligne, classes)):
            if index == 0 and premiere_colonne_entete:
                cellules.append(f'<th scope="row"{attribut(classe)}>{valeur}</th>')
            else:
                cellules.append(f"<td{attribut(classe)}>{valeur}</td>")
        corps.append(f"<tr>{''.join(cellules)}</tr>")
    legende = f"<caption>{echapper(titre)}</caption>" if titre else ""
    return ('<div class="defilant"><table>' + legende
            + f"<thead><tr>{tete}</tr></thead><tbody>{''.join(corps)}</tbody>"
            + "</table></div>")


def plan(corps: str, etiquette: str = "Dans cette page") -> str:
    """Le sommaire d'une page longue, DÉDUIT de ses sections.

    Il est lu dans le HTML déjà rendu, où chaque section identifiée porte son
    titre : il ne peut donc pas dériver du contenu qu'il annonce.
    """
    import re

    motif = re.compile(
        r'<details class="section" id="([^"]+)"><summary>.*?<span>(.*?)</span></summary>'
        r'|<section class="cle" id="([^"]+)" tabindex="-1"><h3>(.*?)</h3>',
        re.S,
    )
    entrees = [(trouve[1] or trouve[3], trouve[2] or trouve[4])
               for trouve in motif.finditer(corps)]
    if not entrees:
        return ""
    liens = "".join(
        f'<li><a href="#{identifiant}" data-vers="{identifiant}">{titre}</a></li>'
        for identifiant, titre in entrees
    )
    return (f'<nav class="plan" aria-label="{echapper(etiquette)}">'
            f'<p class="etiquette">{echapper(etiquette)}</p><ol>{liens}</ol></nav>')


def appel(titre: str, texte: str, actions: list[tuple[str, str, bool]]) -> str:
    """Le panneau crème : ce qu'on demande au lecteur de faire ensuite.

    Crème et non vert : une affiche entièrement sombre se lit de loin, mais le
    geste qu'on demande doit se lire de près. ``actions`` donne le libellé,
    l'adresse, et si le lien est le geste principal.
    """
    liens = "".join(
        f'<a class="bouton" href="{cible}">{echapper(libelle)}</a>' if principal
        else f'<a href="{cible}">{echapper(libelle)}</a>'
        for libelle, cible, principal in actions
    )
    return f"""<div class="creme">
<p class="surtitre">Ce que vous pouvez faire</p>
<h2 class="serif" style="margin:0">{titre}</h2>
<p>{texte}</p>
<p class="actions">{liens}</p>
</div>"""


def gestes(etapes: list[str]) -> str:
    """Une marche à suivre, numérotée."""
    corps = "".join(
        f'<li><span class="rang">{index + 1}</span><span>{texte}</span></li>'
        for index, texte in enumerate(etapes)
    )
    return f'<ol class="gestes">{corps}</ol>'


def engagements(cartes: list[tuple[str, str, str]]) -> str:
    """Les engagements du programme, chiffrés et numérotés.

    Trois niveaux par carte : le CHIFFRE en or attire l'œil, la PROMESSE en
    serif porte le message, le DÉTAIL répond à qui veut savoir comment.
    """
    corps = "".join(
        f'<div class="engagement"><div class="rang">{index + 1:02d}</div>'
        f'<div class="chiffre">{chiffre}</div>'
        f'<div class="promesse">{promesse}</div>'
        f'<div class="detail">{detail}</div></div>'
        for index, (chiffre, promesse, detail) in enumerate(cartes)
    )
    return ('<section class="engagements" aria-label="Nos engagements">'
            f'<div class="grille">{corps}</div></section>')
