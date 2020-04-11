function affiche(n){
    switch(n) {
        case 1:
          location.assign("pagePython.html");
          break;
        case 2:
          location.assign("pageBinaire.html");
          break;
        case 3:
          location.assign("pageWeb.html");
          break;
        case 4:
          location.assign("pageArchi.html");
          break;
        case 5:
          location.assign("pageStructure.html");
          break;
        case 6:
          location.assign("pageAlgo.html");
          break;
        case 7:
          location.assign("pageMicrocontroleur.html");
          break;
        case 8:
          location.assign("pageProjet.html");
          break;
        case 9:
          location.assign("pageExos.html");
          break;
        case 10:
          location.assign("pageFormulaire.html");
          break;
        default:
          alert("ok");
      }
    /*if (n===1){
        location.assign("pagePython.html");
    } 
    else{
        location.assign("pageWeb.html");
    }*/
    
}