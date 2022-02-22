const familyStand = document.getElementById("207FamilyStand");
const familyAnim1 = document.getElementById("207FamilyAnim1");
const familyAnim2 = document.getElementById("207FamilyAnim2");
const familyAnim3 = document.getElementById("207FamilyAnim3");
const camionAnim1 = document.getElementById("camionCote1");
const camionAnim2 = document.getElementById("camionCote2");

var showFamilyStand = familyStand.style.visibility;
var showFamilyAnim1 = familyAnim1.style.visibility;
var showFamilyAnim2 = familyAnim2.style.visibility;
var showFamilyAnim3 = familyAnim3.style.visibility;
var showCamionAnim1 = camionAnim1.style.visibility;
var showCamionAnim2 = camionAnim2.style.visibility;

familyAnim1.style.visibility = "hidden";
familyAnim2.style.visibility = "hidden";
familyAnim3.style.visibility = "hidden";

showFamilyStand = "visible";
showFamilyAnim1 = "hidden";
showFamilyAnim2 = "hidden";
showFamilyAnim3 = "hidden";
showCamionAnim1 = "hidden";
showCamionAnim2 = "hidden";

function animFamilyRight() {
    if (showFamilyStand == "visible")
    {
        showFamilyStand = "hidden";
        showFamilyAnim1 = "visible";
        showFamilyAnim2 = "hidden";
        showFamilyAnim3 = "hidden";
        showCamionAnim1 = "visible";
    }

    if (showFamilyAnim1 = "visible")
    {
        showFamilyAnim1 = "hidden";
        showFamilyAnim2 = "visible";
        showFamilyAnim3 = "hidden";
    }

    else if (showFamilyAnim2 = "visible")
    {
        showFamilyAnim1 = "hidden";
        showFamilyAnim2 = "hidden";
        showFamilyAnim3 = "visible";
    }

    else if (showFamilyAnim3 = "visible")
    {
        showFamilyAnim1 = "visible";
        showFamilyAnim2 = "hidden";
        showFamilyAnim3 = "hidden";
    }
}

function animCamionRight() {
    if (showCamionAnim1 = "visible")
    {
        showCamionAnim1 = "hidden";
        showCamionAnim2 = "visible";
    }

    else
    {
        showCamionAnim1 = "visible";
        showCamionAnim2 = "hidden";
    }
}