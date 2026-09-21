"""Le texte des sept pages, et lui seul.

Chaque fonction de ce module rend le CORPS d'une page : ce qui se trouve entre
le bandeau de tête et le pied, sans jamais écrire une balise de structure ni un
chiffre. Les balises viennent de ``gabarit``, les chiffres de ``donnees`` —
appelés par leur clé, de sorte qu'un chiffre corrigé le soit partout d'un coup,
et que la page « Données et sources » ne puisse pas être en retard sur le
texte.

Ce que ces pages cherchent à faire tient en une phrase : montrer ce que la
politique française des transports coûte et à qui, puis proposer une
alternative libérale — mesure par mesure, avec ses chiffres, ses objections et
ses limites.
"""

from __future__ import annotations

from . import donnees
from . import gabarit as g

v = donnees.valeur


# -- accueil : le programme --------------------------------------------------


def programme() -> str:
    tete = g.affiche(
        "Notre programme pour les transports",
        "Votre billet de TER en paie " + g.cle_texte(v("recettes_usagers_ter"))
        + ". Qui paie le reste, et pourquoi ne le voyez-vous jamais ?",
        "Un trajet en train régional coûte environ quatre fois le prix du "
        "billet. La différence est versée par la région, par l'État et par "
        "les employeurs, sans qu'aucun de ces montants ne paraisse jamais "
        "devant vous. "
        + g.cle_texte("Le problème n'est pas que les transports soient aidés.")
        + " C'est que personne ne sait de combien, ni pour quelle ligne, ni à "
        "la place de quoi.",
    )

    reperes = g.fiches(["concours_ferroviaire", "recettes_usagers_ter",
                        "ticpe", "age_voies"], reperes=True)

    cartes = g.engagements([
        (
            "Chaque contrat",
            "mis en concurrence, " + g.cle_texte("dans les cinq ans") + ".",
            "Tous les services achetés par une collectivité — TER, "
            "Transilien, bus et tramways urbains — sont attribués par appel "
            "d'offres, avec un cahier des charges public. L'autorité continue "
            "de décider des lignes, des horaires et des tarifs : elle change "
            "seulement de fournisseur quand un autre fait mieux. "
            f"{v('ter_ouverts')} de l'offre conventionnée a été attribuée "
            "ainsi — onze lots, quand une soixantaine doivent l'être avant la "
            "fin 2033.",
        ),
        (
            "Votre argent",
            "écrit " + g.cle_texte("ligne par ligne") + ", avant le vote.",
            "Chaque ligne publie ce qu'elle coûte, ce qu'elle rapporte, "
            "combien de voyageurs elle transporte et quelle subvention "
            "chacun reçoit. Aucun grand projet n'est lancé sans une "
            "contre-expertise indépendante publiée, et sans que le mode de "
            "financement soit voté en même temps que le projet — ce qui n'a "
            f"été fait ni pour le Grand Paris Express, ni pour {v('lyon_turin')} "
            "de liaison Lyon-Turin.",
        ),
        (
            "L'usage",
            "payé " + g.cle_texte("au kilomètre") + ", pas à la pompe.",
            "La " + g.terme("TICPE") + " prélève la même somme au litre, que "
            "l'on roule à trois heures du matin en Lozère ou à huit heures "
            "dans un centre-ville saturé. Nous lui substituons, à prélèvement "
            "constant, une redevance d'usage modulable par zone et par heure, "
            "dont le produit est affecté aux infrastructures à hauteur de ce "
            "qu'elles coûtent réellement. Ni impôt supplémentaire, ni fichier "
            "de déplacements — et une entrée progressive pour les véhicules "
            "électriques, qui ne paient presque rien aujourd'hui.",
        ),
        (
            "Les émissions",
            "tarifées, " + g.cle_texte("pas la vignette") + " du véhicule.",
            "Les " + g.terme("ZFE") + " interdisent des véhicules selon leur "
            "âge, sans regarder l'usage qu'on en fait. Nous leur substituons "
            "la tarification des nuisances là où elles se produisent, et nous "
            "remplaçons le calendrier d'interdiction des motorisations par un "
            "objectif d'émissions. La substitution est la condition, et non "
            f"une précaution de style : la France paie {v('astreinte_air')} "
            "d'astreinte pour ses dépassements de pollution de l'air, et "
            "supprimer l'instrument sans le remplacer nous ferait payer "
            "davantage.",
        ),
    ])

    etapes = g.gestes([
        "<strong>Vous voyez enfin le prix de votre trajet.</strong> Chaque "
        "billet, chaque abonnement porte la mention de ce qu'il coûte "
        "réellement et de qui paie la différence. Le montant ne change pas ; "
        "il devient une information.",
        "<strong>Votre région achète son service au meilleur offrant.</strong> "
        "Le cahier des charges — fréquences, horaires, tarifs, qualité — "
        "reste le sien. Ce qui change, c'est qu'un opérateur qui fait moins "
        "bien pour plus cher peut perdre le contrat.",
        "<strong>Vous payez la route à l'usage, pas à l'achat.</strong> La "
        "taxe au litre laisse la place à une redevance au kilomètre, modulée "
        "selon le lieu et l'heure, à recettes constantes pour l'État. Rouler "
        "peu coûte moins ; rouler dans un embouteillage coûte ce que cet "
        "embouteillage coûte aux autres.",
    ])

    comparatif = g.tableau(
        ["", "Aujourd'hui", "Avec la réforme"],
        [
            ["Qui fait rouler votre train régional",
             "L'opérateur historique, par convention reconduite",
             "Celui qui a remporté l'appel d'offres"],
            ["Ce que vous savez du coût",
             "Le prix du billet, et rien d'autre",
             "Le coût complet, la subvention, la fréquentation"],
            ["Ce que vous payez pour la route",
             "Une taxe au litre, partout la même",
             "Une redevance à l'usage, selon le lieu et l'heure"],
            ["Si votre ligne est mal exploitée",
             "Rien à faire avant la fin de la convention",
             "L'autorité remet le lot en jeu"],
            ["Si vous avez une vieille voiture",
             "Interdiction d'entrée dans les zones à faibles émissions",
             "Vous payez ce que vous émettez, là où cela compte"],
            ["Qui décide d'un grand projet",
             "L'État, l'évaluation venant après la décision",
             "Un vote, après contre-expertise publiée et financement arrêté"],
        ],
        ["", "", ""],
        "Ce que la réforme change, ligne à ligne",
    )

    changements = g.points([
        ("Le prix redevient une information",
         "Un usager qui ignore ce que son trajet coûte ne peut arbitrer "
         "entre rien. Un élu qui ignore ce que sa ligne coûte par voyageur "
         "ne peut choisir qu'au prestige. Publier ces deux chiffres ne coûte "
         "rien et change les deux décisions."),
        ("L'opérateur cesse d'être irremplaçable",
         "Un contrat reconduit sans mise en concurrence n'a aucun prix de "
         "référence : ni l'autorité ni l'opérateur ne savent si le service "
         "est cher. Les premiers lots français remis en appel d'offres ont "
         f"vu leurs coûts de production reculer de {v('baisse_couts_ter')} — "
         "chiffre relevé par un rapport sénatorial qui conclut, par ailleurs, "
         "à un bilan financier incertain. Nous citons les deux."),
        ("La solidarité territoriale devient explicite",
         "Faire rouler un train peu fréquenté dans une vallée est un choix "
         "politique légitime. Il doit s'écrire comme tel — une "
         + g.terme("obligation de service public") + " définie, chiffrée et "
         "payée — au lieu d'être noyé dans le déficit d'un opérateur."),
        ("La facture cesse d'être envoyée aux suivants",
         f"L'État a repris {v('dette_reprise')} de dette ferroviaire sans "
         "rien changer à ce qui l'avait produite. Le Grand Paris Express est "
         "financé par un emprunt remboursable jusque dans les années 2070 : "
         "une génération circule, la suivante paie."),
    ])

    appel = g.appel(
        "Vérifiez plutôt que de nous croire.",
        "Tous les chiffres de ce site sont datés, sourcés et notés selon leur "
        "fiabilité. Le simulateur calcule dans votre navigateur ce que vos "
        "déplacements vous coûtent réellement, taxes et subventions "
        "comprises — rien n'est envoyé nulle part.",
        [("Ce que vous payez vraiment", "simulateur.html", True),
         ("Ce qui ne va pas aujourd'hui", "diagnostic.html", False),
         ("D'où viennent nos chiffres", "donnees.html", False)],
    )

    pas_propose = g.depliant(
        "Ce que nous ne proposons pas",
        """
<p>Une proposition libérale sur les transports est immédiatement traduite par
ses adversaires en « privatisation du rail » et en « fin des trains de
campagne ». Disons donc en toutes lettres ce que ce programme ne contient
pas.</p>
<ul class="serree">
  <li><strong>Pas de vente du réseau.</strong> Les voies, les gares et les
  routes restent des biens publics. Ce qui est mis en concurrence, c'est
  l'exploitation du service, pas la propriété de l'infrastructure.</li>
  <li><strong>Pas de fermeture de lignes décidée par un opérateur.</strong>
  Le service est défini par l'autorité organisatrice élue. Un exploitant peut
  perdre un contrat ; il ne peut pas supprimer un train que la collectivité a
  décidé d'acheter.</li>
  <li><strong>Pas de hausse du prélèvement total.</strong> La redevance
  d'usage remplace la taxe sur les carburants à recettes constantes pour
  l'État. Elle ne l'est pas pour chaque conducteur, et nous ne le cachons
  pas : à prélèvement global inchangé, rouler peu coûtera moins et rouler
  beaucoup coûtera plus. Le cas le plus net est celui du véhicule électrique,
  qui n'acquitte presque rien aujourd'hui : notre simulateur affiche l'écart
  sans l'adoucir, et la mesure 3 prévoit une entrée progressive.</li>
  <li><strong>Pas d'abandon de la desserte rurale.</strong> Elle est
  maintenue, mais payée explicitement, par une ligne budgétaire votée plutôt
  que par le déficit d'une entreprise publique.</li>
</ul>
<p class="discret">Ce qui reste, après ces quatre exclusions, est ce que
pratiquent l'Allemagne pour ses trains régionaux, la Suisse pour le
financement de son réseau et l'Italie pour sa grande vitesse — trois pays dont
personne ne dit qu'ils ont sacrifié leurs chemins de fer.</p>""",
        "non-propose",
    )

    garanties = g.depliant(
        "Les garanties, écrites dans la loi",
        """
<p>Une réforme des transports ne vaut que par ce qu'elle interdit à ceux qui
l'appliqueront. Six règles, dans la loi et non dans un décret :</p>
<ol class="gestes">
  <li><span class="rang">1</span><span><strong>Publication obligatoire.</strong>
  Coût complet, recettes, fréquentation et subvention par voyageur de chaque
  ligne, publiés chaque année dans un format réutilisable.</span></li>
  <li><span class="rang">2</span><span><strong>Mise en concurrence de
  droit.</strong> Aucun contrat d'exploitation ne peut être reconduit sans
  appel d'offres, sauf décision motivée de l'autorité organisatrice, rendue
  publique.</span></li>
  <li><span class="rang">3</span><span><strong>Contre-expertise avant
  décision.</strong> Tout projet dépassant un seuil fait l'objet d'une
  évaluation indépendante publiée avant le vote, et non après.</span></li>
  <li><span class="rang">4</span><span><strong>Affectation bornée de la
  redevance d'usage.</strong> Son produit est affecté à l'entretien et au
  développement des infrastructures À HAUTEUR DE LEUR COÛT CONSTATÉ, établi
  chaque année par un rapport public ; le solde demeure recette générale.
  L'affectation totale ferait un trou dans le budget de l'État que nous ne
  saurions pas combler, et nous préférons une garantie tenable à une promesse
  large.</span></li>
  <li><span class="rang">5</span><span><strong>Protection des
  déplacements.</strong> La redevance d'usage se paie sans que soit constitué
  aucun fichier des trajets : comptage forfaitaire ou relevé de compteur, au
  choix de l'automobiliste.</span></li>
  <li><span class="rang">6</span><span><strong>Clause de sauvegarde sur l'air
  et sur l'arrêt.</strong> Si les valeurs limites de pollution ne sont pas
  tenues dans les délais, la restriction d'accès revient de plein droit ; si
  l'expérimentation de la redevance coûte plus qu'elle ne rapporte, elle
  s'arrête. Une réforme qui ne prévoit pas son propre échec n'est pas une
  réforme.</span></li>
</ol>
<p class="discret">Deux de ces règles sont plus fragiles que les autres, et il
vaut mieux l'écrire que se le faire dire : une affectation de recette se défait
par une loi de finances, et une interdiction de fichier par une loi ordinaire.
C'est le sort qu'a connu la TICPE, dont l'affectation aux routes a disparu sans
bruit. Nous proposons donc de les inscrire par une loi organique, qui ne se
modifie pas dans le cours d'un budget — et nous serions favorables, pour
l'interdiction du fichier, à une garantie de niveau constitutionnel.</p>""",
        "garanties",
    )

    transition = g.depliant(
        "Comment on y va, en cinq ans",
        """
<p>Aucun réseau de transport ne change du jour au lendemain, et personne ne
doit se retrouver sans train pendant la transition. Le calendrier est donc
lent, et chaque étape est réversible tant que la suivante n'a pas eu lieu.</p>
<ul class="serree">
  <li><strong>Année 1 — la transparence.</strong> Publication des coûts, des
  recettes et des subventions par ligne. Cette seule mesure ne coûte rien, ne
  ferme rien, et rend le reste discutable.</li>
  <li><strong>Années 1 à 3 — les appels d'offres.</strong> Les conventions qui
  arrivent à échéance sont remises en concurrence lot par lot, en commençant
  par les plus denses, où l'échec est le moins coûteux et les candidats les
  plus nombreux.</li>
  <li><strong>Année 3 — l'expérimentation de la redevance d'usage.</strong>
  Sur les poids lourds d'abord, comme la Suisse et l'Allemagne l'ont fait
  avant nous — et comme la France a échoué à le faire en 2013. La différence
  tient en un mot : l'écotaxe était une taxe DE PLUS, la redevance est une
  taxe À LA PLACE. Le texte qui la crée éteint la taxe au litre dans le même
  article, faute de quoi il ne doit pas être déposé. Puis les véhicules légers
  dans une région volontaire.</li>
  <li><strong>Années 4 et 5 — la bascule.</strong> La taxe au litre décroît à
  mesure que la redevance monte, à prélèvement constant et vérifié chaque
  année par un rapport public. Les véhicules électriques y entrent par
  paliers : ils n'acquittent presque rien aujourd'hui, et leur appliquer le
  tarif plein d'un coup punirait un achat fait sous un autre régime
  fiscal.</li>
  <li><strong>À tout moment — l'arrêt.</strong> Si l'expérimentation montre
  que le dispositif coûte plus qu'il ne rapporte, elle s'arrête. Une réforme
  qu'on ne peut pas arrêter n'est pas une réforme, c'est un pari.</li>
</ul>""",
        "transition",
    )

    return f"""
{tete}

{reperes}

<h2>Quatre engagements</h2>
{cartes}

<h2>Ce que ça change pour vous</h2>
{etapes}

{comparatif}

<h2>Pourquoi cela marche</h2>
{changements}

{appel}

<h2>Les questions qui viennent tout de suite</h2>
{pas_propose}
{garanties}
{transition}

{g.note(
    "Ce site ne chiffre pas la réforme à l'échelle du pays, et il explique "
    "pourquoi sur la page <a href='reforme.html#financement'>La réforme</a> : "
    "un tel chiffrage exigerait un modèle des coûts d'exploitation "
    "ferroviaires et routiers que ce dépôt ne contient pas. Une économie "
    "annoncée sans ce modèle serait inventée.",
    "avertissement")}
"""


# -- le système actuel -------------------------------------------------------


def diagnostic() -> str:
    tete = g.affiche(
        "Le système actuel",
        "Un réseau payé par " + g.cle_texte("trois guichets") + " que "
        "personne ne regarde en même temps.",
        "L'usager paie un billet, l'employeur un prélèvement sur les "
        "salaires, le contribuable une subvention, et l'automobiliste une "
        "taxe qui ne finance pas la route. Chacun de ces quatre flux est "
        "défendable. Mis bout à bout, ils forment un système dont personne — "
        "ni l'élu, ni l'opérateur, ni le voyageur — ne connaît le prix de "
        "revient.",
    )

    qui_paie = g.tableau(
        ["Qui paie", "Combien", "Ce qu'il voit"],
        [
            ["Le voyageur",
             f"environ {v('recettes_usagers_ter').lstrip('≈ ')} du coût d'un "
             "TER, un cinquième d'un réseau urbain de province",
             "Le prix du billet"],
            ["L'employeur",
             f"{v('versement_mobilite')} de " + g.terme("versement mobilité"),
             "Une ligne sur un bordereau de cotisations"],
            ["Le contribuable local",
             "la subvention d'équilibre votée par la région ou "
             "l'intercommunalité",
             "Une ligne dans un budget de plusieurs centaines de pages"],
            ["Le contribuable national",
             f"les concours de l'État, {v('concours_ferroviaire')} par an pour "
             "le seul ferroviaire",
             "Rien"],
            ["L'automobiliste",
             f"{v('ticpe')} de " + g.terme("TICPE") + ", plus la TVA qui "
             "s'applique par-dessus",
             "Un prix à la pompe, dont il ignore la composition"],
        ],
        ["", "long texte", "texte"],
        "Qui finance les transports, et ce que chacun en perçoit",
    )

    repartition = g.cle(
        "Comment le système fonctionne, en une page",
        "Une collectivité décide du service, achète ce service à un "
        "opérateur, et le finance avec un prélèvement sur les salaires, une "
        "subvention et des billets. Aucun de ces trois montants n'est "
        "rapproché des deux autres.",
        f"""
<p>La collectivité compétente — la région pour les trains régionaux,
l'intercommunalité pour les bus, Île-de-France Mobilités en région parisienne —
est l'{g.terme('AOM')}. Elle fixe les lignes, les horaires et les tarifs, puis
signe un contrat avec un exploitant. Jusqu'en 2019, ce contrat ne pouvait aller
qu'à l'opérateur historique pour le rail ; depuis, il peut être mis en
concurrence, et il l'est rarement : {v('ter_ouverts')} des services TER.</p>
<p>Le financement vient d'ailleurs. Le {g.terme('versement mobilité')} pèse sur
la masse salariale des employeurs et rapporte {v('versement_mobilite')} par an.
La subvention d'équilibre vient du budget de la collectivité. Les billets
apportent le reste — {v('recettes_usagers_urbain')} du coût d'un réseau urbain
de province, {v('recettes_usagers_ter')} de celui d'un TER.</p>
<p>Quant à la route, elle est financée de côté. Les {v('ticpe')} de taxe sur
les carburants ne partent pas tous au budget général — ce site l'a écrit
pendant un an avant d'aller le vérifier, et c'était faux : l'État en garde
environ la moitié, les collectivités en reçoivent une large part, et l'agence
de financement des infrastructures — l'AFIT France, {v('afit')} de budget
annuel — une fraction. Le défaut n'est donc pas que cet argent disparaisse,
c'est qu'aucune de ces parts ne soit liée à une route : ce sont des budgets,
pas des affectations. L'entretien des voiries, lui, relève des départements et
des communes, sur leurs propres ressources.</p>""",
        identifiant="fonctionnement",
    )

    defaut_prix = g.cle(
        "Premier défaut : le prix ne dit plus rien",
        f"Quand le billet couvre {v('recettes_usagers_ter')} du coût, son "
        "montant ne renseigne plus sur ce que le trajet mobilise. Il ne "
        "renseigne pas davantage l'élu qui le fixe.",
        """
<p>Un prix sert à deux choses : dire à celui qui achète ce que sa décision
coûte aux autres, et dire à celui qui produit où il vaut la peine de produire.
Un prix qui couvre le quart du coût ne fait ni l'un ni l'autre — et le reproche
ne vise pas la subvention, qui peut être parfaitement justifiée, mais le fait
qu'elle soit invisible.</p>
<p>La conséquence se lit dans les arbitrages : une région qui ignore ce que
coûte le voyageur transporté sur chacune de ses lignes ne peut pas savoir si
l'argent d'un aller-retour quotidien serait mieux employé en cars cadencés, en
train, ou en aide directe aux habitants concernés. Elle décide donc à
l'estime, et le plus souvent en faveur de ce qui se voit.</p>""",
        identifiant="prix",
    )

    defaut_monopole = g.cle(
        "Deuxième défaut : un contrat sans prix de référence",
        "Une convention reconduite sans mise en concurrence ne dit à personne "
        "si le service est cher : l'autorité n'a rien à quoi le comparer, et "
        "l'opérateur non plus.",
        f"""
<p>Ce n'est pas une accusation contre les exploitants publics : un monopole
n'est pas peuplé de paresseux, il est privé de l'information que produit la
comparaison. Il n'est plus nécessaire d'aller chercher la démonstration à
l'étranger. Les premiers lots TER français remis en appel d'offres ont vu leurs
coûts de production reculer de {v('baisse_couts_ter')} : l'étoile d'Amiens, les
Pays de la Loire, la Nouvelle-Aquitaine, et une offre augmentée de trois quarts
à deux fois en région Sud pour le même argent.</p>
<p>Le rapport sénatorial qui établit ces chiffres conclut pourtant à un
<strong>bilan incertain</strong> pour les finances publiques, et nous le citons
aussi : chaque lot impose des dépenses nouvelles aux régions —
{v('cout_transition_ter')} pour un atelier de maintenance neuf, des
indemnisations de candidats, des recrutements. Les gains d'exploitation sont
réels ; les coûts de transition le sont également, et ils tombent sur la
collectivité avant les gains.</p>
<p>Où en est-on ? {v('ter_ouverts')} de l'offre conventionnée a été attribuée
après appel d'offres. Onze lots, quand une soixantaine doivent l'être d'ici la
fin 2033 — et le calendrier se resserre au point que, sur certains, l'opérateur
historique risque d'être le seul candidat. Un appel d'offres à un candidat ne
produit aucun prix de référence.</p>
{g.note(
    "La concurrence dont il est question ici est celle POUR le marché : "
    "l'autorité met un lot en appel d'offres et choisit l'exploitant. "
    "L'usager, lui, ne change rien à ses habitudes — il ne choisit pas plus "
    "son train qu'il ne choisit aujourd'hui l'entreprise qui ramasse ses "
    "ordures.")}""",
        identifiant="monopole",
    )

    defaut_dette = g.cle(
        "Troisième défaut : la dette comme mode de financement",
        f"L'État a repris {v('dette_reprise')} de dette ferroviaire sans "
        "modifier le mécanisme qui l'avait engendrée, et la principale "
        "infrastructure en construction est financée par un emprunt "
        "remboursable sur cinquante ans.",
        f"""
<p>La dette de SNCF Réseau venait du financement des lignes à grande vitesse
par l'emprunt, à des niveaux de trafic qui ne les remboursaient pas. Sa reprise
par l'État, en deux temps, a soldé le passé. Elle n'a pas touché à la cause :
un gestionnaire d'infrastructure dont les péages ne couvrent pas les charges
emprunte la différence, et recommence.</p>
<p>Le même mécanisme est à l'œuvre aujourd'hui : {v('grand_paris_express')} de
travaux pour le Grand Paris Express, portés par une dette adossée à des taxes
affectées et remboursable jusque dans les années 2070. L'estimation initiale
était inférieure de moitié. Aucune des révisions n'a donné lieu à un nouveau
vote.</p>""",
        identifiant="dette",
    )

    defaut_projets = g.cle(
        "Quatrième défaut : on décide, puis on évalue",
        "L'" + g.terme("évaluation socio-économique") + " est obligatoire "
        "pour les grands projets. Elle intervient après l'annonce, et n'a "
        "presque jamais renversé une décision.",
        f"""
<p>Le cas le mieux documenté est la liaison Lyon-Turin : {v('lyon_turin')}
annoncés, accès compris, dont la Cour des comptes relevait que les prévisions
de trafic n'avaient jamais été réactualisées de façon contradictoire. Les voies
d'accès françaises ne sont à ce jour ni financées, ni décidées.</p>
<p>Le vice n'est pas propre à ce projet. Il tient à l'ordre des opérations :
l'annonce vient d'abord, le dossier ensuite, et une évaluation défavorable
arrive quand l'engagement politique est déjà pris. Une contre-expertise
indépendante publiée AVANT le vote ne garantit pas la bonne décision ; elle
garantit qu'on ne pourra pas dire qu'on ne savait pas.</p>""",
        identifiant="projets",
    )

    defaut_entretien = g.cle(
        "Cinquième défaut : l'entretien perd contre le ruban",
        f"Les voies du réseau ferré ont {v('age_voies')} de moyenne, et "
        f"{v('ponts_degrades')} sont en mauvais état structurel. Renouveler "
        "ne s'inaugure pas.",
        f"""
<p>Un réseau vieillit quand on y investit moins qu'il ne s'use. Les
ralentissements imposés pour cause de voie dégradée en sont la mesure la plus
directe : le train met plus longtemps qu'il y a trente ans sur une partie des
lignes régionales, et ce recul ne figure dans aucun indicateur de
ponctualité — celui-ci compare l'horaire réel à l'horaire annoncé, lequel a
été allongé.</p>
<p>Sur la route, l'inventaire est pire : le rapport sénatorial de 2019 estimait
{v('ponts_degrades')} en mauvais état sur un parc dont il notait qu'aucune
collectivité ne tenait la liste complète. Un pays qui ne sait pas combien de
ponts il possède ne peut pas savoir ce que leur entretien coûte.</p>
{g.note(
    f"{v('ponctualite_ter')} des TER sont comptés à l'heure, et ce chiffre "
    "rassure à tort : un train est « à l'heure » s'il arrive avec moins de "
    "cinq minutes de retard sur un horaire lui-même allongé, et les trains "
    "supprimés ne sont pas comptés du tout. C'est le moins sévère des "
    "indicateurs possibles.")}""",
        identifiant="entretien",
    )

    defaut_interdiction = g.cle(
        "Sixième défaut : interdire plutôt que faire payer",
        "Les zones à faibles émissions, le calendrier de fin des moteurs "
        "thermiques et les restrictions de vitesse rationnent l'usage par "
        "l'interdiction, au lieu d'en faire payer le coût réel.",
        f"""
<p>Une {g.terme('ZFE')} interdit la circulation aux véhicules trop anciens,
classés par vignette. Le critère est l'âge du véhicule, jamais l'usage : rouler
mille kilomètres par an dans une vieille voiture y est interdit, en faire trente
mille dans une neuve ne l'est pas. L'effet distributif est celui qu'on imagine —
ceux qui changent de voiture le plus rarement sont ceux qui en ont le moins les
moyens.</p>
<p>Le même raisonnement vaut pour la fiscalité des carburants : la
{g.terme('TICPE')} prélève la même somme au litre en zone rurale et en heure de
pointe urbaine, alors que les nuisances — congestion, bruit, qualité de l'air —
diffèrent du tout au tout. Une taxe aveugle au lieu et à l'heure ne peut pas
corriger un problème qui dépend du lieu et de l'heure.</p>
<p>Le débat de 2026 a montré l'impasse des deux camps. Le Parlement a voté la
suppression des zones à faibles émissions ; le Conseil constitutionnel l'a
censurée pour un motif de procédure — la mesure n'avait pas sa place dans le
texte qui la portait — et les zones sont restées. Supprimer l'instrument sans
lui substituer quoi que ce soit n'aurait de toute façon pas réglé le problème
qui l'a fait naître : la France est sous astreinte,
{v('astreinte_air')} au plus fort, pour des valeurs limites de pollution de
l'air qu'elle devait respecter depuis 2010 et qu'elle dépasse toujours à Paris
et à Lyon. Le choix n'est pas entre interdire et ne rien faire ; il est entre
interdire et faire payer.</p>""",
        identifiant="interdiction",
    )

    defaut_fret = g.cle(
        "Et le fret, que personne ne regarde",
        "La " + g.terme("part modale") + " du rail dans le transport de "
        f"marchandises est tombée à {v('fret_ferroviaire')}, contre {v('fret_ue')} en moyenne "
        "européenne.",
        f"""
<p>Le fret ferroviaire a perdu la moitié de sa part modale en vingt-cinq ans,
pendant qu'elle progressait en Allemagne et en Autriche. Les causes sont
connues et cumulatives : des sillons attribués en priorité aux voyageurs, des
travaux nocturnes qui coupent les itinéraires longs, des
{g.terme('péages ferroviaires', 'péage ferroviaire')} parmi les plus élevés
d'Europe, et la disparition progressive des embranchements particuliers qui
reliaient les usines au réseau.</p>
<p>Le fret n'a aucun électorat : il ne fait pas d'inauguration et n'apparaît
dans aucune promesse de campagne. C'est pourtant le segment où le report modal
serait le plus utile, et celui où la concurrence est déjà ouverte depuis
2006 — sans que cela suffise. La concurrence ne crée pas de sillons : elle
répartit ceux qu'on veut bien lui laisser, et c'est l'objet de la mesure 7.</p>""",
        identifiant="fret",
    )

    defaut_autoroutes = g.cle(
        "Et les autoroutes, dont la décision approche sans être prise",
        "Les sept concessions historiques s'achèvent entre 2031 et 2036. Ce "
        "qu'on fera du réseau à cette date est la décision de transport la "
        "plus lourde de la décennie, et aucune majorité ne s'est prononcée.",
        f"""
<p>Les concessions rapportent aujourd'hui {v('peages_ca')} de péages par an à
leurs titulaires. À leur terme, les ouvrages reviennent gratuitement à l'État,
qui devra choisir : remettre le réseau en concession, l'exploiter en régie, ou
basculer vers un péage d'usage généralisé. Chacune de ces voies engage des
décennies et des dizaines de milliards.</p>
<p>Le régulateur alerte sur un point que le débat ignore :
{v('concessions_investissements')} d'investissements restent dus par les
concessionnaires avant la fin des contrats, et les obligations de fin de
contrat — l'état dans lequel le réseau doit être rendu — sont mal définies. Un
concessionnaire dont le contrat s'achève n'a aucune raison d'entretenir
au-delà du strict nécessaire, et c'est le moment où la vigilance devrait être
maximale.</p>
<p>Ce site a longtemps signalé cette échéance comme « la décision la plus
lourde de la décennie » sans prendre parti. C'était une facilité : signaler
n'est pas décider. La mesure 8 tranche.</p>""",
        identifiant="autoroutes",
    )

    a_garder = g.depliant(
        "Ce qu'il ne faut surtout pas casser",
        f"""
<p>Un diagnostic qui ne trouverait que des défauts serait un tract. Le système
français a des qualités réelles, et plusieurs sont rares :</p>
<ul class="serree">
  <li><strong>Le maillage.</strong> {v('reseau_ferre')} de lignes exploitées
  font le deuxième réseau d'Europe. Aucun pays ne le reconstruirait
  aujourd'hui, et le démailler est irréversible.</li>
  <li><strong>La grande vitesse.</strong> Le TGV a mis les grandes villes à
  quelques heures les unes des autres et pris à l'avion l'essentiel du trafic
  intérieur sur les axes qu'il dessert. C'est une réussite industrielle et
  d'aménagement.</li>
  <li><strong>La sécurité.</strong> Le ferroviaire français est l'un des plus
  sûrs d'Europe. Toute réforme qui toucherait à l'unicité des règles de
  sécurité ou à l'indépendance de leur contrôle serait une mauvaise
  réforme.</li>
  <li><strong>La tarification sociale.</strong> Les réductions pour les jeunes,
  les familles et les bas revenus sont un choix légitime. Nous proposons de les
  rendre explicites et financées, pas de les supprimer.</li>
</ul>
<p class="discret">Ce sont ces quatre acquis que la dégradation de
l'infrastructure menace le plus sûrement : un réseau qu'on n'entretient pas se
ferme tout seul, ligne par ligne, sans que personne n'ait à le décider.</p>""",
        "a-garder",
    )

    corps_sections = "\n".join([repartition, defaut_prix, defaut_monopole,
                                defaut_dette, defaut_projets, defaut_entretien,
                                defaut_interdiction, defaut_fret,
                                defaut_autoroutes, a_garder])

    return f"""
{tete}

{g.fiches(["reseau_ferre", "petites_lignes", "part_voiture_travail",
           "emissions_transports"])}

{g.plan(corps_sections)}

<h2>Qui paie, et ce que chacun voit</h2>
{qui_paie}

<h2>Comment ça marche, et ce qui ne marche pas</h2>
{corps_sections}

{g.appel(
    "Six défauts, deux sujets oubliés, huit mesures.",
    "Chacun de ces défauts appelle une mesure précise, avec son mécanisme, "
    "son effet attendu et l'objection la plus sérieuse qu'on lui oppose. Le "
    "fret et les autoroutes en ont une aussi : diagnostiquer sans proposer "
    "est exactement ce que nous reprochons aux autres.",
    [("La réforme, mesure par mesure", "reforme.html", True),
     ("Ce que font les autres pays", "comparaisons.html", False)],
)}
"""


# -- comparaisons internationales --------------------------------------------


def comparaisons() -> str:
    tete = g.affiche(
        "Ailleurs",
        "Six pays, dont " + g.cle_texte("le nôtre, qui a échoué") + ".",
        "La Suisse finance son réseau par des recettes affectées et votées ; "
        "l'Allemagne achète ses trains régionaux par appel d'offres ; "
        "l'Italie laisse deux opérateurs se concurrencer sur la grande "
        "vitesse ; le Japon a privatisé ses chemins de fer. Le Royaume-Uni a "
        "essayé autre chose et fait machine arrière. La France, elle, a tenté "
        "notre troisième mesure en 2013 et l'a abandonnée pour un milliard "
        "d'euros — c'est la ligne la plus utile du tableau.",
    )

    entetes = ["Pays", "Investissement dans le réseau",
               "Ce que paie l'usager", "Le mécanisme"]
    # La France y figure au titre de l'échec, et sa ligne ne se lit pas comme
    # les autres : les deux colonnes chiffrées n'ont pas de sens pour un
    # dispositif qui n'a jamais fonctionné, et elles le disent.
    lignes = [[f'<span id="pays-{pays.nom.lower().replace(" ", "-")}">'
               f"{pays.drapeau} {pays.nom}</span>",
               pays.investissement, pays.usager, pays.modele]
              for pays in donnees.PAYS]
    table = g.tableau(entetes, lignes, ["", "texte", "texte", "long texte"],
                      "Cinq systèmes de transport, et ce qui les distingue")

    fiches_pays = "".join(
        g.depliant(
            f"{pays.drapeau} {pays.nom} — {pays.modele}",
            "<ul class=\"serree\">"
            + "".join(f"<li>{ligne}</li>" for ligne in pays.detail)
            + "</ul>"
            + f'<p class="reponse"><strong>Ce qu\'on en retient.</strong> '
            f"{pays.lecon}</p>"
            + g.note(f"<p><strong>La réserve.</strong> {pays.reserve}</p>"
                     f'<p class="discret">{pays.source} · {pays.annee} · '
                     f"{g.etiquette_fiabilite(pays.fiabilite)}</p>",
                     "avertissement"),
            f"detail-{pays.nom.lower().replace(' ', '-')}",
        )
        for pays in donnees.PAYS
    )

    deux_concurrences = g.cle(
        "Deux concurrences, qu'il ne faut pas confondre",
        "La concurrence POUR le marché met un contrat en appel d'offres ; la "
        "concurrence SUR le marché laisse plusieurs opérateurs rouler côte à "
        "côte. Elles ne s'appliquent pas aux mêmes lignes.",
        f"""
<ul class="serree">
  <li><strong>Pour le marché</strong> — la {g.terme('délégation de service public')} : l'autorité définit le service,
  met le lot en appel d'offres, choisit l'exploitant pour quelques années.
  C'est le modèle allemand pour les trains régionaux, et le modèle français
  ordinaire pour les bus urbains. Il convient là où le service ne serait pas
  rentable seul, c'est-à-dire presque partout.</li>
  <li><strong>Sur le marché</strong> — l'{g.terme('open access')} : chacun
  fait rouler ses trains à ses tarifs et à ses risques. C'est le modèle
  italien sur la grande vitesse, et ce qui se passe déjà en France entre Paris
  et Lyon. Il ne fonctionne que là où la demande est assez dense pour faire
  vivre deux offres.</li>
</ul>
<p>Confondre les deux est la source de la plupart des malentendus du débat
français : on oppose l'exemple britannique — une architecture de franchises mal
conçue — à une proposition qui, pour les trains régionaux, décrit l'Allemagne.</p>""",
        identifiant="deux-concurrences",
    )

    ce_que_ca_ne_prouve_pas = g.cle(
        "Ce que ces comparaisons ne prouvent pas",
        "Qu'un mécanisme marche ailleurs n'établit pas qu'il marchera ici. "
        "Elles servent à écarter les impossibilités, pas à fonder une "
        "promesse.",
        """
<ul class="serree">
  <li><strong>Les périmètres diffèrent.</strong> « Ce que paie l'usager » ne
  recouvre pas les mêmes charges d'un pays à l'autre : selon qu'on y compte ou
  non l'infrastructure, le même réseau affiche un taux de couverture du simple
  au double.</li>
  <li><strong>Les géographies diffèrent.</strong> La densité japonaise, la
  taille suisse et la structure polycentrique allemande ne sont pas des
  variables d'ajustement : elles expliquent une partie de ce qu'on attribue
  aux institutions.</li>
  <li><strong>Les échecs comptent autant que les réussites.</strong> Le
  Royaume-Uni est dans ce tableau pour cette raison. Une comparaison qui ne
  retiendrait que les succès ne convaincrait que ceux qui le sont déjà.</li>
  <li><strong>Aucun de ces pays n'a supprimé la subvention.</strong> Tous
  paient leur réseau avec de l'argent public. Ce qui change, c'est la manière
  dont cet argent est décidé, affecté et contrôlé.</li>
</ul>""",
        identifiant="limites-comparaison",
    )

    corps_sections = "\n".join([deux_concurrences, ce_que_ca_ne_prouve_pas])

    return f"""
{tete}

{table}

{g.note(
    "Les deux chiffres de chaque ligne sont de SECONDE MAIN et portent leur "
    "réserve dans la fiche du pays. Les comparaisons internationales de "
    "transport sont les plus faciles à retourner contre celui qui les "
    "publie : deux chiffres exacts, pris dans deux éditions différentes, font "
    "un tableau faux.",
    "avertissement")}

<h2>Pays par pays</h2>
{fiches_pays}

<h2>Ce qu'il faut en tirer, et ce qu'il ne faut pas</h2>
{corps_sections}

{g.appel(
    "Ce que nous en retenons, écrit en huit mesures.",
    "Le financement affecté suisse, les appels d'offres allemands et "
    "l'ouverture italienne se retrouvent dans trois de nos huit mesures. Les "
    "deux échecs — le britannique et le nôtre — se retrouvent dans ce que "
    "nous ne proposons pas, et dans la façon dont nous proposons le reste.",
    [("La réforme, mesure par mesure", "reforme.html", True),
     ("Ce que nous ne proposons pas", "index.html#non-propose", False)],
)}
"""


# -- la réforme --------------------------------------------------------------


def reforme() -> str:
    tete = g.affiche(
        "La réforme",
        "Huit mesures, " + g.cle_texte("et ce qu'on peut leur opposer") + ".",
        "Chacune est décrite par son mécanisme — ce qu'elle change dans les "
        "textes —, par son effet attendu, et par l'objection la plus sérieuse "
        "qu'on lui oppose. Quand nous ne savons pas chiffrer, nous l'écrivons "
        "plutôt que d'inventer un montant.",
    )

    mesure_1 = g.cle(
        "1. Tout contrat d'exploitation passe par un appel d'offres",
        "Les services achetés par une collectivité — TER, Transilien, bus, "
        "tramways — sont attribués par mise en concurrence, et reconduits "
        "sans appel d'offres seulement sur décision motivée et publiée.",
        f"""
<p><strong>Le mécanisme.</strong> La loi inverse la charge : aujourd'hui,
l'autorité peut mettre en concurrence ; demain, elle doit, ou bien elle
explique publiquement pourquoi elle ne le fait pas. Le cahier des charges — les
lignes, les horaires, les tarifs, la qualité attendue — reste écrit par
l'autorité élue.</p>
<p><strong>L'effet attendu.</strong> Un prix de référence, là où il n'en existe
aucun. Il n'est plus besoin de l'emprunter à l'Allemagne : les premiers lots
français remis en concurrence ont vu leurs coûts de production au
{g.terme('train-kilomètre')} reculer de {v('baisse_couts_ter')}, et l'offre
augmenter de trois quarts à deux fois à coût constant en région Sud.
L'opérateur historique a remporté une large part de ces lots, ce qui est le
signe que le mécanisme fonctionne — pas qu'il échoue.</p>
<p><strong>L'objection la plus sérieuse.</strong> Elle est désormais chiffrée,
et par le Sénat. Chaque lot impose à la région des dépenses nouvelles :
{v('cout_transition_ter')} pour un atelier de maintenance neuf — environ
200 M€ anticipés en région Sud, 193 M€ en Nouvelle-Aquitaine —,
l'indemnisation des candidats malheureux, et un quart d'effectifs en plus dans
les services TER. Le même rapport relève que le calendrier est intenable :
une soixantaine de lots à attribuer d'ici 2033, au point que sur certains
l'opérateur historique serait le seul candidat. Un appel d'offres sans
candidat ne produit aucun prix de référence, et coûte tout de même ses frais
de procédure.</p>
<p><strong>Ce que nous en tirons.</strong> Commencer par les réseaux denses,
où les candidats sont nombreux ; étaler le calendrier plutôt que de tenir une
échéance au prix de lots déserts ; et mutualiser entre régions ce qui peut
l'être — ateliers, matériel, ingénierie d'appel d'offres. Une région seule
paie un atelier ; trois régions voisines en paient un tiers chacune.</p>""",
        identifiant="concurrence",
    )

    mesure_2 = g.cle(
        "2. Chaque ligne publie ce qu'elle coûte",
        "Coût complet, recettes, fréquentation et subvention par voyageur, "
        "publiés chaque année, ligne par ligne, dans un format "
        "réutilisable.",
        f"""
<p><strong>Le mécanisme.</strong> Une obligation de publication inscrite dans
la loi, assortie d'un format normalisé et d'un contrôle de l'{g.terme('ART')}.
Les données existent déjà : elles servent à négocier les contrats. Ce qui
manque, c'est leur publicité.</p>
<p><strong>L'effet attendu.</strong> Le débat devient possible. Aujourd'hui,
personne ne peut dire si la ligne qu'on ferme coûtait plus cher par voyageur
que celle qu'on garde, ni si un car cadencé rendrait le même service pour le
cinquième du prix. Demain, chacun pourra le vérifier — y compris pour nous
contredire.</p>
<p><strong>L'objection la plus sérieuse.</strong> Publier une subvention par
voyageur, c'est armer ceux qui voudront fermer les lignes rurales. La réponse
est que cette information circule déjà, mais en circuit fermé : ce sont les
habitants qui ne l'ont pas. Une ligne qu'on ne défend qu'à condition de cacher
son coût est une ligne mal défendue.</p>""",
        identifiant="transparence",
    )

    mesure_3 = g.cle(
        "3. Payer l'usage de la route, pas sa possession",
        "À prélèvement constant, une redevance kilométrique modulable par "
        "zone et par heure remplace progressivement la taxe sur les "
        "carburants. Son produit est affecté aux infrastructures à hauteur de "
        "ce qu'elles coûtent, et le solde demeure recette générale.",
        f"""
<p><strong>Le mécanisme.</strong> La {g.terme('TICPE')} décroît à mesure que
la redevance monte, dans le même texte et au même rythme. Le taux de la
redevance est voté chaque année, et son produit affecté à l'entretien et au
développement du réseau <strong>à hauteur du coût constaté de celui-ci</strong>,
établi par un rapport public ; le solde demeure recette générale. Les poids
lourds d'abord, puis les véhicules légers dans une région volontaire.</p>
<p><strong>Pourquoi une affectation bornée, et non totale.</strong> Parce que
l'affectation totale est une promesse que nous ne saurions pas tenir. Les
{v('ticpe')} de taxe sur les carburants ne financent pas les routes, mais ils
financent quelque chose : l'État en garde environ la moitié, et les
collectivités une large part. Affecter l'intégralité du produit aux
infrastructures ouvrirait dans le budget général un trou de plusieurs
milliards dont ce volet ne dit pas comment il serait comblé — et un volet
transports qui déséquilibre le budget de l'État n'est pas un programme
sérieux. Nous affectons donc ce que les infrastructures coûtent, ce qui est
déjà une rupture : aujourd'hui, ce montant n'est même pas calculé.</p>
<p><strong>Le précédent français, qui est un échec.</strong> La France a déjà
tenté cette mesure. L'écotaxe poids lourds a été votée, construite, puis
abandonnée en 2013 devant la fronde des « bonnets rouges » : le contribuable a
versé {v('ecotaxe_cout')} pour une taxe qui n'a jamais rien perçu. Nous en
retenons une règle, et elle est contraignante : l'écotaxe était une taxe DE
PLUS, la redevance est une taxe À LA PLACE. Si le texte qui crée la redevance
n'éteint pas la taxe au litre dans le même article, il ne doit pas être
déposé.</p>
<p><strong>Les véhicules électriques, qui sont le cas le plus dur.</strong> Un
véhicule électrique acquitte aujourd'hui l'accise sur l'électricité,
{v('accise_electricite')} : rapporté au kilomètre, plus de six fois moins
qu'un véhicule thermique, pour une chaussée qui s'use pareillement. Une
redevance d'usage corrige exactement cela, et c'est pourquoi elle leur coûte
beaucoup plus. Nous l'écrivons ici, notre simulateur l'affiche, et nous
prévoyons une entrée par paliers sur la durée d'un mandat : on ne change pas
rétroactivement le calcul d'un achat déjà fait.</p>
<p><strong>L'effet attendu.</strong> Un prix qui dit enfin quelque chose :
rouler en heure creuse sur une route vide coûte moins que rouler en heure de
pointe dans une agglomération saturée. C'est la seule manière connue de
réduire la congestion sans l'interdire, et elle remplace un prélèvement
aveugle qui pèse aujourd'hui le plus sur ceux qui n'ont pas d'alternative.</p>
<p><strong>L'objection la plus sérieuse.</strong> La vie privée. Une redevance
au kilomètre peut se transformer en registre des déplacements, et aucune
promesse politique ne protège contre cela. Nous proposons deux modalités sans
géolocalisation — forfait kilométrique déclaré, ou relevé de compteur au
contrôle technique — et l'interdiction, dans la loi, de constituer un fichier
des trajets. Nous ne prétendons pas que la question soit close.</p>""",
        identifiant="usage",
    )

    mesure_4 = g.cle(
        "4. Tarifer les nuisances au lieu d'interdire les véhicules",
        "Les zones à faibles émissions laissent la place à une tarification "
        "des émissions réellement produites, là où elles nuisent, et le "
        "calendrier d'interdiction des motorisations à un objectif "
        "d'émissions.",
        f"""
<p><strong>Le mécanisme.</strong> La vignette disparaît comme critère d'accès.
Ce qui la remplace est un prix : plus élevé pour un véhicule qui émet beaucoup,
dans une zone et à une heure où cela compte, nul là où cela ne compte pas. La
même logique s'applique aux constructeurs : un objectif d'émissions, et non
l'interdiction d'une technologie nommée.</p>
<p><strong>L'ordre des opérations, qui est tout.</strong> En 2026, le Parlement
a voté la suppression des zones à faibles émissions et le Conseil
constitutionnel l'a censurée pour un motif de forme — la mesure n'avait pas sa
place dans le texte qui la portait. Nous ne proposons pas de recommencer de la
même façon. Une suppression sèche laisserait entier le problème qui a fait
naître ces zones : la France est sous astreinte, {v('astreinte_air')} au plus
fort, pour des valeurs limites de pollution de l'air qu'elle devait respecter
depuis 2010 et qu'elle dépasse toujours. La restriction ne tombe donc que
lorsque la tarification la remplace, zone par zone — et elle revient de plein
droit si les valeurs limites ne sont pas tenues. La contrainte européenne
porte sur un résultat, pas sur un instrument : c'est ce qui rend la
substitution possible, et c'est aussi ce qui l'oblige à marcher.</p>
<p><strong>L'effet attendu.</strong> Le même résultat environnemental, obtenu
sans exclure de la ville ceux qui changent de voiture le plus rarement. Une
{g.terme('ZFE')} regarde l'âge du véhicule ; une tarification regarde ce qu'il
émet et où il roule — ce qui est précisément ce qu'on prétend corriger.</p>
<p><strong>L'objection la plus sérieuse.</strong> Une tarification des
émissions frappe aussi les ménages modestes, et l'expérience des
« gilets jaunes » a montré ce qu'il en coûte de l'ignorer. Elle n'est
acceptable qu'à prélèvement constant et avec restitution visible du produit —
faute de quoi elle ne sera qu'une taxe de plus, et sera rejetée comme
telle.</p>""",
        identifiant="tarification",
    )

    mesure_5 = g.cle(
        "5. Aucun grand projet sans contre-expertise publiée",
        "Tout projet dépassant un seuil fait l'objet d'une évaluation "
        "indépendante, publiée avant le vote, et son financement est décidé "
        "en même temps que lui.",
        f"""
<p><strong>Le mécanisme.</strong> L'{g.terme('évaluation socio-économique')}
existe déjà ; elle arrive après l'annonce. Nous en faisons une condition du
vote : contre-expertise indépendante publiée, hypothèses de trafic ouvertes à
la critique, et loi de financement adoptée en même temps que la
déclaration d'utilité publique.</p>
<p><strong>L'effet attendu.</strong> Moins de projets, mieux financés. Le
Grand Paris Express est passé d'environ la moitié à {v('grand_paris_express')}
sans qu'aucune révision donne lieu à un nouveau vote ; la liaison Lyon-Turin
est annoncée à {v('lyon_turin')} accès compris, ces accès n'étant ni financés
ni décidés. Nous ne disons pas que ces projets sont mauvais : nous disons que
personne ne l'a vérifié devant les électeurs.</p>
<p><strong>L'objection la plus sérieuse.</strong> Une évaluation
socio-économique repose sur des valeurs conventionnelles — le prix du temps,
celui d'une tonne de carbone — qui peuvent être choisies pour obtenir le
résultat voulu. C'est vrai. C'est un argument pour publier les hypothèses et
les soumettre à contradiction, pas pour s'en passer.</p>""",
        identifiant="projets-evaluation",
    )

    mesure_6 = g.cle(
        "6. Libérer l'offre de mobilité",
        "Autocars, transport à la demande, covoiturage, véhicules de "
        "transport avec chauffeur : ce qui n'est pas interdit pour des motifs "
        "de sécurité doit être permis, y compris là où cela concurrence un "
        "service public.",
        f"""
<p><strong>Le mécanisme.</strong> La libéralisation des autocars longue
distance de 2015 est le précédent : des liaisons de plus de cent kilomètres
étaient interdites aux cars pour protéger le train. Nous étendons la même
logique aux services de proximité — transport à la demande, navettes privées,
covoiturage organisé — en supprimant les restrictions qui ne protègent qu'un
opérateur en place.</p>
<p><strong>L'effet attendu.</strong> Une offre là où il n'y en a pas. Le marché
des autocars, qui n'existait pas avant 2015, transportait
{v('cars_longue_distance')} de passagers par an avant l'épidémie, à des prix
que le rail ne pratique pas — au bénéfice, d'abord, de ceux qui n'ont pas de
voiture.</p>
<p><strong>L'objection la plus sérieuse.</strong> Ces services écrèment les
lignes rentables et laissent au service public les dessertes qui coûtent. La
réponse tient dans la mesure 2 : quand le coût de chaque ligne est public,
l'écrémage se voit et se compense explicitement, au lieu de creuser un déficit
que personne n'analyse.</p>""",
        identifiant="offre",
    )

    mesure_7 = g.cle(
        "7. Rendre au fret des sillons, et un prix de sillon",
        "Un volume de sillons de marchandises garanti par axe et opposable, "
        "des péages ferroviaires ramenés au coût qu'un train de fret impose "
        "réellement, et des itinéraires de report pendant les travaux.",
        f"""
<p><strong>Le mécanisme.</strong> Trois textes, et aucun n'est spectaculaire.
Le contrat qui lie l'État au gestionnaire d'infrastructure inscrit un volume de
{g.terme('sillons', 'sillon')} de fret par grand axe, opposable et
assorti d'une compensation lorsqu'il n'est pas tenu. Les
{g.terme('péages ferroviaires', 'péage ferroviaire')} appliqués au fret sont
ramenés au coût que ce trafic impose au réseau, ce que le droit européen permet
et que nos voisins pratiquent. Enfin, tout chantier de régénération publie son
itinéraire de report avant de commencer.</p>
<p><strong>L'effet attendu.</strong> La part modale du rail dans les
marchandises est tombée à {v('fret_ferroviaire')}, contre {v('fret_ue')} en
moyenne européenne. Le fret ferroviaire est ouvert à la concurrence depuis
2006, et cela n'a pas suffi : la concurrence ne crée pas de sillons, elle se
partage ceux qu'on lui laisse. Un chargeur n'arbitre pas sur un prix seul, il
arbitre sur une promesse d'horaire tenue — c'est cela qu'il faut lui rendre.</p>
<p><strong>L'objection la plus sérieuse.</strong> Un sillon donné au fret est
un sillon retiré aux voyageurs, et un péage ramené au coût marginal est une
recette en moins pour le gestionnaire d'infrastructure — donc une subvention en
plus, ou une dette de plus. Les deux sont vrais. Nous assumons l'arbitrage sur
les axes où le fret a une chance, et nous refusons de le prétendre gratuit :
cette mesure coûte, et son coût doit figurer dans la loi de finances qui la
porte.</p>""",
        identifiant="fret-mesure",
    )

    mesure_8 = g.cle(
        "8. Décider maintenant ce que deviennent les autoroutes en 2031",
        "Aucune prolongation de concession ; des obligations de fin de contrat "
        "écrites tout de suite ; puis des contrats courts, de périmètre "
        "réduit, à péage plafonné et régulé — ou la redevance d'usage.",
        f"""
<p><strong>Le mécanisme.</strong> Une loi, votée avant l'échéance et non dans
l'urgence qui la suivra. Elle interdit toute prolongation des concessions
historiques, qui s'achèvent entre 2031 et 2036. Elle définit dès maintenant
l'état dans lequel le réseau doit être rendu, avec inventaire contradictoire et
garantie financière : {v('concessions_investissements')} d'investissements
restent dus par les concessionnaires avant la fin des contrats, et un
concessionnaire sortant n'a aucune raison d'entretenir au-delà du strict
nécessaire. Elle arrête enfin la suite : des contrats plus courts et de
périmètre plus réduit, remis en concurrence avec un péage plafonné et contrôlé
par l'{g.terme('ART')}, ou l'intégration du réseau concédé dans la redevance
d'usage de la mesure 3.</p>
<p><strong>L'effet attendu.</strong> Ne pas refaire 2006. Les concessions
rapportent {v('peages_ca')} de péages par an, et l'État s'apprête à récupérer
gratuitement un réseau qu'il avait vendu. La décision se prendra une fois ; si
elle se prend dans l'urgence, elle se prendra mal, et pour trente ans.</p>
<p><strong>L'objection la plus sérieuse.</strong> Une régie publique
rapporterait davantage à l'État qu'une nouvelle mise en concession, et nous ne
pouvons pas démontrer le contraire : la réponse dépend du coût de la dette
publique, de la capacité de l'État à conduire des travaux, et d'hypothèses de
trafic sur trente ans. Notre préférence pour la concurrence ne vaut pas
démonstration. Ce que nous tenons pour acquis est plus étroit : quelle que soit
la voie retenue, elle doit être choisie après une contre-expertise publiée —
c'est la mesure 5 — et jamais par une prolongation négociée en fin de
contrat.</p>""",
        identifiant="autoroutes-mesure",
    )

    financement = g.cle(
        "Ce que nous ne pouvons pas chiffrer, et pourquoi",
        "Nous n'annonçons aucune économie globale. Un tel chiffrage exigerait "
        "un modèle des coûts d'exploitation que ce dépôt ne contient pas.",
        f"""
<p>Il serait facile d'écrire qu'ouvrir les contrats régionaux à la concurrence
ferait économiser plusieurs milliards par an : il suffirait d'appliquer la
baisse de {v('baisse_couts_ter')} constatée sur les premiers lots au total des
concours publics au ferroviaire. Ce calcul serait faux, pour trois raisons
au moins.</p>
<ul class="serree">
  <li>Cette baisse porte sur le coût des lots effectivement remis en
  concurrence, à service constant — pas sur l'ensemble des concours publics,
  qui comprennent l'infrastructure, la dette et les retraites.</li>
  <li>Une autorité qui paie moins cher le train-kilomètre en achète
  généralement davantage : c'est ce qui s'est passé, l'offre ayant augmenté de
  trois quarts à deux fois sur certains lots à coût constant. L'économie s'est
  transformée en trains, ce qui est un bon résultat — mais pas une économie
  budgétaire.</li>
  <li>La transition a un coût propre, et il n'est plus vrai de le dire mal
  documenté : {v('cout_transition_ter')} par atelier de maintenance neuf,
  l'indemnisation des candidats, un quart d'effectifs supplémentaires dans les
  services TER des régions. Ce coût tombe avant les gains, et il tombe sur la
  région, pas sur l'État.</li>
</ul>
<p>Ce que nous pouvons affirmer est plus modeste, et vérifiable : sur les lots
qui ont été remis en concurrence, la collectivité paie moins cher le même
service, et paie en même temps une facture de transition que personne n'avait
anticipée. Les deux sont établis, et par la même source. Pour le reste — ce que
cela donnerait à l'échelle du pays —, le système actuel ne connaît toujours pas
ses propres coûts, et aucune des économies qu'on lui prête, dans un sens ou
dans l'autre, ne repose sur une donnée publique ligne par ligne. La deuxième
mesure de ce programme est celle qui rend les sept autres discutables.</p>""",
        identifiant="financement",
    )

    corps_sections = "\n".join([mesure_1, mesure_2, mesure_3, mesure_4,
                                mesure_5, mesure_6, mesure_7, mesure_8,
                                financement])

    return f"""
{tete}

{g.plan(corps_sections)}

{corps_sections}

{g.note(
    "Chacune de ces mesures est écrite avec l'objection qu'on lui oppose, et "
    "aucune n'est présentée comme gratuite. La page "
    "<a href='objections.html'>Objections</a> reprend les dix critiques les "
    "plus sérieuses, y compris les deux auxquelles nous répondons mal.",
    "avertissement")}

{g.appel(
    "Ce que cela change pour vous, en chiffres.",
    "Le simulateur additionne ce que vos déplacements vous coûtent "
    "aujourd'hui — taxes sur le carburant, péages, abonnement, et la part que "
    "vous payez sans la voir — puis montre comment ce même total se "
    "décompose. Tout se calcule dans votre navigateur.",
    [("Ce que vous payez vraiment", "simulateur.html", True),
     ("Les objections", "objections.html", False)],
)}
"""


# -- le simulateur -----------------------------------------------------------


def simulateur() -> str:
    tete = g.affiche(
        "Ce que vous payez",
        "Vos déplacements vous coûtent " + g.cle_texte("bien plus") + " que "
        "votre carburant et votre abonnement.",
        "D'un côté ce que vous versez — taxes sur l'énergie, péages, "
        "abonnement. De l'autre ce que la collectivité verse pour les trajets "
        "que vous faites, et dont aucun document ne vous informe. Ce "
        "simulateur met les deux côte à côte, et refuse de les mélanger avec "
        "les agrégats nationaux, qui les comprennent déjà. Tout se calcule "
        "dans votre navigateur : "
        + g.cle_texte("rien n'est envoyé nulle part") + ".",
    )

    formulaire = """
<form class="creme simulateur-court" id="formulaire">
  <div class="tete">
    <h2 class="serif">Et vous, ça fait combien&nbsp;?</h2>
    <span class="etiquette">Le simulateur</span>
  </div>
  <div class="grille">
    <div>
      <label for="motorisation">Votre véhicule<span class="aide">celui que
      vous utilisez le plus</span></label>
      <select id="motorisation" name="motorisation">
        <option value="gazole" selected>Voiture au gazole</option>
        <option value="essence">Voiture à essence</option>
        <option value="electrique">Voiture électrique</option>
        <option value="aucune">Pas de voiture</option>
      </select>
    </div>
    <div>
      <label for="kilometres">Kilomètres par an<span class="aide">la moyenne
      française est d'environ douze mille</span></label>
      <input id="kilometres" name="kilometres" type="number" inputmode="numeric"
             min="0" max="200000" step="500" value="12000">
    </div>
    <div>
      <label for="peages">Péages, par an<span class="aide">ce que vous passez
      aux barrières</span></label>
      <input id="peages" name="peages" type="number" inputmode="numeric"
             min="0" max="10000" step="10" value="150">
    </div>
    <div>
      <label for="reseau">Transport public<span class="aide">celui que vous
      empruntez</span></label>
      <select id="reseau" name="reseau">
        <option value="urbain" selected>Bus, métro, tramway</option>
        <option value="ter">Train régional</option>
        <option value="aucun">Aucun</option>
      </select>
    </div>
    <div>
      <label for="abonnement">Abonnement, par mois<span class="aide">ce que
      vous payez vous-même</span></label>
      <input id="abonnement" name="abonnement" type="number" inputmode="numeric"
             min="0" max="1000" step="1" value="60">
    </div>
    <div>
      <label for="emploi">Vous êtes<span class="aide">le versement mobilité
      pèse sur les employeurs</span></label>
      <select id="emploi" name="emploi">
        <option value="salarie" selected>En emploi</option>
        <option value="autre">Sans emploi, étudiant ou retraité</option>
      </select>
    </div>
    <div class="action"><button type="button" id="calculer">Calculer →</button></div>
  </div>
  <p class="discret" style="margin:0.9rem 0 0">Deux totaux : ce que vos
  déplacements vous coûtent visiblement, et ce que la collectivité verse pour
  les trajets que vous faites. Ce formulaire n'a ni adresse d'envoi ni méthode
  d'envoi : il ne peut rien transmettre, même si le calcul échoue.</p>
</form>"""

    resultat = """
<div id="resultat" tabindex="-1">
  <noscript>
    <div class="erreur">Ce simulateur a besoin de JavaScript : le calcul se
    fait dans votre navigateur, il n'y a pas de serveur pour le faire à sa
    place — et le bouton « Calculer » ne fait donc rien ici, plutôt que
    d'envoyer vos réponses quelque part. Les hypothèses et la formule sont
    lisibles sur la page
    <a href="donnees.html#simulateur">Données et sources</a>.</div>
  </noscript>
</div>"""

    methode = g.depliant(
        "Comment ce calcul est fait",
        f"""
<p>Le simulateur n'a aucun secret : il applique des tarifs publics à des
kilomètres et à un abonnement saisis, puis décompose le total. Voici la
formule, dans l'ordre où elle s'applique.</p>
<h4>Ce que vous voyez passer</h4>
<ul class="serree">
  <li><strong>Taxes sur le carburant</strong> : la {g.terme('TICPE')} —
  {v('ticpe_gazole')} sur le gazole, {v('ticpe_essence')} sur l'essence —
  appliquée à votre consommation, plus la TVA qui porte sur un prix incluant
  déjà cette accise. Pour un véhicule électrique, l'accise sur l'électricité
  et la TVA correspondante.</li>
  <li><strong>Péages</strong> : ce que vous déclarez, TVA comprise.</li>
  <li><strong>Abonnement</strong> : ce que vous versez vous-même, douze fois
  par an.</li>
</ul>
<h4>Ce que vous ne voyez pas</h4>
<ul class="serree">
  <li><strong>La subvention de vos propres trajets</strong>, et elle seule :
  votre abonnement couvre {v('recettes_usagers_urbain')} du coût d'un réseau
  urbain, {v('recettes_usagers_ter')} de celui d'un TER. Le simulateur en
  déduit ce que la collectivité verse pour VOS trajets, par le versement
  mobilité et par son propre budget.</li>
</ul>
<h4>Ce que ce calcul n'additionne plus, et pourquoi</h4>
<p>Jusqu'en septembre 2026, cette page ajoutait à la ligne ci-dessus deux
autres montants : votre part des {v('depense_publique_transports')} de concours
publics aux transports, et les {v('versement_mobilite')} de
{g.terme('versement mobilité')} rapportés à un actif. <strong>C'était une
erreur de calcul</strong>, et elle gonflait le seul chiffre que cette page
existe pour établir : l'agrégat des concours publics COMPREND le versement
mobilité et les subventions d'exploitation qui paient vos trajets. Les
additionner comptait le même euro deux ou trois fois.</p>
<p>Ces deux ordres de grandeur restent affichés, mais à côté du calcul et
jamais dedans. Nous les laissons parce qu'ils situent l'enjeu, et nous les
sortons du total parce qu'ils n'y ont pas leur place. Le corriger fait baisser
le chiffre qui servait notre démonstration : c'est précisément pourquoi il
fallait le corriger.</p>
<h4>Ce que la réforme changerait</h4>
<ul class="serree">
  <li><strong>La redevance d'usage remplace la taxe au litre</strong>, à
  prélèvement constant pour l'État — pas pour chaque conducteur : le
  simulateur la calcule au kilomètre, pour montrer l'ordre de grandeur de la
  substitution. Son niveau est une <strong>hypothèse de travail</strong>,
  calibrée sur un véhicule thermique moyen, pas une mesure.</li>
  <li><strong>Si vous roulez en électrique, l'écart affiché est
  considérable</strong>, et nous ne l'avons pas adouci. Un véhicule électrique
  acquitte {v('accise_electricite')} d'accise sur ce qu'il consomme, soit
  plus de six fois moins au kilomètre qu'un véhicule thermique, pour une
  chaussée qui s'use pareillement. C'est l'anomalie que la redevance corrige,
  et c'est aussi pourquoi la mesure 3 prévoit une entrée par paliers.</li>
  <li><strong>Le reste ne bouge pas</strong> : la subvention de vos trajets
  et les concours publics restent ce qu'ils sont. Ils deviennent visibles,
  c'est tout — et c'est le sujet de ce site.</li>
</ul>
{g.note(
    "Ce simulateur illustre des ORDRES DE GRANDEUR. Il ne prédit ni votre "
    "facture, ni le coût de vos trajets, et il ne chiffre pas la réforme à "
    "l'échelle du pays — voir <a href='reforme.html#financement'>ce que nous "
    "pouvons affirmer et ce que nous ne pouvons pas</a>. Chacune de ses "
    "hypothèses est écrite, datée et discutable sur la page "
    "<a href='donnees.html#simulateur'>Données et sources</a>.",
    "avertissement")}""",
        "methode-simulateur",
    )

    return f"""
{tete}

{formulaire}

{resultat}

{methode}

{g.appel(
    "Le total vous surprend ? C'est le sujet.",
    "Un prélèvement qu'on ne voit pas n'est jamais discuté. Rendre visible ce "
    "que les transports coûtent et à qui est la première mesure de ce "
    "programme, et la seule qui ne coûte rien.",
    [("La réforme en huit mesures", "reforme.html", True),
     ("Pourquoi ça coûte autant", "diagnostic.html", False)],
)}
"""


# -- objections --------------------------------------------------------------


def objections() -> str:
    tete = g.affiche(
        "Objections",
        "Seize critiques, " + g.cle_texte("dont trois auxquelles nous "
                                          "répondons mal") + ".",
        "Un programme qui ne publierait que les objections qu'il sait "
        "démolir ne mériterait pas d'être lu. Les seize qui suivent sont les "
        "plus sérieuses que nous connaissions ; les trois dernières sont "
        "celles où notre réponse est incomplète, et nous le disons plutôt "
        "que d'en fabriquer une.",
    )

    o_ecotaxe = g.cle(
        "« L'écotaxe a déjà échoué, vous allez recommencer »",
        "L'objection est fondée, et c'est notre propre pays qui en fait la "
        "preuve. La différence tient en un mot : l'écotaxe était une taxe de "
        "plus, la redevance est une taxe à la place.",
        f"""
<p>Rappelons l'échec plutôt que de l'attendre : votée sans opposition,
construite, dotée de cent soixante-quatorze portiques, l'écotaxe poids lourds a
été suspendue en octobre 2013 devant la fronde des « bonnets rouges », et le
contrat résilié un an plus tard. Le contribuable a versé {v('ecotaxe_cout')}
pour une taxe qui n'a jamais rien perçu. La Cour des comptes y a vu un échec de
politique publique, et elle avait raison.</p>
<p>Trois choses l'ont tuée, et nous en tirons trois règles. Elle s'ajoutait aux
prélèvements existants sans qu'aucun ne baisse : notre texte éteint la taxe au
litre dans le même article, ou il n'est pas déposé. Elle frappait d'abord une
profession organisée, sans contrepartie visible pour elle : la redevance
remplace ce que les transporteurs acquittent déjà sur leur gazole. Elle était
collectée par un dispositif privé complexe dont le coût a nourri le soupçon :
nous proposons le relevé de compteur au contrôle technique, qui n'exige aucun
portique.</p>
<p>Ce que nous ne prétendons pas : que ces trois différences suffisent. Une
réforme de la fiscalité des carburants peut échouer pour des raisons qui n'ont
rien à voir avec son dessin, et la France en a fait deux fois l'expérience,
avec l'écotaxe puis avec les « gilets jaunes ». C'est pourquoi la bascule est
progressive, expérimentale et réversible — pas parce que nous doutons de la
mesure, mais parce que nous avons lu ce qui est arrivé aux précédentes.</p>""",
        identifiant="ecotaxe",
    )

    o_recentralisation = g.cle(
        "« Obliger les régions à mettre en concurrence, c'est recentraliser »",
        "L'objection vise juste, et elle vient de notre propre camp. Nous y "
        "répondons par la soupape : l'obligation n'est pas d'attribuer à un "
        "concurrent, elle est de s'expliquer publiquement quand on ne met pas "
        "en concurrence.",
        """
<p>Un programme libéral qui impose une procédure aux collectivités doit
s'expliquer. La libre administration des collectivités territoriales est un
principe constitutionnel, et une loi nationale qui dicterait aux régions le
mode d'attribution de leurs contrats heurterait à la fois ce principe et notre
propre préférence pour les décisions prises au plus près.</p>
<p>D'où la forme retenue, qui n'est pas une obligation d'attribuer mais une
obligation de motiver. La région garde le droit de reconduire son opérateur
sans appel d'offres ; elle doit dire pourquoi, publiquement, devant ses
électeurs. C'est l'inversion de la charge de la preuve, pas la confiscation du
choix. Un exécutif régional qui assume devant les siens de payer plus cher
pour ne pas changer d'opérateur est dans son droit ; un exécutif qui le fait
sans avoir à le dire ne l'est pas moins, mais personne ne peut le lui
reprocher, et c'est cela que nous changeons.</p>
<p>Ajoutons que l'échéance ne vient pas de nous : le droit européen impose la
mise en concurrence des services conventionnés d'ici la fin 2033. La question
n'est pas de savoir si les régions s'y mettront, mais si elles s'y mettent en
ordre ou dans l'urgence — et le rapport sénatorial de 2026 penche pour
l'urgence.</p>""",
        identifiant="recentralisation",
    )

    o_electriques = g.cle(
        "« Votre redevance va faire payer six fois plus les voitures "
        "électriques »",
        "C'est exact, et notre simulateur l'affiche. Un véhicule électrique "
        "use la route comme un autre et ne paie presque rien pour elle : "
        "c'est l'anomalie, pas la correction.",
        f"""
<p>Un véhicule électrique acquitte l'accise sur l'électricité,
{v('accise_electricite')} — rapporté au kilomètre, plus de six fois moins
qu'un véhicule thermique sur son carburant. Cet écart n'a jamais été décidé :
il résulte du fait qu'une taxe au litre ne sait taxer qu'un litre. Il grandit
mécaniquement à mesure que le parc s'électrifie, et il emporte avec lui le
financement de la route.</p>
<p>Nous ne le corrigeons pas d'un coup pour autant. Des centaines de milliers
de personnes ont acheté un véhicule électrique sous un régime fiscal donné,
souvent à notre invitation collective ; leur appliquer le tarif plein dès la
première année serait leur changer les règles après coup. La redevance leur
est donc appliquée par paliers, sur la durée d'un mandat.</p>
<p>Ce que nous n'accepterons pas, c'est de laisser croire que la question ne se
pose pas. Elle se posera à quiconque gouvernera, libéral ou non, le jour où la
taxe sur les carburants aura cessé de rapporter.</p>""",
        identifiant="electriques",
    )

    o_gratuite = g.cle(
        "« Pourquoi pas la gratuité des transports ? »",
        "Parce qu'un prix nul est un prix, et le moins informatif de tous. La "
        "gratuité ne supprime pas le coût : elle le déplace vers l'employeur "
        "et le contribuable, et elle efface le dernier signal qui restait.",
        f"""
<p>Un réseau gratuit reste payé : par le {g.terme('versement mobilité')}, donc
par les employeurs, et par le budget de la collectivité, donc par l'impôt
local. Le taux de couverture par l'usager tombe à zéro, et avec lui toute
possibilité de savoir si l'offre correspond à la demande. Or le taux moyen a
déjà reculé — il est de {v('recettes_usagers_urbain')} sur les réseaux urbains
de province — à mesure que l'offre et la gratuité progressaient plus vite que
la fréquentation.</p>
<p>Notre désaccord n'est pas moral. Il est que la gratuité résout un problème
d'accès — certains ne peuvent pas payer — par un instrument qui s'applique à
tous, y compris à ceux qui peuvent. La tarification sociale résout le même
problème en visant ceux qui en ont besoin, et laisse le prix dire quelque
chose aux autres. C'est pourquoi nous proposons de rendre les réductions
existantes explicites et financées, et non de les étendre à tout le monde.</p>
<p>Une nuance, tout de même, que l'honnêteté impose : sur un petit réseau où la
recette commerciale couvre à peine le coût de la percevoir, la gratuité peut
être le choix rationnel. Ce n'est pas une position de principe contre, c'est
une position contre la gratuité comme principe.</p>""",
        identifiant="gratuite",
    )

    o_perimetre = g.cle(
        "« Votre programme ignore l'avion, le vélo et l'accessibilité »",
        "En partie vrai. Ce volet porte sur le ferroviaire, la route et les "
        "transports collectifs ; voici ce que nous pensons du reste, plutôt "
        "que de laisser le silence répondre.",
        """
<ul class="serree">
  <li><strong>L'aérien.</strong> Le carburant des vols commerciaux est exonéré
  d'accise, quand celui des automobilistes est l'un des plus taxés d'Europe.
  C'est une distorsion, et un libéral n'a aucune raison de la défendre : nous
  soutenons la fin de cette exonération, qui se décide au niveau européen et
  international, et non par une loi française. D'ici là, nous nous opposons au
  subventionnement de lignes aériennes intérieures qui concurrencent un train
  lui-même subventionné : payer deux fois pour le même trajet est le contraire
  d'une politique.</li>
  <li><strong>Le vélo et la marche.</strong> Ils ne relèvent pas d'un volet
  national : les aménagements se décident et se paient localement, et nous ne
  proposons pas de le changer. Ce que notre programme leur apporte est
  indirect mais réel — une tarification des nuisances qui renchérit la voiture
  là où elle gêne, et la publication du coût par usager, qui rend enfin
  comparable ce qu'une collectivité dépense par déplacement en bus, en train
  ou en piste cyclable.</li>
  <li><strong>L'accessibilité.</strong> C'est une obligation légale, et notre
  mesure 1 lui donne un levier qu'elle n'a pas aujourd'hui : ce qui figure au
  cahier des charges d'un appel d'offres est exigible et pénalisable, ce qui
  figure dans un plan pluriannuel ne l'est pas. Nous proposons que le niveau
  d'accessibilité attendu soit une clause contractuelle notée, au même titre
  que la ponctualité.</li>
  <li><strong>L'outre-mer et la Corse.</strong> La continuité territoriale est
  exactement ce que nous appelons une
  """ + g.terme("obligation de service public") + """ : un service que le
  marché ne rendrait pas seul, que la collectivité achète explicitement.
  Qu'elle soit chiffrée et votée plutôt que noyée dans un déficit vaut là
  autant qu'ailleurs.</li>
  <li><strong>Les ports.</strong> Nous n'en traitons pas, et nous n'avons pas
  de position arrêtée. Le dire vaut mieux que d'improviser.</li>
</ul>""",
        identifiant="perimetre",
    )

    o1 = g.cle(
        "« Privatiser le rail, c'est le fiasco britannique »",
        "Le fiasco britannique est réel, et ce n'est pas ce que nous "
        "proposons : nous ne vendons ni les voies, ni les gares, et nous "
        "décrivons pour les trains régionaux le modèle allemand, pas le "
        "modèle des franchises.",
        """
<p>Le Royaume-Uni a fragmenté son réseau entre un gestionnaire
d'infrastructure privé et des dizaines de franchises, avec des interfaces
contractuelles si nombreuses que personne ne portait plus le risque. Railtrack
a été renationalisée en 2002, les franchises abandonnées depuis 2020.</p>
<p>Ce que nous proposons laisse l'infrastructure publique, garde l'autorité
organisatrice maîtresse du service, et met en concurrence le seul contrat
d'exploitation — ce que font l'Allemagne depuis 1996 et la France elle-même,
depuis toujours, pour ses bus urbains. Si l'argument britannique valait contre
notre proposition, il vaudrait contre la manière dont sont exploités
aujourd'hui les réseaux de bus de presque toutes les villes françaises.</p>""",
        identifiant="britannique",
    )

    o2 = g.cle(
        "« La concurrence fermera les petites lignes »",
        "C'est l'autorité organisatrice qui décide des lignes, pas "
        "l'exploitant. Les fermetures des vingt dernières années ont eu lieu "
        "sous monopole, faute d'argent pour l'entretien.",
        f"""
<p>Un exploitant qui remporte un appel d'offres exécute un cahier des charges :
il ne choisit ni les lignes, ni les horaires, ni les tarifs. Il peut perdre le
contrat ; il ne peut pas supprimer un train que la collectivité a décidé
d'acheter.</p>
<p>La menace réelle sur les petites lignes est ailleurs : {v('petites_lignes')}
de lignes peu circulées dont la remise en état dépend de contrats
État-régions signés ligne par ligne et rarement financés jusqu'au bout. Un
réseau qu'on n'entretient pas se ferme tout seul — c'est le mode de fermeture
le plus courant en France, et il n'a besoin d'aucune concurrence.</p>""",
        identifiant="petites-lignes",
    )

    o3 = g.cle(
        "« Le train ne sera jamais rentable, donc la concurrence n'a pas de sens »",
        "La plupart des services ferroviaires ne couvrent pas leurs coûts, et "
        "ne les couvriront pas. C'est exactement pourquoi il faut les acheter "
        "par appel d'offres : on met en concurrence le prix de la subvention.",
        """
<p>La confusion est fréquente : mettre en concurrence ne veut pas dire rendre
rentable. Dans une délégation de service public, les candidats se disputent le
droit d'exécuter un service déficitaire, et gagnent celui qui demande la plus
faible compensation pour le même cahier des charges. L'argent public reste, et
c'est son montant qui est mis en jeu.</p>
<p>C'est ainsi que fonctionnent déjà les réseaux de bus français, les trains
régionaux allemands et les liaisons subventionnées de la plupart des pays
européens. Personne n'y a attendu la rentabilité pour introduire une
comparaison.</p>""",
        identifiant="rentabilite",
    )

    o4 = g.cle(
        "« Vous voulez faire payer la route »",
        "Elle est déjà payée, et mal : " + v("ticpe") + " de taxe au litre, "
        "prélevés partout au même tarif, sans lien avec une route.",
        f"""
<p>Précision que nous devons à l'honnêteté, parce que ce site a écrit le
contraire : la {g.terme('TICPE')} ne part pas tout entière au budget général.
L'État en garde environ la moitié, les collectivités en reçoivent une large
part, l'agence des infrastructures une fraction. Ce qui est vrai — et qui
suffit — c'est qu'aucune de ces parts n'est liée à une dépense
d'infrastructure identifiée : elles alimentent des budgets, pas des routes.
L'automobiliste paie donc une accise parmi les plus élevées d'Europe sans
qu'aucun entretien lui soit garanti en retour. Notre proposition ne consiste
pas à faire payer un usage gratuit, mais à remplacer un prélèvement aveugle
par un prix qui dépend du lieu, de l'heure et de la nuisance — à recettes
constantes.</p>
<p>Un effet secondaire, rarement relevé : la taxe au litre s'effondre à mesure
que le parc s'électrifie, alors que l'usure des routes, elle, ne diminue pas.
Un financement adossé au carburant est un financement en voie d'extinction, et
la question se posera de toute façon.</p>""",
        identifiant="payer-route",
    )

    o5 = g.cle(
        "« Une redevance kilométrique, c'est le flicage des déplacements »",
        "C'est l'objection la plus sérieuse, et elle porte. Nous proposons "
        "deux modalités sans géolocalisation, et l'interdiction dans la loi "
        "de constituer un fichier des trajets.",
        """
<p>Un dispositif qui relèverait en continu la position des véhicules serait
inacceptable, et nous ne le proposons pas. Deux modalités s'en passent : le
forfait kilométrique déclaré, régularisé au relevé annuel du compteur lors du
contrôle technique ; et le badge à comptage local, qui ne transmet qu'un total
de kilomètres par zone tarifaire, sans horodatage.</p>
<p>Nous n'affirmons pas que la question soit close. Un dispositif technique
n'a jamais protégé personne contre une loi ultérieure qui l'élargirait, et
c'est pourquoi l'interdiction du fichier doit figurer dans le texte
lui-même — une garantie de niveau constitutionnel serait plus solide encore,
et nous y sommes favorables.</p>""",
        identifiant="vie-privee",
    )

    o6 = g.cle(
        "« Vous allez pénaliser les ruraux »",
        "La fiscalité actuelle les pénalise davantage : elle taxe chaque "
        "litre au même tarif, là où l'alternative au véhicule n'existe pas.",
        f"""
<p>Un habitant d'une zone peu dense roule plus, paie donc plus de
{g.terme('TICPE')}, et reçoit en retour une offre de transport public qui va
de faible à inexistante. La modulation par zone que nous proposons joue
mécaniquement en sa faveur : la redevance est plus élevée là où la congestion
et la pollution sont fortes, c'est-à-dire là où il ne roule pas.</p>
<p>Cela ne suffit pas à régler la question. Une réforme à prélèvement constant
fait des gagnants et des perdants, et prétendre le contraire serait malhonnête.
C'est pourquoi la bascule est progressive, expérimentée d'abord dans une région
volontaire, et suspendue si le bilan ne tient pas ses promesses.</p>""",
        identifiant="ruraux",
    )

    o7 = g.cle(
        "« Sans zones à faibles émissions, la pollution va continuer »",
        "L'objectif n'est pas discuté ; l'instrument l'est. Une "
        + g.terme("ZFE") + " regarde l'âge du véhicule, une tarification "
        "regarde ce qu'il émet et où il roule.",
        """
<p>Deux véhicules du même âge n'émettent pas la même chose, et deux véhicules
identiques ne nuisent pas également selon qu'ils traversent un boulevard
saturé ou une route de campagne. Un critère d'âge est une approximation
grossière d'une nuisance qu'on sait aujourd'hui mesurer autrement.</p>
<p>Ajoutons ce que l'interdiction fait socialement : elle exclut de la ville
ceux qui changent de voiture le plus rarement, c'est-à-dire ceux qui en ont le
moins les moyens. Un prix, lui, laisse le choix — rouler moins, rouler
autrement, ou payer ce que cela coûte aux autres.</p>
<p>Mais l'objectif, lui, n'est pas négociable, et l'épisode de 2026 le montre :
le Parlement a supprimé les zones à faibles émissions, le Conseil
constitutionnel a censuré la suppression pour un motif de procédure, et rien
n'aurait été réglé si elle avait tenu. La France est sous astreinte,
{v('astreinte_air')} au plus fort, pour des valeurs limites qu'elle devait
respecter depuis 2010. C'est pourquoi notre mesure 4 ne supprime rien à sec :
la restriction ne tombe que là où la tarification la remplace, et elle revient
de plein droit si les valeurs limites ne sont pas tenues.</p>""",
        identifiant="zfe",
    )

    o8 = g.cle(
        "« L'ouverture dégradera les conditions de travail des cheminots »",
        "Le cadre social est fixé par la convention collective de branche et "
        "par la loi, pas par l'identité de l'employeur.",
        """
<p>Les appels d'offres régionaux français se déroulent avec transfert
obligatoire des personnels concernés et maintien de leur rémunération. La
question du cadre social se traite dans la convention de branche, qui
s'impose à tous les opérateurs — y compris aux nouveaux entrants, qui ne
peuvent donc pas concourir sur le dumping salarial.</p>
<p>Ce qui est vrai, en revanche, c'est que la mise en concurrence change
l'organisation du travail, et que les gains de productivité constatés
ailleurs viennent en partie de là. C'est un sujet de négociation sociale
sérieux, pas un argument pour maintenir un contrat qu'aucune comparaison ne
vient éclairer.</p>""",
        identifiant="social",
    )

    o9 = g.cle(
        "« Vous ne chiffrez pas votre réforme » — et c'est vrai",
        "Nous n'annonçons aucune économie globale, parce que nous ne savons "
        "pas la calculer honnêtement. C'est une faiblesse de ce programme, et "
        "nous préférons l'écrire.",
        f"""
<p>Appliquer la baisse allemande de
{v('baisse_couts_allemagne').lstrip('≈ ')} au total des concours publics
donnerait un chiffre spectaculaire et faux : cette baisse porte sur les lots
effectivement remis en concurrence, à service constant, et non sur un agrégat
qui comprend l'infrastructure, la dette et les retraites.</p>
<p>Un chiffrage sérieux exigerait un modèle des coûts d'exploitation ligne par
ligne, que personne ne publie — et c'est précisément ce que la mesure 2 vise à
rendre possible. Voir <a href="reforme.html#financement">ce que nous pouvons
affirmer et ce que nous ne pouvons pas</a>.</p>""",
        identifiant="chiffrage",
    )

    o10 = g.cle(
        "« Le vrai problème, c'est le financement du rural » — et nous y "
        "répondons mal",
        "Rendre la subvention visible ne dit pas quel niveau de desserte la "
        "collectivité doit acheter. Cette question reste ouverte, et elle est "
        "politique.",
        f"""
<p>Notre programme améliore l'information : il dira ce que coûte chaque ligne
et par voyageur. Il ne dit pas combien la collectivité doit consentir à payer
pour qu'un bourg de quinze cents habitants garde trois allers-retours par
jour. Aucune méthode ne le dit : c'est un arbitrage de valeurs, entre
l'aménagement du territoire et l'emploi alternatif du même argent.</p>
<p>Nous assumons une préférence — une {g.terme('obligation de service public')}
explicite, chiffrée et votée, plutôt qu'un déficit d'entreprise publique — mais
elle ne tranche pas le montant. Ceux qui nous opposent que la transparence
servira surtout à fermer des lignes ont un argument que nous ne pouvons pas
réfuter par le calcul.</p>""",
        identifiant="rural",
    )

    o_garanties = g.cle(
        "« Vos garanties ne valent que jusqu'à la prochaine loi » — et c'est "
        "vrai",
        "Une affectation de recette se défait par une loi de finances, et une "
        "interdiction de fichier par une loi ordinaire. Nous n'avons pas de "
        "réponse qui ferme la question.",
        """
<p>Notre programme repose sur des engagements de méthode : publier les coûts,
mettre en concurrence sauf motivation publique, affecter le produit de la
redevance, ne constituer aucun fichier des trajets. Tous prennent la forme
d'une loi, et une loi se défait par une loi. La TICPE en est la démonstration :
son affectation aux routes a disparu sans que personne ne s'en aperçoive.</p>
<p>Ce que nous pouvons faire, nous le proposons : inscrire l'affectation et
l'interdiction du fichier dans une loi organique, qui ne se modifie pas au
détour d'un budget, et nous déclarer favorables à une garantie
constitutionnelle pour la protection des déplacements. Ce que nous ne pouvons
pas faire, c'est lier une majorité future. Un programme qui prétendrait le
contraire mentirait sur ce qu'est une loi.</p>
<p>Reste un argument, et il est faible : la transparence, elle, est difficile à
défaire. Une donnée publiée pendant cinq ans a des usagers, des journalistes et
des élus qui s'en servent, et la supprimer se voit. C'est peu, et c'est
pourtant la seule de nos garanties qui se défende toute seule.</p>""",
        identifiant="garanties-fragiles",
    )

    corps_sections = "\n".join([o1, o2, o3, o4, o5, o6, o7, o8,
                                o_ecotaxe, o_recentralisation, o_electriques,
                                o_gratuite, o_perimetre,
                                o9, o10, o_garanties])

    return f"""
{tete}

{g.plan(corps_sections, "Les seize objections")}

{corps_sections}

{g.note(
    "Les trois dernières objections sont celles auxquelles nous répondons "
    "mal. Elles restent en ligne pour cette raison : un programme qui "
    "effacerait ses points faibles au premier contact serait un programme "
    "qu'on ne pourrait pas discuter.",
    "avertissement")}

{g.appel(
    "Une objection qui manque ?",
    "Ce site est ouvert : ses textes, ses chiffres et le code qui l'engendre "
    "sont dans un dépôt public. Une critique argumentée y a sa place, et les "
    "chiffres que nous marquons « à vérifier » attendent qu'on les confronte "
    "à leur source.",
    [("Le dépôt, textes et chiffres compris", g.DEPOT, True),
     ("Toutes nos données", "donnees.html", False)],
)}
"""


# -- qui publie ce site ------------------------------------------------------


def mentions() -> str:
    """Les mentions légales, et ce que ce site ne collecte pas.

    Elle manquait, et c'était la faille la moins coûteuse à corriger : un site
    politique sans éditeur nommé se fait signaler en une journée, et le
    reproche — « on ne sait pas qui parle » — porte d'autant mieux que tout le
    reste du site est consacré à la transparence.
    """
    tete = g.affiche(
        "Qui publie ce site",
        "Un éditeur nommé, " + g.cle_texte("aucune donnée collectée") + ".",
        "Un site qui demande à ses lecteurs de vérifier ses chiffres doit "
        "commencer par dire qui l'écrit, qui le paie, et ce qu'il fait de "
        "leur visite. La réponse à la dernière question est : rien.",
    )

    editeur = g.cle(
        "L'éditeur et le directeur de la publication",
        "Ce site est édité par le " + g.EDITEUR + ".",
        f"""
<ul class="serree">
  <li><strong>Éditeur</strong> : {g.EDITEUR}.</li>
  <li><strong>Siège</strong> : {g.SIEGE_EDITEUR}.</li>
  <li><strong>Directeur de la publication</strong> :
  {g.DIRECTEUR_PUBLICATION}.</li>
  <li><strong>Contact</strong> : {g.CONTACT}.</li>
  <li><strong>Hébergeur</strong> : {g.HEBERGEUR}.</li>
</ul>
<p>Ce site est un document politique. Il n'est ni une source officielle, ni un
service d'information sur les transports : pour vos trajets, voyez votre
autorité organisatrice.</p>""",
        identifiant="editeur",
    )

    donnees_perso = g.cle(
        "Ce que ce site collecte : rien",
        "Aucun compte, aucun cookie, aucune mesure d'audience, aucune "
        "ressource chargée chez un tiers. Le simulateur calcule dans votre "
        "navigateur et n'a aucun moyen d'envoyer quoi que ce soit.",
        """
<ul class="serree">
  <li><strong>Pas de cookie, pas de mesure d'audience.</strong> Ce site
  n'installe rien sur votre appareil et ne compte pas ses visiteurs.</li>
  <li><strong>Aucune ressource tierce.</strong> Polices, pictogrammes, feuille
  de style : tout vient de ce site. Une requête vers un serveur extérieur
  emporterait votre adresse IP chez lui, et un témoin automatique vérifie
  qu'aucune page n'en fait.</li>
  <li><strong>Le simulateur ne transmet rien.</strong> Son formulaire n'a ni
  adresse ni méthode d'envoi, et son bouton n'est pas un bouton de
  soumission : même si le calcul échouait, vos réponses ne pourraient pas
  quitter la page. Ce n'était pas le cas avant septembre 2026, et c'est une
  correction, pas une précaution.</li>
</ul>
<p>Une réserve, parce qu'elle est vraie et qu'on ne la lit jamais :
<strong>l'hébergeur, lui, voit votre adresse IP</strong>, comme tout serveur
qui vous envoie une page. Nous n'y avons pas accès et n'en faisons rien, mais
promettre l'anonymat complet serait un mensonge technique.</p>""",
        identifiant="donnees-personnelles",
    )

    financement = g.cle(
        "Ce que ce site coûte, et qui le paie",
        "L'hébergement est gratuit, le site ne diffuse aucune publicité et ne "
        "reçoit aucun paiement.",
        f"""
<p>Ce site est une collection de pages statiques hébergées gratuitement. Il
n'affiche aucune publicité commerciale, ne vend rien, ne sollicite aucun don
et n'a aucun moyen d'encaisser quoi que ce soit. Ses frais éventuels — un nom
de domaine — sont pris en charge par le {g.EDITEUR}.</p>
<p>En période électorale, les dépenses de propagande d'un parti obéissent à
des règles de financement et de comptabilisation précises. Le détail des
dépenses engagées pour ce site relève du mandataire financier du
{g.EDITEUR} : {g.CONTACT}.</p>""",
        identifiant="financement",
    )

    reutilisation = g.cle(
        "Réutiliser, corriger, contredire",
        "Les textes sont sous licence libre, le code aussi, et le dépôt est "
        "public : une critique argumentée peut être déposée là où le site est "
        "écrit.",
        f"""
<ul class="serree">
  <li><strong>Textes et contenus</strong> : Creative Commons BY-SA 4.0. Vous
  pouvez les reprendre, y compris pour nous contredire, à condition de citer
  la source et de partager aux mêmes conditions.</li>
  <li><strong>Code</strong> : licence Apache 2.0.</li>
  <li><strong>Polices</strong> : SIL Open Font License.
  <strong>Pictogrammes</strong> : Lucide, licence ISC.</li>
</ul>
<p>Une erreur de chiffre, une source mal citée, une objection qui manque : le
dépôt est ouvert, et c'est là que cela se corrige.
<a href="{g.DEPOT}">{g.DEPOT}</a></p>
<p>Les chiffres marqués « à vérifier » sur la page
<a href="donnees.html">Données et sources</a> attendent précisément qu'on les
confronte à leur source. Nous préférons qu'un contradicteur le fasse avant un
débat plutôt que pendant.</p>""",
        identifiant="reutilisation",
    )

    corps_sections = "\n".join([editeur, donnees_perso, financement,
                                 reutilisation])

    return f"""
{tete}

{g.plan(corps_sections)}

{corps_sections}
"""


# -- données et sources ------------------------------------------------------


def page_donnees() -> str:
    tete = g.affiche(
        "Données et sources",
        "Chaque chiffre, " + g.cle_texte("sa source et sa date") + ".",
        "Un chiffre sans source est une opinion. Tous ceux que ce site "
        "emploie sont ici, avec leur millésime, leur origine et leur degré de "
        "fiabilité — y compris ceux que nous vous demandons de vérifier avant "
        "de les citer.",
    )

    lignes = []
    for chiffre in donnees.CHIFFRES:
        source = (f'<a href="{chiffre.lien}">{chiffre.source}</a>'
                  if chiffre.lien else chiffre.source)
        lignes.append([
            f'<span id="{chiffre.cle}">{chiffre.valeur}</span>',
            chiffre.libelle,
            chiffre.annee,
            source,
            g.etiquette_fiabilite(chiffre.fiabilite),
        ])
    table = g.tableau(
        ["Chiffre", "Ce qu'il mesure", "Année", "Source", "Fiabilité"],
        lignes,
        ["nombre", "texte", "date", "long texte", ""],
        "Tous les chiffres cités sur ce site",
    )

    precisions = "".join(
        g.depliant(
            f"{chiffre.valeur} — {chiffre.libelle}",
            f"<p>{chiffre.precision}</p>"
            f'<p class="discret">{chiffre.source} · {chiffre.annee} · '
            f"{g.etiquette_fiabilite(chiffre.fiabilite)}</p>",
            f"detail-{chiffre.cle}",
        )
        for chiffre in donnees.CHIFFRES if chiffre.precision
    )

    pays = g.tableau(
        ["Pays", "Source des deux chiffres", "Année", "Fiabilité"],
        [[f"{p.drapeau} {p.nom}", p.source, p.annee,
          g.etiquette_fiabilite(p.fiabilite)]
         for p in donnees.PAYS],
        ["", "long texte", "date", ""],
        "D'où viennent les comparaisons internationales",
    )

    # Engendré depuis la table des paramètres, et non recopié : une valeur
    # recopiée à la main dans un tableau est une valeur qui finira par dire
    # autre chose que le calcul.
    parametres = g.tableau(
        ["Hypothèse", "Valeur", "Ce qu'elle représente"],
        [[f"<code>{cle_param}</code>", donnees.parametre_affiche(cle_param),
          description]
         for cle_param, (_, description)
         in donnees.DESCRIPTIONS_SIMULATEUR.items()],
        ["", "nombre", "long texte"],
        "Les hypothèses du simulateur, toutes",
    )

    reserves = "".join(
        f"<li><strong>{cle_param}</strong> — {texte}</li>"
        for cle_param, texte in donnees.RESERVES_SIMULATEUR
    )

    methode = g.cle(
        "Comment ce site est fait",
        "Sept pages HTML statiques, engendrées par un script Python depuis un "
        "seul jeu de textes et de chiffres. Aucun serveur, aucune ressource "
        "tierce, aucun traceur.",
        f"""
<ul class="serree">
  <li><strong>Les chiffres n'existent qu'une fois</strong>, dans
  <code>src/transports/donnees.py</code>. Les pages les appellent par leur
  clé : un chiffre ne peut donc pas dire une chose ici et une autre là, et
  cette page-ci est engendrée par la même table.</li>
  <li><strong>Le site ne charge rien d'un tiers.</strong> Les polices, les
  pictogrammes et la feuille de style sont servis par le dépôt. Aucune requête
  vers un serveur extérieur n'emporte votre adresse IP.</li>
  <li><strong>Le simulateur calcule dans votre navigateur.</strong> Aucune
  saisie n'est transmise, enregistrée ni mesurée.</li>
  <li><strong>L'apparence est celle du site
  <a href="{g.SITE_RETRAITES}">retraitecomptenotionelle</a></strong>, dont la
  feuille de style est reprise presque à l'identique, comme l'a fait avant
  nous le volet <a href="{g.SITE_SANTE}">santé</a> : les volets d'un même
  programme doivent se reconnaître.</li>
  <li><strong>Tout est ouvert</strong> : <a href="{g.DEPOT}">le dépôt</a>
  contient les textes, les chiffres, le script de construction et cette
  page.</li>
</ul>""",
        identifiant="methode",
    )

    limites = g.cle(
        "Ce que ce site ne fait pas",
        "Il ne modélise rien, ne chiffre pas la réforme à l'échelle du pays, "
        "et ne remplace aucune source officielle.",
        f"""
<ul class="serree">
  <li><strong>Aucun modèle des coûts de transport.</strong> Les chiffres cités
  sont recopiés de publications ; le seul calcul du site est celui du
  simulateur, et il applique des tarifs publics à une saisie.</li>
  <li><strong>Aucun chiffrage global de la réforme.</strong> Voir
  <a href="reforme.html#financement">ce que nous pouvons affirmer et ce que
  nous ne pouvons pas</a>.</li>
  <li><strong>Beaucoup de chiffres à vérifier.</strong> Ceux marqués
  {g.etiquette_fiabilite('verifier')} sont de seconde main. Le transport est
  un domaine où les périmètres comptables varient d'une publication à
  l'autre : ils doivent être confrontés à leur source avant toute reprise
  publique, et le site le dit partout où ils paraissent plutôt que dans une
  note que personne n'ouvre.</li>
  <li><strong>Aucune valeur officielle.</strong> Pour vos trajets, vos tarifs
  et vos droits, seules votre autorité organisatrice et
  <a href="https://www.service-public.fr/">service-public.fr</a> font foi.</li>
</ul>""",
        identifiant="limites",
    )

    return f"""
{tete}

<h2>Tous les chiffres</h2>
{table}

<h2>Le détail, chiffre par chiffre</h2>
{precisions}

<h2 id="pays">Les comparaisons internationales</h2>
<p>Les six pays comparés portent chacun leur source, leur millésime et leur
réserve — celle-ci est écrite dans la fiche du pays, sur la page
<a href="comparaisons.html">Ailleurs</a>, et non reléguée ici.</p>
{pays}

<h2 id="simulateur">Les hypothèses du simulateur</h2>
<p>Le simulateur applique des tarifs publics à des kilomètres et à un
abonnement saisis, puis décompose le total. Ses paramètres sont écrits une
seule fois, dans <code>src/transports/donnees.py</code>, et déposés dans
<code>moteur/donnees.json</code> que la page lit au chargement.</p>
{parametres}
<h3>Les réserves qui comptent</h3>
<ul class="serree">{reserves}</ul>
{g.note(
    "Les hypothèses marquées « ordre de grandeur », « agrégat reconstitué » "
    "ou « hypothèse de travail » ne sont pas des mesures. Un débat public "
    "sérieux exige qu'on les distingue des chiffres publiés, et ce site "
    "refuse de les présenter autrement.",
    "avertissement")}

{methode}
{limites}
"""
