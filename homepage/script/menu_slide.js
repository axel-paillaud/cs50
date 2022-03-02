const mapEuropeSvg = document.getElementById("map_of_europe");
var slideContainer = document.getElementById("slide_container");

mapEuropeSvg.style.visibility = "hidden";

function showOnOver() {
    slideContainer.classList.add("slide_transition_in");
    mapEuropeSvg.style.visibility = "visible";
    slideContainer.classList.remove("slide_transition_out");
}

function hideOnOut() {
    slideContainer.classList.remove("slide_transition_in");
    slideContainer.classList.add("slide_transition_out");
}