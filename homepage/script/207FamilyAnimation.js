const family = document.getElementById("svg207Family");
const familyStand = document.getElementById("207FamilyStand");
const familyAnim1 = document.getElementById("207FamilyAnim1");
const familyAnim2 = document.getElementById("207FamilyAnim2");
const familyAnim3 = document.getElementById("207FamilyAnim3");
const camionAnim1 = document.getElementById("camionCote1");
const camionAnim2 = document.getElementById("camionCote2");
let camionIntervId;
let familyIntervId;
var delayMoveRight = [7000, 5000, 10000];
var multiplePosRight = [20, 40, 60];
var pos = 0;

function randomMultiplePosRight(items) {
    return items[Math.floor(Math.random()*items.length)];
}

function randomDelayMoveRight(items) {
    return items[Math.floor(Math.random()*items.length)];
}

function familyStandBy() {
    familyStand.style.visibility = "visible";
    familyAnim1.style.visibility = "hidden";
    familyAnim2.style.visibility = "hidden";
    familyAnim3.style.visibility = "hidden";
    camionAnim1.style.visibility = "hidden";
    camionAnim2.style.visibility = "hidden";
}

function stopMove() {
    clearInterval(camionIntervId);
    clearInterval(familyIntervId);
    familyIntervId = null;
    camionIntervId = null;
    familyStandBy();
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

function randomStart() {
    var vRandomDelay = randomDelayMoveRight(delayMoveRight);
    setTimeout(moveRight, vRandomDelay)
}

function moveRight() {
    setTimeout(stopMove, 3000);
    if (!camionIntervId && !familyIntervId)
    {
        camionIntervId = setInterval(animCamionRight, 200);
        familyIntervId = setInterval(animFamilyRight, 500);
    }
    var maxWidth = window.innerWidth;
    pos += randomMultiplePosRight(multiplePosRight);
    if (pos >= (maxWidth / 2)) {
        stopMove();
        return;
    }
    else {
        family.style.transform = "translate(" + pos +"px, 0px)";
        randomStart();
    }
}

randomStart();
