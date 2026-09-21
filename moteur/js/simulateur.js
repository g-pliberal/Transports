// Le simulateur : ce que les déplacements d'une personne lui coûtent, et par
// quels guichets.
//
// Il tient en un fichier et n'emploie aucune bibliothèque, pour la même raison
// que le reste du site : la page ne demande rien à un tiers, et la promesse
// faite à qui remplit le formulaire — « tout se calcule dans votre navigateur,
// rien n'est envoyé » — ne souffre aucune requête sortante.
//
// Ses paramètres ne sont PAS écrits ici. Ils viennent de `moteur/donnees.json`,
// lui-même écrit depuis `src/transports/donnees.py` : le taux qu'affiche la
// page « Données et sources » et celui qu'applique ce calcul sont le même
// nombre, et ne peuvent pas diverger. Un témoin du dépôt vérifie qu'aucune
// constante ne s'est glissée ici.
//
// Ce que ce fichier ne prétend pas être : un modèle. Il applique des tarifs
// publics à des kilomètres saisis, puis range le résultat en deux colonnes —
// ce qui passe devant vous, ce qui passe ailleurs. Il n'annonce aucune
// économie : le site dit ailleurs qu'il ne sait pas chiffrer la réforme, et il
// ne le saurait pas davantage ici.

const FINE = " ";

let PARAMETRES = null;
let RESERVES = [];

// -- mise en forme -----------------------------------------------------------

function nombre(valeur, decimales = 0) {
  return valeur.toFixed(decimales)
    .replace(/\B(?=(\d{3})+(?!\d))/g, FINE)
    .replace(".", ",");
}

function euros(valeur) {
  return `${nombre(Math.round(valeur))}${FINE}€`;
}

function pourcentage(valeur, decimales = 1) {
  return `${nombre(valeur * 100, decimales)}${FINE}%`;
}

function echapper(texte) {
  return String(texte).replace(/[&<>"']/g, (caractere) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#x27;",
  }[caractere]));
}

// -- le calcul ---------------------------------------------------------------

/**
 * Les taxes payées sur l'énergie d'un an de conduite.
 *
 * L'accise s'applique au litre — ou au kilowattheure —, et la TVA s'applique
 * ensuite à un prix qui la comprend déjà : l'impôt est taxé, et ce détail vaut
 * plusieurs dizaines d'euros par an pour un automobiliste ordinaire.
 */
function taxesEnergie(saisie) {
  const p = PARAMETRES;
  const centaines = saisie.kilometres / 100;
  let accise = 0;
  if (saisie.motorisation === "gazole") {
    accise = centaines * p.conso_gazole_100km * p.ticpe_gazole_litre;
  } else if (saisie.motorisation === "essence") {
    accise = centaines * p.conso_essence_100km * p.ticpe_essence_litre;
  } else if (saisie.motorisation === "electrique") {
    accise = centaines * p.conso_electrique_100kwh * p.accise_electricite_kwh;
  }
  return accise * (1 + p.tva);
}

/** La part du coût d'un trajet en transport public que l'usager acquitte. */
function partUsager(reseau) {
  const p = PARAMETRES;
  if (reseau === "urbain") { return p.part_recettes_usagers_urbain; }
  if (reseau === "ter") { return p.part_recettes_usagers_ter; }
  return 0;
}

/**
 * Ce qui passe devant vous : ce que vous payez et que vous voyez passer.
 *
 * Les taxes sur le carburant y figurent bien qu'elles soient invisibles à la
 * pompe — le prix affiché ne les détaille pas. Elles sont ici parce que c'est
 * vous qui les versez, au centime près, au moment où vous faites le plein.
 */
function fluxVisibles(saisie) {
  const abonnement = saisie.abonnement * 12;
  const lignes = [
    ["Taxes sur l'énergie de vos trajets", taxesEnergie(saisie),
     "Accise sur le carburant ou l'électricité, et la TVA qui s'applique "
     + "par-dessus."],
    ["Péages", saisie.peages,
     "Ce que vous déclarez passer aux barrières, TVA comprise."],
    ["Abonnement de transport public", abonnement,
     "Ce que vous versez vous-même, douze fois par an."],
  ].filter(([, montant]) => montant > 0);
  const total = lignes.reduce((somme, [, montant]) => somme + montant, 0);
  return { lignes, total, abonnement };
}

/**
 * Ce que vos déplacements coûtent à d'autres que vous.
 *
 * UNE SEULE LIGNE, et c'est une correction. Ce simulateur en additionnait
 * trois — la subvention de vos trajets, votre part des concours publics et le
 * versement mobilité de votre employeur — alors que les deux dernières
 * FINANCENT la première. L'agrégat des concours publics comprend le versement
 * mobilité et les subventions d'exploitation des réseaux conventionnés : les
 * additionner comptait le même euro jusqu'à trois fois, et gonflait d'autant
 * le seul chiffre que cette page existe pour établir.
 *
 * Les deux ordres de grandeur collectifs n'ont pas disparu pour autant : ils
 * sont affichés à côté du calcul par `reperesCollectifs`, jamais dedans.
 */
function fluxInvisibles(saisie, abonnement) {
  const part = partUsager(saisie.reseau);
  const subvention = part > 0 ? abonnement * (1 / part - 1) : 0;
  const lignes = [
    ["Subvention de vos propres trajets", subvention,
     `Votre abonnement couvre ${pourcentage(part, 0)} du coût du service : la `
     + "collectivité verse le reste pour les trajets que vous faites, par le "
     + "versement mobilité et par le budget de votre région ou de votre "
     + "intercommunalité."],
  ].filter(([, montant]) => montant > 0);

  const total = lignes.reduce((somme, [, montant]) => somme + montant, 0);
  return { lignes, total, subvention, part };
}

/**
 * Deux ordres de grandeur collectifs, qui ne s'additionnent à rien.
 *
 * Ils RECOUVRENT en partie la subvention calculée plus haut : l'agrégat des
 * concours publics comprend le versement mobilité, lequel finance lui-même
 * une part des trajets conventionnés. Les montrer à côté du total, et non
 * dedans, est la seule façon honnête de les montrer — ils situent l'enjeu,
 * ils ne s'ajoutent pas à votre facture.
 */
function reperesCollectifs(saisie) {
  const p = PARAMETRES;
  return {
    concours: p.concours_publics_transports / p.population,
    versement: saisie.emploi === "salarie"
      ? p.versement_mobilite_total / p.actifs_occupes : 0,
  };
}

/**
 * Ce que la réforme changerait, et ce qu'elle ne changerait pas.
 *
 * La redevance d'usage remplace la taxe au litre à prélèvement constant : la
 * comparaison ci-dessous ne montre donc pas une économie, mais un ordre de
 * grandeur de la substitution pour un profil donné. Un automobiliste qui roule
 * peu y gagne, celui qui roule beaucoup y perd — c'est le principe même d'un
 * prix à l'usage, et le taire serait malhonnête.
 */
function substitution(saisie) {
  const p = PARAMETRES;
  const redevance = saisie.kilometres * p.redevance_usage_km;
  const taxes = taxesEnergie(saisie);
  return { redevance, taxes, ecart: redevance - taxes };
}

// -- rendu -------------------------------------------------------------------

function tableauLignes(lignes, total, intitule) {
  const corps = lignes.map(([libelle, montant, glose]) => `
    <tr><th scope="row">${echapper(libelle)}<span class="dont">${echapper(glose)}</span></th>
    <td class="nombre">${euros(montant)}</td>
    <td class="nombre">${euros(montant / 12)}</td></tr>`).join("");
  return `<div class="defilant"><table>
    <caption>${echapper(intitule)}</caption>
    <thead><tr><th scope="col">Ce qui est payé</th>
      <th scope="col" class="nombre">Par an</th>
      <th scope="col" class="nombre">Par mois</th></tr></thead>
    <tbody>${corps}
      <tr><th scope="row"><strong>Total</strong></th>
      <td class="nombre"><strong>${euros(total)}</strong></td>
      <td class="nombre"><strong>${euros(total / 12)}</strong></td></tr>
    </tbody></table></div>`;
}

function scenario(titre, categorie, total, largeur, classe, glose) {
  return `<div class="scenario">
  <div class="entete">
    <span class="titre">${echapper(titre)}</span>
    <span class="montant">
      <span class="chiffre principal">
        <span class="categorie">${echapper(categorie)}</span>
        <span class="somme">${euros(total)}</span>
        <span class="unite">par an</span>
      </span>
    </span>
  </div>
  <div class="barre ${classe}"><span style="width:${largeur.toFixed(1)}%"></span></div>
  <p class="glose">${glose}</p>
</div>`;
}

/**
 * La phrase que ce simulateur existe pour écrire.
 *
 * Elle dit que le total ne baisse pas, et que c'est sa VISIBILITÉ qui change.
 * Sans elle, deux barres de longueurs différentes se lisent comme une économie
 * — ce qu'elles ne sont pas.
 */
function avertissementTotal(visible, invisible) {
  const total = visible + invisible;
  if (invisible <= 0) {
    return `<div class="note resume">
  <p><strong>Vos trajets ne sont pas subventionnés, et c'est aussi un
  fait.</strong> Vous payez ${euros(visible)} par an, et aucune collectivité ne
  verse quoi que ce soit pour les déplacements que vous faites : la voiture n'a
  pas de subvention d'exploitation. Ce que ce programme change pour vous n'est
  donc pas le montant — c'est ce que cet argent finance, et le fait que rouler
  à l'heure et à l'endroit où cela coûte cher aux autres se paie enfin comme
  tel.</p>
</div>`;
  }
  return `<div class="note resume">
  <p><strong>Le total ne baisse pas : il se voit.</strong> Ce programme ne
  promet pas de vous prélever moins la première année — il promet que les
  ${euros(total)} que vos déplacements coûtent chaque année s'écrivent enfin :
  ${euros(visible)} que vous payez au guichet, ${euros(invisible)} que d'autres
  paient pour vos trajets. Un prélèvement qu'on ne voit pas n'est jamais
  discuté, et ce qui n'est jamais discuté ne s'améliore pas.</p>
</div>`;
}

/**
 * Les repères collectifs, avec la phrase qui interdit de les additionner.
 *
 * Elle est en gras et au-dessus des montants, et non en note : c'est
 * précisément la faute que cette page a commise, et un lecteur qui ne lit que
 * les chiffres doit buter sur l'avertissement avant de les lire.
 */
function reperes(valeurs) {
  const lignes = [
    ["Concours publics aux transports, par habitant", valeurs.concours,
     "Agrégat national reconstitué, rapporté à un habitant."],
    ["Versement mobilité, par actif occupé", valeurs.versement,
     "Payé par les employeurs, et compris dans l'agrégat ci-dessus."],
  ].filter(([, montant]) => montant > 0);
  if (!lignes.length) { return ""; }
  const corps = lignes.map(([libelle, montant, glose]) =>
    `<li><strong>${euros(montant)} par an</strong> — ${echapper(libelle)}.
     <span class="discret">${echapper(glose)}</span></li>`).join("");
  return `<div class="note">
  <div>
  <p><strong>Deux repères, qui ne s'ajoutent pas au calcul ci-dessus.</strong>
  Le total des concours publics comprend le versement mobilité et les
  subventions qui paient vos propres trajets : l'ajouter à ceux-ci compterait
  le même euro deux ou trois fois. Cette page l'a fait jusqu'en septembre 2026
  et ne le fait plus.</p>
  <ul class="serree">${corps}</ul>
  </div>
</div>`;
}

function rendre(saisie) {
  const visibles = fluxVisibles(saisie);
  const invisibles = fluxInvisibles(saisie, visibles.abonnement);
  const bascule = substitution(saisie);
  const collectifs = reperesCollectifs(saisie);
  const total = visibles.total + invisibles.total;
  const echelle = Math.max(visibles.total, invisibles.total, 1);

  // Les deux barres se lisent sur la MÊME échelle, celle du plus grand des
  // deux totaux : deux barres rapportées chacune à leur propre maximum ne se
  // comparent pas, et c'est la comparaison qui est ici tout le propos.
  const partVisible = (visibles.total / echelle) * 100;
  const partInvisible = (invisibles.total / echelle) * 100;

  const reserves = RESERVES.map(({ parametre, texte }) =>
    `<li><strong>${echapper(parametre)}</strong> — ${echapper(texte)}</li>`).join("");

  // Le cas du véhicule électrique ne peut PAS être servi par la phrase
  // générale. La redevance étant calibrée sur un véhicule thermique moyen,
  // elle multiplie par plus de six ce qu'un véhicule électrique acquitte,
  // et un résultat pareil sans explication est une capture d'écran que nos
  // adversaires feront à notre place. Nous l'affichons, et nous le motivons.
  let gloseBascule;
  if (bascule.taxes <= 0) {
    gloseBascule = `Sans véhicule, la substitution de la redevance d'usage à la
       taxe sur les carburants ne change rien pour vous — sinon que le
       financement des routes cesserait de dépendre d'une taxe qui s'éteint
       avec le moteur thermique.`;
  } else if (saisie.motorisation === "electrique") {
    gloseBascule = `À l'usage, vos kilomètres coûteraient
       <strong>${euros(bascule.redevance)} par an</strong> de redevance, contre
       <strong>${euros(bascule.taxes)}</strong> d'accise sur l'électricité
       aujourd'hui. L'écart est considérable, et nous préférons l'afficher que
       le laisser découvrir : un véhicule électrique use la chaussée comme un
       autre et ne paie presque rien pour elle, parce qu'une taxe au litre ne
       sait taxer qu'un litre. C'est l'angle mort qui condamne le financement
       actuel — et c'est aussi une hausse brutale pour qui a acheté son
       véhicule sous un autre régime fiscal. C'est pourquoi le programme
       propose une entrée progressive sur la durée d'un mandat, et non le
       tarif plein dès la première année.`;
  } else {
    gloseBascule = `À l'usage, vos kilomètres coûteraient
       <strong>${euros(bascule.redevance)} par an</strong> de redevance, contre
       <strong>${euros(bascule.taxes)}</strong> de taxes sur l'énergie
       aujourd'hui, soit
       ${bascule.ecart >= 0 ? "environ " + euros(bascule.ecart) + " de plus"
                            : "environ " + euros(-bascule.ecart) + " de moins"}.
       La bascule se fait à prélèvement constant POUR L'ÉTAT, pas pour chaque
       conducteur : rouler peu coûte moins, rouler beaucoup coûte plus.`;
  }

  return `
<h2>Ce que vos déplacements coûtent</h2>
${scenario("Ce que vous payez au guichet", "payé directement", visibles.total,
    partVisible, "actuel",
    `Taxes sur l'énergie, péages et abonnement : `
    + `${euros(visibles.total / 12)} par mois, que vous versez vous-même.`)}
${scenario("Ce que d'autres paient pour vos trajets", "payé par la collectivité",
    invisibles.total, partInvisible, "liberal",
    invisibles.total > 0
      ? `La subvention de vos propres déplacements : `
        + `${pourcentage(invisibles.total / (total || 1), 0)} de ce qu'ils `
        + `coûtent au total, et aucun document ne vous en informe.`
      : `Aucune : la voiture ne reçoit pas de subvention d'exploitation. `
        + `Ce que vous payez, vous le payez en entier.`)}

${avertissementTotal(visibles.total, invisibles.total)}

<div class="paire">
  <div>${tableauLignes(visibles.lignes, visibles.total,
    "Ce qui passe par vous")}</div>
  <div>${invisibles.lignes.length
    ? tableauLignes(invisibles.lignes, invisibles.total, "Ce qui passe ailleurs")
    : ""}</div>
</div>

${reperes(collectifs)}

<div class="note">
  <div>
  <p><strong>Et avec la redevance d'usage ?</strong> ${gloseBascule}</p>
  </div>
</div>

<div class="note avertissement">
  <div>
  <p><strong>Ce calcul illustre des ordres de grandeur, il ne prédit rien.</strong>
  Les tarifs employés sont publics ; les parts, les moyennes et l'agrégat des
  concours publics ne le sont pas au même titre. Les voici :</p>
  <ul class="serree">${reserves}</ul>
  <p class="discret"><a href="donnees.html#simulateur">Toutes les hypothèses,
  avec leurs sources</a> · <a href="reforme.html#financement">ce que nous ne
  pouvons pas chiffrer</a></p>
  </div>
</div>`;
}

// -- démarrage ---------------------------------------------------------------

function lireSaisie(formulaire) {
  const valeur = (nom) => formulaire.elements[nom].value;
  return {
    motorisation: valeur("motorisation"),
    kilometres: Math.max(0, Number(valeur("kilometres")) || 0),
    peages: Math.max(0, Number(valeur("peages")) || 0),
    reseau: valeur("reseau"),
    abonnement: Math.max(0, Number(valeur("abonnement")) || 0),
    emploi: valeur("emploi"),
  };
}

async function demarrer() {
  const formulaire = document.getElementById("formulaire");
  const sortie = document.getElementById("resultat");
  if (!formulaire || !sortie) { return; }

  try {
    const reponse = await fetch("moteur/donnees.json", { cache: "force-cache" });
    if (!reponse.ok) { throw new Error(`donnees.json (${reponse.status})`); }
    const paquet = await reponse.json();
    PARAMETRES = paquet.parametres;
    RESERVES = paquet.reserves || [];
  } catch (erreur) {
    sortie.innerHTML = '<div class="erreur">Les paramètres du simulateur '
      + "n'ont pas pu être chargés. Le détail du calcul et toutes ses "
      + 'hypothèses restent lisibles sur la page <a href="donnees.html#simulateur">'
      + "Données et sources</a>.</div>";
    return;
  }

  const calculer = (evenement) => {
    if (evenement) { evenement.preventDefault(); }
    sortie.innerHTML = rendre(lireSaisie(formulaire));
  };

  // Le bouton n'est PAS un bouton de soumission, et le formulaire n'a ni
  // méthode ni adresse d'envoi. C'est voulu : tant que le formulaire était en
  // `method="get"`, un script non chargé suffisait à ce qu'un clic envoie le
  // kilométrage et l'abonnement dans l'URL — donc au serveur, qui les
  // journalise. La page promet l'inverse, et une promesse qui ne tient que
  // si le JavaScript se charge n'est pas une promesse.
  const bouton = document.getElementById("calculer");
  if (bouton) { bouton.addEventListener("click", calculer); }
  // Ceinture : un navigateur peut tenter une soumission implicite (touche
  // Entrée). Sans action ni méthode elle ne sortirait pas de la page, mais
  // autant l'arrêter avant.
  formulaire.addEventListener("submit", calculer);
  // Le résultat suit la saisie : recalculer à chaque changement évite d'avoir
  // à valider pour voir l'effet d'un kilométrage ou d'un choix de réseau, qui
  // est justement ce que cette page veut faire éprouver.
  formulaire.addEventListener("change", calculer);
  calculer(null);
}

demarrer();
