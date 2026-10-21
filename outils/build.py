#!/usr/bin/env python3
"""Génère les pages HTML du site ALTP (maquette). Usage : python3 outils/build.py"""
import os
BASE="https://webaunet.github.io/altp/"
TEL="07 86 53 70 64"; TELL="+33786537064"; MAIL="contact@altp-france.com"
ADR="17 Rue de la Gaudrée, 91410 Dourdan"
PAGES=[("index.html","Accueil"),("prestations.html","Prestations"),("contact.html","Contact")]

def head(title,desc):
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="images/favicon.png">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;600;800&family=Archivo+Black&display=swap">
<link rel="stylesheet" href="style.css">
</head>
<body>
'''
def header(cur):
    li="".join(f'<li><a href="{h}"'+(' aria-current="page"' if h==cur else '')+f'>{n}</a></li>' for h,n in PAGES)
    return f'''<header>
  <div class="w bar">
    <a class="logo" href="{BASE}" aria-label="ALTP, retour à l'accueil"><img src="images/logo.png" width="845" height="260" alt="ALTP Landscape Terrassement"></a>
    <nav id="menu" aria-label="Navigation principale"><ul>{li}</ul></nav>
    <a class="btn tel" href="tel:{TELL}" aria-label="Appeler le {TEL}">&#9990;<span class="num">&nbsp;{TEL}</span></a>
    <button class="burger" id="burger" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="menu"><span></span></button>
  </div>
</header>
'''
FOOT=f'''<footer>
  <div class="w">
    <span>ALTP · {ADR} · {TEL}</span>
    <span><a href="index.html">Accueil</a> · <a href="prestations.html">Prestations</a> · <a href="contact.html">Contact</a> · <a href="mentions-legales.html">Mentions légales</a></span>
  </div>
</footer>
<script src="script.js"></script>
</body>
</html>
'''
def page(fn,title,desc,cur,body):
    open(fn,"w",encoding="utf-8").write(head(title,desc)+header(cur)+"<main>\n"+body+"\n</main>\n"+FOOT)

def card(img,w,h,alt,t,p):
    return f'<article class="card"><img loading="lazy" src="images/{img}" width="{w}" height="{h}" alt="{alt}"><div><h3>{t}</h3><p>{p}</p></div></article>'
def coord():
    return f'''<address class="coord">
        <div><small>Téléphone</small><a href="tel:{TELL}">{TEL}</a></div>
        <div><small>E-mail</small><a href="mailto:{MAIL}">{MAIL}</a></div>
        <div><small>Adresse</small>17 Rue de la Gaudrée<br>91410 Dourdan</div>
      </address>'''

# ---------- ACCUEIL ----------
home=f'''  <section class="hero">
    <img src="images/maconnerie.jpg" width="1408" height="768" alt="Paysagiste en train de monter un muret en pierre dans un jardin avec escalier et massifs">
    <div class="w">
      <span class="eyebrow">Aménagement paysager et terrassement · Dourdan (91)</span>
      <h1>Votre jardin, travaillé avec précision.</h1>
      <p>ALTP aménage, terrasse et entretient les jardins de Dourdan et de ses environs : de la préparation du terrain à la finition des allées, terrasses et massifs.</p>
      <div class="cta"><a class="btn" href="contact.html">Demander un devis</a><a class="btn ghost" href="prestations.html">Voir les prestations</a></div>
    </div>
  </section>
  <div class="hero-curve" aria-hidden="true"></div>
  <section class="band terre" id="amenager" style="padding-top:56px"><div class="w">
    <div class="head"><span class="eyebrow">Aménager</span><h2>Du terrain nu au jardin fini</h2><p>Terrassement, maçonnerie paysagère, terrasses, allées et espaces verts : on prépare le sol, puis on construit ce qui fera la vie de votre extérieur.</p></div>
    <div class="grid">
      {card("terrassement.jpg",1376,768,"Ouvrier qui terrasse un jardin avec une pelle et une brouette devant une maison","Terrassement","Décaissement, remblai et nivellement du terrain avant toute création.")}
      {card("terrasse-bois.jpg",1408,768,"Pose d'une terrasse en bois devant une maison en pierre","Terrasses","Terrasse en bois ou dallage, posée de niveau et pensée pour durer.")}
      {card("allee-paves.jpg",1408,768,"Allée en pavés bordée d'un muret de pierre et de massifs","Allées et pavés","Allées dallées ou pavées, accès et cheminements dans le jardin.")}
      {card("espace-vert.jpg",1408,768,"Création d'un massif et d'une pelouse aux courbes douces devant une maison moderne","Espaces verts","Massifs, pelouse et plantations dessinés pour votre terrain.")}
    </div></div></section>
  <section class="band sombre" id="entretenir"><div class="w">
    <div class="head"><span class="eyebrow">Entretenir</span><h2>Un jardin soigné, saison après saison</h2><p>Tonte, taille, élagage et évacuation des déchets verts : l'entretien qui garde vos aménagements nets.</p></div>
    <div class="grid">
      {card("tonte.jpg",1376,768,"Jardinier qui tond une pelouse près d'une maison aux volets bleus","Tonte","Pelouse tondue régulièrement, bordures reprises.")}
      {card("taille-haies.jpg",1200,896,"Jardinier équipé d'un casque anti-bruit qui taille une haie","Taille de haies","Haies et arbustes taillés proprement, déchets évacués.")}
      {card("elagage.jpg",1376,768,"Élagueur encordé dans un grand arbre avec une tronçonneuse","Élagage","Taille et abattage d'arbres, en sécurité, près des habitations.")}
      {card("dechets-verts.jpg",1408,768,"Jardinier chargeant des déchets verts sur une remorque","Déchets verts","Branches et tontes chargées et évacuées après le chantier.")}
    </div></div></section>
  <section class="band sec-approche" id="approche"><div class="w approche">
    <img loading="lazy" src="images/conception.jpg" width="1408" height="768" alt="Plan de jardin affiché sur une tablette, discuté autour d'une table de jardin">
    <div><span class="eyebrow">Notre approche</span><h2 style="margin-top:12px">Un projet cadré avant le premier coup de pelle</h2>
      <ol class="etapes">
        <li><b>1</b><div><strong>On écoute</strong><p>Vous décrivez votre terrain, vos usages et votre budget.</p></div></li>
        <li><b>2</b><div><strong>On conçoit</strong><p>Le projet est dessiné et expliqué avant de démarrer.</p></div></li>
        <li><b>3</b><div><strong>On réalise</strong><p>Terrassement, construction et plantations, puis entretien si vous le souhaitez.</p></div></li>
      </ol></div></div></section>
  <section class="contact"><div class="w box">
    <div><span class="eyebrow" style="color:#a8d160">Contact</span><h2 style="margin-top:12px">Parlons de votre jardin</h2><p>Décrivez votre projet par téléphone ou par e-mail. Nous revenons vers vous pour en discuter.</p>
      <div class="cta" style="margin-top:24px"><a class="btn" href="contact.html" style="background:#fff;color:var(--noir);border-color:#fff">Nous écrire</a></div></div>
    {coord()}</div></section>'''
page("index.html","ALTP Dourdan | Aménagement paysager et terrassement","ALTP, aménagement paysager, terrassement et entretien de jardins à Dourdan (91). Terrasses, allées, plantations, tonte, taille et élagage.","index.html",home)

# ---------- PRESTATIONS ----------
prest=f'''  <section class="ph"><div class="w">
    <div><span class="eyebrow">Nos prestations</span><h1>Deux façons de prendre soin de votre extérieur</h1>
      <p>Créer ou transformer un espace, ou le garder en forme toute l'année : choisissez par où commencer.</p>
      <div class="cta" style="margin-top:28px"><a class="btn" href="#amenager">Aménager</a><a class="btn ghost" href="#entretenir">Entretenir</a></div></div>
    <div class="mosaic">
      <img src="images/nivellement.jpg" width="1400" height="764" alt="Jardinier qui ratisse et nivelle une terre fraîchement travaillée">
      <img src="images/plantation.jpg" width="1400" height="764" alt="Jardinier qui plante des vivaces dans un massif">
      <img src="images/dessouchage.jpg" width="1408" height="768" alt="Souche d'arbre et broyeur de souches dans un jardin">
    </div></div></section>
  <section class="band terre" id="amenager"><div class="w detail">
    <div><span class="eyebrow">Aménager</span><h2 style="margin-top:12px">Préparer, construire, planter</h2>
      <ul class="liste">
        <li><strong>Terrassement et nivellement.</strong> Reprise du terrain, décaissement, remblai, mise à niveau avant les travaux.</li>
        <li><strong>Dessouchage.</strong> Retrait des souches pour libérer l'espace à aménager.</li>
        <li><strong>Terrasses, allées et dallages.</strong> Bois, dalles ou pavés selon l'usage et le style de la maison.</li>
        <li><strong>Maçonnerie paysagère.</strong> Murets, marches et soutènements en pierre.</li>
        <li><strong>Plantations et création d'espaces verts.</strong> Massifs, arbustes et pelouse.</li>
      </ul></div>
    <img loading="lazy" src="images/allee-dallee.jpg" width="1408" height="768" alt="Chantier d'une allée dallée devant une maison en pierre, éclairée en soirée"></div></section>
  <section class="band sombre" id="entretenir"><div class="w detail rev">
    <div><span class="eyebrow">Entretenir</span><h2 style="margin-top:12px">Un entretien régulier, un jardin net</h2>
      <ul class="liste">
        <li><strong>Tonte et entretien général.</strong> Pelouse, bordures et espaces verts remis en ordre.</li>
        <li><strong>Taille de haies et d'arbustes.</strong> Taille propre, coupes ramassées.</li>
        <li><strong>Élagage.</strong> Taille et abattage d'arbres.</li>
        <li><strong>Évacuation des déchets verts.</strong> Chargés et emportés après intervention.</li>
      </ul></div>
    <img loading="lazy" src="images/entretien.jpg" width="1408" height="768" alt="Jardin entretenu avec pelouse tondue, massifs fleuris et allée gravillonnée"></div></section>
  <section class="contact"><div class="w box">
    <div><span class="eyebrow" style="color:#a8d160">Un projet précis ?</span><h2 style="margin-top:12px">Décrivez-nous votre terrain</h2><p>Surface, contraintes, travaux souhaités : quelques lignes suffisent pour démarrer la discussion.</p>
      <div class="cta" style="margin-top:24px"><a class="btn" href="contact.html" style="background:#fff;color:var(--noir);border-color:#fff">Demander un devis</a></div></div>
    <img src="images/robot-tonte.jpg" loading="lazy" width="1408" height="768" alt="Jardin avec muret en pierre, massifs et robot de tonte sur la pelouse" style="border-radius:6px;aspect-ratio:3/2;object-fit:cover;width:100%"></div></section>'''
page("prestations.html","Prestations | ALTP Dourdan","Terrassement, terrasses, allées, plantations, tonte, taille de haies et élagage : les prestations d'ALTP à Dourdan (91).","prestations.html",prest)

# ---------- CONTACT ----------
cont=f'''  <section class="ph vert"><div class="w">
    <div><span class="eyebrow">Contact</span><h1>Un projet de jardin à Dourdan ?</h1>
      <p>Appelez-nous ou remplissez le formulaire : vous obtenez un message prêt à envoyer par SMS ou par e-mail.</p>
      <a class="bigtel" href="tel:{TELL}">{TEL}</a></div>
    <img src="images/entretien.jpg" width="1408" height="768" alt="Jardin entretenu avec pelouse tondue, massifs fleuris et allée gravillonnée" style="border-radius:6px;aspect-ratio:3/2;object-fit:cover;width:100%"></div></section>
  <section class="band court terre"><div class="w formgrid">
    <div><h2 style="margin-bottom:24px">Décrivez votre demande</h2>
      <form id="form" class="fcard" novalidate>
        <p class="fintro">Les champs sont tous obligatoires.</p>
        <div class="row">
        <label for="nom">Nom et prénom<input id="nom" name="nom" autocomplete="name" required aria-describedby="e-nom"><span class="err" id="e-nom" role="alert"></span></label>
        <label for="tel">Téléphone<input id="tel" name="tel" type="tel" autocomplete="tel" inputmode="tel" required aria-describedby="e-tel"><span class="err" id="e-tel" role="alert"></span></label>
        </div>
        <div class="row">
        <label for="mail">E-mail<input id="mail" name="mail" type="email" autocomplete="email" required aria-describedby="e-mail"><span class="err" id="e-mail" role="alert"></span></label>
        <label for="type">Type de travaux<select id="type" name="type" required aria-describedby="e-type"><option value="">Choisir…</option><option>Terrassement</option><option>Terrasse ou allée</option><option>Maçonnerie paysagère</option><option>Plantations, espaces verts</option><option>Entretien (tonte, taille, élagage)</option><option>Autre</option></select><span class="err" id="e-type" role="alert"></span></label>
        </div>
        <label for="msg">Votre projet<textarea id="msg" name="msg" required aria-describedby="e-msg"></textarea><span class="err" id="e-msg" role="alert"></span></label>
        <button class="btn big" type="submit">Préparer ma demande</button>
      </form></div>
    <div>
      <div class="recap" id="recap" hidden aria-live="polite">
        <h3>Votre demande est prête</h3>
        <pre id="recap-txt"></pre>
        <div class="actions">
          <a class="btn" id="b-sms" href="#">Envoyer par SMS</a>
          <a class="btn ghost" id="b-mail" href="#">Envoyer par e-mail</a>
          <button class="btn ghost" type="button" id="b-copy">Copier</button>
          <a class="btn ghost" href="tel:{TELL}">Appeler</a>
        </div>
        <div class="ok" id="ok" role="status"></div>
      </div>
      <div id="avant" class="head" style="margin:0 0 24px"><span class="eyebrow">Comment ça marche</span><p>Ce site est une maquette : le formulaire ne s'envoie pas tout seul. Une fois rempli, il prépare votre message, que vous envoyez d'un clic par SMS ou par e-mail, ou que vous copiez.</p></div>
      {coord()}
    </div></div></section>'''
page("contact.html","Contact | ALTP Dourdan","Contactez ALTP à Dourdan (91) pour un projet d'aménagement paysager, de terrassement ou d'entretien de jardin : téléphone, e-mail, formulaire.","contact.html",cont)

# ---------- MENTIONS LÉGALES ----------
leg=f'''  <section class="band court" style="padding-top:64px"><div class="w legal">
    <span class="eyebrow">Informations légales</span><h1 style="margin-top:12px">Mentions légales</h1>
    <h2>Éditeur du site</h2>
    <p>ALTP (Aménagement Landscape Terrassement Précision)<br>SIREN : 989049796<br>Adresse : {ADR}<br>Téléphone : {TEL}<br>E-mail : <a href="mailto:{MAIL}">{MAIL}</a><br>Dirigeant au registre : Antonin Torillec</p>
    <h2>Hébergement de la maquette</h2>
    <p>GitHub Pages (GitHub, Inc.).</p>
    <h2>Informations à compléter</h2>
    <p class="manque">Forme juridique, capital social, numéro de TVA, directeur de la publication et hébergeur définitif du futur site : non vérifiés à ce jour, à fournir par l'entreprise.</p>
    <h2>Maquette</h2>
    <p>Ce site est une maquette de démonstration présentée à l'entreprise. Les images sont illustratives et ne représentent pas des réalisations d'ALTP.</p>
  </div></section>'''
page("mentions-legales.html","Mentions légales | ALTP Dourdan","Mentions légales du site d'ALTP, aménagement paysager et terrassement à Dourdan (91).","",leg)
print("ok")
