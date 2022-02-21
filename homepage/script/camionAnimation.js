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

function animCamion() {
    camion1.style.transform = "translate(500px, 0px)";
    camion2.style.transform = "translate(500px, 0px)";
}

function startAnim() {
    if (document.body.scrollTop > 1758 || document.documentElement.scrollTop > 1758)
    {
        animCamion();
    }
}

function getScrollValue() {
    let scrollValue = document.documentElement.scrollTop;
    console.log(scrollValue);
}

window.onscroll = function() {startAnim()};

setInterval(switchAnim, 200);
