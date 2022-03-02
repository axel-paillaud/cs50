const mapEuropeSvg = document.getElementById("map_of_europe");
var slideContainer = document.getElementById("slide_container");

mapEuropeSvg.style.visibility = "hidden";

function showOnOver() {
    slideContainer.classList.add("slide_transition");
    mapEuropeSvg.style.visibility = "visible";
}

function hideOnOut() {
    mapEuropeSvg.style.visibility = "hidden";
}