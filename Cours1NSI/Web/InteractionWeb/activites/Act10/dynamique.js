/*On retient le numéro de la porte choisie*/
var numero;
/*On efface les deux portes sui sont inutiles*/
function choisir(){
    let choix=document.getElementById("menu");
    let porte=choix.value;
    let p1=document.getElementById("im1");
    let p2=document.getElementById("im2");
    let p3=document.getElementById("im3");
    if (porte==="porte1"){
        p2.remove();
        p3.remove();
        numero="1";
    }
    if (porte==="porte2"){
        p1.remove();
        p3.remove();
        numero="2";
      }
    if (porte==="porte3"){
        p2.remove();
        p1.remove();
        numero="3";
      }
    /*on fait apparaître le bouton*/
    let bouton=document.getElementById("bouton");
    bouton.style.visibility='visible'; 
}

function ouvrir(){
    /*on cache la dernière porte*/
    let porteChoisie=document.getElementById("im"+numero);
    porteChoisie.style.visibility='hidden';
    /*on crée un nouvel objet image (img)*/
    let newImage=document.createElement('img');
    /*on attribut une taille à l'image*/
    newImage.width="500";
    if (numero==="1"){
        /*on affecte la photo choisie*/
        newImage.src="lapin.jpg";
    }
    if (numero==="2"){
        newImage.src="jason.jpg";
    }
    if (numero==="3"){
        newImage.src="werewolf2.jpg";
    }
    /*on place la nouvelle image en tant qu'enfant du titre*/
    let lien=document.getElementById("grostitre");
    lien.appendChild(newImage);
}