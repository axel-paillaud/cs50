const camion1 = document.getElementById("camionInkAnim1");
const camion2 = document.getElementById("camionInkAnim2");
camion1.style.visibility = "visible";
camion2.style.visibility = "hidden";



function switchAnim() {

    if (camion1.style.visibility == "visible") {
        camion1.style.visibility = "hidden";
        camion2.style.visibility = "visible";
        }

    else {
        camion1.style.visibility = "visible";
        camion2.style.visibility = "hidden";
        }
    }

function startAnim() {
    camion1.style.transform = "translate(500px, 0px)";
    camion2.style.transform = "translate(500px, 0px)";
}

setInterval(switchAnim, 200);
