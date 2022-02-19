const camion1 = document.getElementById("camionInkAnim1");
const camion2 = document.getElementById("camionInkAnim2");

function moteur() {
    let delay = 500;
    camion1.style.display = "block";
    camion2.style.display = "none";

    while(true) {
        if (camion1.style.display == "block") {
            setTimeout(function() {
            camion1.style.display = "none";
            camion2.style.display = "block";
            }, );
        }
        else {
            camion1.style.display = "block";
            camion2.style.display = "none";
        }
    }
}

console.log(camion1);

moteur();

