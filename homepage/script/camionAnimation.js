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
    if (document.body.scrollTop > (window.innerWidth * 0.886) || document.documentElement.scrollTop > (window.innerWidth * 0.886))
    {
        animCamion();
    }
}

function getScrollValue() {
    let scrollValue = document.documentElement.scrollTop;
    console.log(scrollValue);
}

function getWindowWidth() {
    let windowWidth = window.innerWidth;
    console.log(windowWidth);
}

function getWindowHeight() {
    let windowHeight = window.innerHeight
    console.log(windowHeight)
}

window.onscroll = function() {startAnim()};

setInterval(switchAnim, 200);
