function identite(){
  let choix=document.getElementById("champ");
  let element=document.getElementById("nom");
  /*placer la valeur de la variable choix dans le titre*/
  element.innerHTML=choix.value;
}
function modif(){
    let titre=document.getElementById("grostitre");
    /*Changer la couleur du titre*/
    titre.style.color="red";
  }
  