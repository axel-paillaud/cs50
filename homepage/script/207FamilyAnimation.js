const family = document.getElementById("animContainer");
const familyStand = document.getElementById("207FamilyStand");
const familyAnim1 = document.getElementById("207FamilyAnim1");
const familyAnim2 = document.getElementById("207FamilyAnim2");
const familyAnim3 = document.getElementById("207FamilyAnim3");
const camionAnim1 = document.getElementById("camionCote1");
const camionAnim2 = document.getElementById("camionCote2");
var move = false;
let nIntervId;

function familyStandBy() {
    familyStand.style.visibility = "visible";
    familyAnim1.style.visibility = "hidden";
    familyAnim2.style.visibility = "hidden";
    familyAnim3.style.visibility = "hidden";
    camionAnim1.style.visibility = "hidden";
    camionAnim2.style.visibility = "hidden";
}

familyStandBy();

function animFamilyRight() {

    if (familyAnim1.style.visibility == "visible")
    {
        familyAnim1.style.visibility = "hidden";
        familyAnim2.style.visibility = "visible";
        familyAnim3.style.visibility = "hidden";
    }

    else if (familyAnim2.style.visibility == "visible")
    {
        familyAnim1.style.visibility = "hidden";
        familyAnim2.style.visibility = "hidden";
        familyAnim3.style.visibility = "visible";
    }

    else if (familyAnim3.style.visibility == "visible")
    {
        familyAnim1.style.visibility = "visible";
        familyAnim2.style.visibility = "hidden";
        familyAnim3.style.visibility = "hidden";
    }
}

function animCamionRight() {
    if (familyStand.style.visibility == "visible")
    {
        familyStand.style.visibility = "hidden";
        camionAnim1.style.visibility = "visible";
        familyAnim1.style.visibility = "visible";
    }

    else if (camionAnim1.style.visibility == "visible")
    {
        camionAnim1.style.visibility = "hidden";
        camionAnim2.style.visibility = "visible";
    }

    else {
        camionAnim1.style.visibility = "visible";
        camionAnim2.style.visibility = "hidden";
    }
}

function checkMove() {
    if (move == true) {
        setInterval(animCamionRight, 200);
        setInterval(animFamilyRight, 500);
    }
    else {
        familyStandBy();
    }
}

function moveRight() {
    move = true;
    animCamionRight();
    animFamilyRight();
    checkMove();
    /*Ici, il faudrait que cela déplace de +30px à chaque fois */
    family.style.transform = "translate(30px, 0px)";
    move = false;
    checkMove();
}

function stopMove() {
    clearInterval();
}

setInterval(moveRight, 10000);