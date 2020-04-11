/*Récupérer le genre pour le choix du perso*/
var sexe;
var genre;

function choixSexe(){
    let choix = document.getElementById("menu");
    sexe = choix.value;
    afficheliste(sexe);
}

function afficheliste(s){
    if (s == "H"){
        genre = "homme";
    }
    if (s == "F"){
        genre = "femme";
    }
    if (s == "A"){
        genre = "autre";
    }
    let liste = document.getElementById(genre);
    liste.style.visibility='visible'; 
}

/*Placer l'image d'un homme dans la carte d'ID*/
function placerImageH(){
    let p = document.getElementById("perso");
    let n = document.getElementById("liste_hommes");
    if (n.value === "1"){
        p.src = "images/persos/hommes/aang.jpg"; 
    }
    if (n.value === "2"){
        p.src = "images/persos/hommes/batman.jpg"; 
    }
    if (n.value === "3"){
        p.src = "images/persos/hommes/captain.jpg"; 
    }
    if (n.value === "4"){
        p.src = "images/persos/hommes/deadpool.jpg"; 
    }
    if (n.value === "5"){
        p.src = "images/persos/hommes/hulk.jpg"; 
    }
    if (n.value === "6"){
        p.src = "images/persos/hommes/ironman.jpg"; 
    }
    if (n.value === "7"){
        p.src = "images/persos/hommes/spider.jpg"; 
    }
    if (n.value === "8"){
        p.src = "images/persos/hommes/starlord.jpg"; 
    }
}

/*Placer l'image d'une femme dans la carte d'ID*/
function placerImageF(){
    let p = document.getElementById("perso");
    let n = document.getElementById("liste_femmes");
    if (n.value === "1"){
        p.src = "images/persos/femmes/blackwidow.png"; 
    }
    if (n.value === "2"){
        p.src = "images/persos/femmes/gamora.jpg"; 
    }
    if (n.value === "3"){
        p.src = "images/persos/femmes/korra.png"; 
    }
    if (n.value === "4"){
        p.src = "images/persos/femmes/wonderwoman.jpg"; 
    }
}

/*Placer l'image d'un autre dans la carte d'ID*/
function placerImageA(){
    let p = document.getElementById("perso");
    let n = document.getElementById("liste_autres");
    if (n.value === "1"){
        p.src = "images/persos/autres/chat.png"; 
    }
    if (n.value === "2"){
        p.src = "images/persos/autres/zombi.jpg"; 
    }
    if (n.value === "3"){
        p.src = "images/persos/autres/vampire.png"; 
    }
    if (n.value === "4"){
        p.src = "images/persos/autres/tirex.png"; 
    }
    if (n.value === "5"){
        p.src = "images/persos/autres/werewolf.png"; 
    }
}

/*On écrit le nom de la personne dans la carte d'identité*/
function ecrireNom(){
    let pseudo = document.getElementById("nom");
    let element = document.getElementById("nomID");
    element.innerHTML = pseudo.value;
}


/*Theme de la carte*/
function theme(n){
    let couleur = document.getElementById("carte");
    if (n === 1){
        couleur.style.backgroundImage = 'url(images/fonds/fondViolet.png)';
       }
       if (n === 2){
        couleur.style.backgroundImage = 'url(images/fonds/fondVert.png)';
       }
       if (n === 3){
        couleur.style.backgroundImage = 'url(images/fonds/fondBleu.png)';
       }
       if (n === 4){
        couleur.style.backgroundImage = 'url(images/fonds/fondOrange.png)';
       }
       if (n === 5){
        couleur.style.backgroundImage = 'url(images/fonds/fondJaune.png)';
       }
}

/*Description de la personne*/
function envoi(){
    let texte = document.getElementById("descrp");
    let content = texte.value;
    let zone = document.getElementById("zone");
    zone.style.visibility = "visible";
    zone.innerHTML = content;
}

/*Imprimer la page web*/
function imprimer(){
    window.print();
}

