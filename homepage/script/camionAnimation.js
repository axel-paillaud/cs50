const camion1 = document.getElementById("camionInkAnim1");
const camion2 = document.getElementById("camionInkAnim2");
camion1.style.display = "block";
camion2.style.display = "none";

function switchAnim() {

    if (camion1.style.display == "block") {
        camion1.style.display = "none";
        camion2.style.display = "block";
        }

    else {
        camion1.style.display = "block";
        camion2.style.display = "none";
        }
    }

function startAnim() {
    document.getElementById(camionInkAnim1).style.transform = "translate(500px, 0px)";
    document.getElementById(camionInkAnim2).style.transform = "translate(500px, 0px)";
}

setInterval(switchAnim, 200);
