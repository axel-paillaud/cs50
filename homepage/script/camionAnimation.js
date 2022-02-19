const camion1 = document.getElementById("camionInkAnim1");
const camion2 = document.getElementById("camionInkAnim2");

function moteur() {
    camion1.style.display = "block";
    camion2.style.display = "none";

    while(true) {
        camion1.style.display = "none";
        camion2.style.display = "block";
    }
}

console.log(camion1);
moteur();
