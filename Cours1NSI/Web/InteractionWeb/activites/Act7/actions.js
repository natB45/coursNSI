function changer(){
  let choix=document.getElementById("menu");
  let couleur=choix.value; /*on regarde quelle est la couleur choisie*/
  if (couleur=="coul"){
    document.body.style.backgroundColor="white";
  }
  if (couleur=="coul1"){
    document.body.style.backgroundColor="green";
  }
  if (couleur=="coul2"){
    document.body.style.backgroundColor="blue";
  }
  if (couleur=="coul3"){
    document.body.style.backgroundColor="orange";
  }

}
