var nombre=parseInt(prompt("Donnez un entier positif : "));
/*parseInt() permet de reconnaitre la réponse comme un nombre*/
var s=0;
var i=1;
while (i<=nombre){
  s+=i;  
  i++;     /*i augmente de 1*/
}
alert("La somme des "+nombre+" premiers entiers strictements positifs est "+s);

/*on affiche les 10 premiers entiers strictements positifs*/
for (let i=0;i<=10;i++){
  alert(i);
}