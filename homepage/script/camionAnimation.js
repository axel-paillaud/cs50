const camion1 = document.getElementById("camionInkAnim1");
const camion2 = document.getElementById("camionInkAnim2");

function moteur() {
    var show1 = camion1.style.display;
    var show2 = camion2.style.display;

    show1 == "block";
    show2 == "none";
    console.log(show1);
    console.log(show2);
}

console.log(camion1);
moteur();
