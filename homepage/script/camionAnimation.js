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
    
}

setInterval(switchAnim, 200);
