var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");
var x = canvas.width/2;   //coordonnées du centre de la balle
var y = canvas.height-30;
var dx = 1;   //déplacement de l'abscisse
var dy = -2;  //déplacement de l'ordonnée
var ballRadius = 10;  //rayon de la balle tracée
var paddleHeight = 10;  //Hauteur de la raquette
var paddleWidth = 75;   //largeur
var paddleX = (canvas.width-paddleWidth)/2;  //abscisse du coin surpérieur gauche
//booléens conservant l'état des touches gauche et droites (false : touche relâchée)
var rightPressed = false;  
var leftPressed = false;
//variables des briques
var brickRowCount = 3;  //nombre de lignes
var brickColumnCount = 5;  //nombre de colonnes
var brickWidth = 75;  //largeur
var brickHeight = 20;  //hauteur
var brickPadding = 10;  //espace entre les briques
var brickOffsetTop = 30;  //espace en haut
var brickOffsetLeft = 30;  //espace à gauche

var bricks = [];  //création d'un tableau contenant les objets briques
for(var c=0; c<brickColumnCount; c++) {
    bricks[c] = [];
    for(var r=0; r<brickRowCount; r++) {
        bricks[c][r] = { x: 0, y: 0, status: 1  };  //status 1 si on on trace le rectangle, 0 sinon
    }
}

//dessiner les briques
function drawBricks() {
    for(var c=0; c<brickColumnCount; c++) {
        for(var r=0; r<brickRowCount; r++) {
            if (bricks[c][r].status == 1) {
                var brickX = (c*(brickWidth+brickPadding))+brickOffsetLeft;
                var brickY = (r*(brickHeight+brickPadding))+brickOffsetTop;
                bricks[c][r].x = brickX;
                bricks[c][r].y = brickY;
                ctx.beginPath();
                ctx.rect(brickX, brickY, brickWidth, brickHeight);
                ctx.fillStyle = "#0095DD";
                ctx.fill();
                ctx.closePath();
            }
        }
    }
}

//On attend l'évènement : presser une touche va déclencher la fonction keyDownHandler
document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("keyup", keyUpHandler, false);
//Si la touche est pressée, l'état de la variable passe à true
function keyDownHandler(event) {
    //event est la variable correspondant à l'évènement capté
    //key permet de savoir qu'elle touche est enfoncée   
    if(event.key == "Right" || event.key == "ArrowRight") {  
        rightPressed = true;
    }
    else if(event.key == "Left" || event.key == "ArrowLeft") {
        leftPressed = true;
    }
}
//si la touche est relâchée, l'état passe à false
function keyUpHandler(event) {
    if(event.key == "Right" || event.key == "ArrowRight") {
        rightPressed = false;
    }
    else if(event.key == "Left" || event.key == "ArrowLeft") {
        leftPressed = false;
    }
}

//détection de collisions entre la balle et les briques
function collisionDetection() {
    for(var c=0; c<brickColumnCount; c++) {
        for(var r=0; r<brickRowCount; r++) {
            var b = bricks[c][r];  //on récupère l'objet brique
            //si la brique est affichée
            if (b.status == 1) {
                //on regarde si le centre de la balle est dans la brique
                if(x > b.x && x < b.x+brickWidth && y > b.y && y < b.y+brickHeight) {
                    dy = -dy;
                    b.status = 0;  //on change le status pour ne plus l'afficher
                }
            }
            
        }
    }
}

function drawBall() {
    //on trace la balle
    ctx.beginPath()
    ctx.arc(x, y, ballRadius, 0, Math.PI*2, false);  
    ctx.fillStyle = "red";
    ctx.fill();
    ctx.closePath();
}

function drawPaddle() {
    //on trace la raquette
    ctx.beginPath()
    ctx.rect(paddleX, canvas.height-paddleHeight, paddleWidth, paddleHeight);  
    ctx.fillStyle = "#0095DD";
    ctx.fill();
    ctx.closePath();
}

function draw() {
    //on efface ce qui est dessiné sur le caneva
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawPaddle(); //on place la raquette
    drawBall();  //on trace la balle
    drawBricks();  //on trace les rectangles
    collisionDetection();  //détection des collisions
    if (x + dx - ballRadius < 0  ||  x + dx + ballRadius > canvas.width) { 
        //on regarde si on touche le mur de gauche ou de droite
        dx = -dx;
    }
    if (y + dy - ballRadius < 0) {  
        //on regarde si on touche le mur du haut
        dy = -dy;   //dans ce cas, la balle rebondit
    }
    else if (y + dy + ballRadius > canvas.height) {
        //on sort en bas de la fenêtre : on affiche Game Over
        alert("GAME OVER"); 
        //on redémarre le jeu en rechargeant la page.
        document.location.reload();
        }  
    else if (y + dy + ballRadius >= canvas.height - paddleHeight + 3) {
            //on touche la bas de la fenêtre
            //si on touche la raquette
            if(x > paddleX && x < paddleX + paddleWidth) {
                dy = -dy;
            }
    }
    x += dx
    y += dy
    //on déplace la raquette vers la gauche et on empêche la sortie de la fenêtre
    if (leftPressed == true && paddleX >= 0) {
        paddleX -= 7
    }
    //on déplace la raquette vers la droite et on empêche la sortie de la fenêtre
    if (rightPressed == true && paddleX + paddleWidth <= canvas.width) {
        paddleX += 7
    }
    
}

setInterval(draw, 10);  //lancement de la fonction draw toutes les 10 ms