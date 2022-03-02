const mapEuropeSvg = document.getElementById("map_of_europe");
var slideContainerMap = document.getElementById("slide_container_map");

mapEuropeSvg.style.visibility = "hidden";

function showOnOver() {
    slideContainerMap.classList.add("slide_transition_in");
    mapEuropeSvg.style.visibility = "visible";
    slideContainerMap.classList.remove("slide_transition_out");
}

function hideOnOut() {
    slideContainerMap.classList.remove("slide_transition_in");
    slideContainerMap.classList.add("slide_transition_out");
}