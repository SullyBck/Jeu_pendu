from javax.swing import JOptionPane
import time
import random

def setup():
    size(700,500)
    frameRate(60)
    background(225, 225, 225)
    
    # lettres valides, selon la difficulté
    lows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    caps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    accents = [u'ç', u'à', u'á', u'â', u'ã', u'ä', u'å', u'è', u'é', u'ê', u'ë', u'ì', u'í', u'î', u'ï', u'ò', u'ó', u'ô', u'õ', u'ö', u'ù', u'ú', u'û', u'ü', u'ý', u'ÿ', u'ñ']
    numbs = [' ', '-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    global lettres_easy
    global lettres_hard
    lettres_easy = lows + caps + accents
    lettres_hard = lettres_easy + numbs
    
    newStart() # permet de ré-exécuter le start, afin de rejouer
    
def draw():
    tac() 
    compteur() 
    printlettres() 
    bouton() 
    if trouve == 1 :
        win() 
    if trouve == 2 :
        lose()
    printmot(avancee_mot)
    pendu(chances)
    
    
def newStart():
    # nouvelle partie
    global trouve 
    trouve = 0 
    # 0 = pas trouvé 
    # 1 = trouvé (gagné)
    # 2 = perdu (pas trouvé)
    
    global lettres_fausses
    global lettres_testees
    global mots_testes
    lettres_fausses = ""
    lettres_testees = []
    mots_testes = []
    
    chances_initiales()
    difficulty()
    tirage()
    tic()
    
def chances_initiales():
    # nombre de chances au début du jeu
    global ch_initiales
    global chances
    ch_initiales = " "
    while ch_initiales==None or not ch_initiales.isdigit() :
        ch_initiales = JOptionPane.showInputDialog(frame, u"Nombre de chances ? (De 1 à 11)", u"Choix chances", JOptionPane.QUESTION_MESSAGE)
    ch_initiales = int(ch_initiales)
    if ch_initiales > 11 or ch_initiales < 1 :
        ch_initiales = 11
    chances = ch_initiales
    p = str(ch_initiales) + " chances"
    print (p)
    
def difficulty():
    # choix "difficulté" mot tiré
    global hard
    hard = False
    difficult = "false"
    while difficult != None and len(difficult)>0  :
        difficult = JOptionPane.showInputDialog(frame, u"Normal (OK) ou Difficile (Annuler) ?", u"Choix difficulté du mot", JOptionPane.QUESTION_MESSAGE)
    if difficult == None :
        hard = True
        print ("hard")
    else :
        print ("easy")    
        
def tirage():
    # choix du mot parmi les listes
    global mot
    mots_easy = ["JAVA", "PROCESSING", "VARIABLE", "INFORMATIQUE", "ORDINATEUR", "FICHIER", "ERREUR", "python", "windows", "CLAVIER",  "PROGRAMME", "PRISE", "DOSSIER", "SCRATCH", "PENDU", "BINAIRE", "FONCTION", "SOURIS"]
    mots_hard = ["anticonstitution", u"rançongiciel", u"html5", u"css3", "clef-usb", "wi-fi", "arc-en-ciel", "Pop-up", u"NUMÉRIQUE", u"DÉBOGAGE", u"anticrénelage", u"bibliothèque", u"émulateur"]
    if hard :
        mot = random.choice(mots_hard)
    else :
        mot = random.choice(mots_easy)
    mot = mot.lower()
    print (mot) # à mettre en commentaire pour jouer
    
    # mot affiché (au début)
    global avancee_mot 
    avancee_mot = "_" * len(mot)
    
    #pour afficher les tirets "-" dès le début ("clef-usb")
    d = 0
    for c in mot :
        if c == "-" :
            f = d + 1
            avancee_mot = avancee_mot[:d] + "-" + avancee_mot[f:]
        d = d + 1
    
def tic():
    # début du temps
    global start_time 
    start_time = time.time()
    

def tac():
    # défilement du temps
    global comp
    global comp_final
    if trouve == 0 :
        t_sec = round(time.time() - start_time)
        (t_min, t_sec) = divmod(t_sec,60)
        t_sec = int(t_sec)
        t_min = int(t_min)
        comp = '{:02}:{:02}'.format(t_min,t_sec)
    else :
        # arrêt du timer
        comp_final = u"temps écoulé :\n" + comp
    
def compteur():
    # affichage du timer
    stroke(225,225,225)
    fill(225, 225, 225)
    rect(400,190,400,100)
    fill(20,60,90,250)
    textSize(30)
    textMode(SHAPE)
    textAlign(CENTER, TOP);
    line(0,120,width, 120, 0, 0);
    if trouve == 0 :
        text(comp, 550,200)
    else :
        text(comp_final, 550, 200)
    
def printlettres():
    # fond
    stroke(225,225,225)
    fill(225, 225, 225)
    rect(300,350,400,50)
    # afficher les lettres fausses déjà essayées (en bas)
    textSize(30)
    fill(216, 24, 50)
    text(lettres_fausses, 530, 350)
    
def bouton():
    # rectangle bouton
    stroke(255,255,255)
    fill(200, 200, 200)
    rect(475,420,200,60)
    # texte, qui change d'apparence
    textSize(50)
    fill(107,142,35)
    if chances < 6 :
        fill(216, 24, 50)
    if trouve == 0 :
        text("deviner",575,420)
    elif trouve == 1 :
        fill(107,142,35)
        text("rejouer",575,420)
    elif trouve == 2 :
        fill(216, 24, 50)
        text("rejouer",575,420)

def mousePressed():
     # intéractions bouton deviner et rejouer
    if (mouseX > 475) and (mouseX < 675) and (mouseY >420) and (mouseY<480):
        if trouve != 0 :
            newStart()
            stroke(225,225,225)
            fill(225, 225, 225)
            rect(0,0,700,500)
        else :
            deviner()
    
def keyPressed():
    # touches tapées
    if hard and key in lettres_hard and key != ' ' and key != '-' :
        correspondance_lettre(key)
    elif hard and (key == ' ' or key == '-') and '-' in mot :
        correspondance_lettre(key)   
    elif not hard and key in lettres_easy :
        correspondance_lettre(key)
    else :
        print(u"tapez un caractère valide")
    
def deviner():
    # différentes boites de dialogue en fonction de la situation
    proposition = JOptionPane.showInputDialog(frame, u"Entrez une lettre ou un mot", u"Proposition", JOptionPane.QUESTION_MESSAGE)
    
    while (not prop_valid(proposition)) or (noaccent(proposition) in mots_testes) or (noaccent(proposition) in lettres_testees) :
        if not prop_valid(proposition) :
            proposition = JOptionPane.showInputDialog(frame, u"Entrez une LETTRE ou un MOT", u"Caractère(s) invalide(s)", JOptionPane.QUESTION_MESSAGE)
        elif noaccent(proposition) in mots_testes :
            proposition = JOptionPane.showInputDialog(frame, u"Entrez un NOUVEAU mot (ou une lettre)", u"Vous avez déjà essayé ce mot", JOptionPane.QUESTION_MESSAGE)
        elif noaccent(proposition) in lettres_testees :
            proposition = JOptionPane.showInputDialog(frame, u"Entrez une NOUVELLE lettre (ou un mot)", u"Vous avez déjà essayé cette lettre", JOptionPane.QUESTION_MESSAGE)
    
    # si l'utilisateur n'a pas RIEN tapé, ni cliqué CANCEL ou CROIX (auquel cas la boite de dialogue se ferme)
    if proposition != None :
        if len(proposition) == 1 :
            correspondance_lettre(proposition)
        elif len(proposition) > 1 :
            correspondance_mot(proposition)

def prop_valid(prop):
    # pour vérifier que l'utilisateur rentre des caractères valides, ou rien
    if prop != None :
        for c in prop :
            if (c == '-' or c == ' ') and not '-' in mot :
                return False
            elif hard and (not c in lettres_hard) :
                return False
            elif not hard and (not c in lettres_easy) :
                return False
        return True
    else :
        return True
    
def noaccent(txt):
    # retourne l'argument sans accent
    if txt != None and len(txt) > 0:
        txt = re.sub(u"[àáâãäå]", 'a', txt)
        txt = re.sub(u"[èéêë]", 'e', txt)
        txt = re.sub(u"[ìíîï]", 'i', txt)
        txt = re.sub(u"[òóôõö]", 'o', txt)
        txt = re.sub(u"[ùúûü]", 'u', txt)
        txt = re.sub(u"[ýÿ]", 'y', txt)
        txt = re.sub(u"[ñ]", 'n', txt)
        txt = re.sub(u"[ç]", 'c', txt)
        txt = re.sub(u"[ ]", '-', txt)
        return txt
    else :
        return False

def correspondance_lettre(prop_lettre):
    global chances
    global avancee_mot
    global trouve
    global lettres_fausses
    global lettres_testees
    
    prop_lettre = prop_lettre.lower()
    prop_lettre = noaccent(prop_lettre)
    
    if prop_lettre in noaccent(avancee_mot) :
        p = prop_lettre + u" est déjà dans le mot"
        
    elif prop_lettre in lettres_testees :
        p = prop_lettre + u" déjà essayé"
              
    elif prop_lettre in mot :
        p = prop_lettre + " est dans le mot"
        # pour remplacer le "_" par la bonne lettre
        d = 0
        for c in noaccent(mot) :
            f = d + 1
            if c == prop_lettre :
                avancee_mot = avancee_mot[:d] + mot[d:f] + avancee_mot[f:]
            d = d + 1 
        # pour que "avancee_mot" ne se superpose pas sur la fenêtre
        stroke(225,225,225)
        fill(225,225,225)
        rect(0,0,700,90) 
        
        if "_" not in avancee_mot :
            trouve = 1
                
    else :
        p = prop_lettre + " n'est pas dans le mot"
        chances = chances - 1
        lettres_testees.append(prop_lettre)
        lettres_fausses = lettres_fausses + " " + prop_lettre
        
        if chances == 0 :
            trouve = 2
                
    print(p)
    
    
def correspondance_mot(prop_mot):
    global chances
    global trouve
    global mots_testes
    
    prop_mot = prop_mot.lower()
    prop_mot = noaccent(prop_mot)
    
    if prop_mot == noaccent(mot) :
        p = "bravo"
        trouve = 1
        
    else :
        p = prop_mot + " n'est pas le bon mot"
        chances = chances - 1 
        mots_testes.append(prop_mot)
        
        if chances == 0 :
            trouve = 2  
              
    print(p)
                         
def win():
    erreurs = ch_initiales - chances
    textAlign(CENTER, TOP);
    textSize(30)
    fill(107,142,35)
    line(0, 120, width, 120, 0, 0)
    
    # texte à afficher, qui s'adapte en fonction des valeurs
    if erreurs == 1 :
        ligne1 = u"Gagné avec " + str(erreurs) + " seule erreur, bravo"
    elif erreurs == 0 :
        ligne1 = u"Gagné avec aucune erreur, bravo"
    else :
        ligne1 = u"Gagné avec " + str(erreurs) + " erreurs, bravo"
        
    if chances == 1 :
        ligne2 = "il vous restait " + str(chances) + " chance"
    else :
        ligne2 = "il vous restait " + str(chances) + " chances"
        
    text(ligne1, 350, 70);
    text(ligne2, 350, 105);
    
def lose():
    textAlign(CENTER, TOP);
    textSize(40)
    fill(216, 24, 50)
    line(0, 120, width, 120, 0, 0);
    perdu = u"Perdu ! le mot était " + mot
    text (perdu, 350, 70)

def printmot(avancee_mot):
    #affichage du mot à trouver ("_" et lettres)
    textSize(60)
    
    if chances > 5 :
        fill(107,142,35) # mot vert
    else :
        fill(216, 24, 50) # mot rouge

    if trouve == 1 : # si gagné
        stroke(225,225,225) # fond
        fill(225,225,225)
        rect(0,0,700,70) 
        fill(107,142,35) # mot vert
        avancee_mot = mot
        
    textAlign(CENTER, BOTTOM);
    line(0, 120, width, 120, 0, 0);
    text(avancee_mot, 350, 70);

def pendu(chances):
    #affichage du pendu, évolutif selon le nb de chances restantes
    stroke(255, 255, 255)
    if chances < 11 :
        fill(150, 150, 150)
        rect(50,450,275, 25) # 1ère barre
    if chances < 10 :
        rect(75,150,25, 300) # 2ème barre
    if chances < 9 :
        rect(75,150,200, 25) # 3ème barre
    if chances < 8 :
        stroke(255,255,255,0)
        rotate(radians(45)) 
        rect(220, -5, 15, 100) # 4ème barre
        rotate(radians(-45)) 
    if chances < 7 :
        stroke(255,255,255)
        rect(230,175,10, 35) # corde
        
    if trouve != 1 :
        fill(216, 24, 50) # perso rouge
    if trouve == 1 :
        fill(107,142,35) # perso vert
        
    if chances < 6 :
        stroke(255,255,255,0)
        ellipse(235,230,40, 40) #tête
    if chances < 5 :
        rect(230,250,10, 90) # corps
    if chances < 4 :
        rotate(radians(165)) 
        rect(-147, -460, 10, 80) # jambe droite
        rotate(radians(-165)) 
    if chances < 3 :
        rotate(radians(15)) 
        rect(307, 257, 10, 80) # jambe gauche
        rotate(radians(-15))
    if chances < 2 :
        rotate(radians(30)) 
        rect(330, 110, 8, 60) # bras gauche
        rotate(radians(-30)) 
    if chances < 1 :
        rotate(radians(-30)) 
        rect(70, 345, 8, 60) # bras droit
        rotate(radians(30)) 
