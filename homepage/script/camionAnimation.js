const camion1 = document.getElementById("camionInkAnim1");
const camion2 = document.getElementById("camionInkAnim2");
camion1.style.display = "block";
camion2.style.display = "none";

function moteur(anim1, anim2) {

    if (anim1.style.display == "block") {
        anim1.style.display = "none";
        anim2.style.display = "block";
        }

    else {
        anim1.style.display = "block";
        anim2.style.display = "none";
        }
    }

window.setInterval(moteur(camion1, camion2), 500);
