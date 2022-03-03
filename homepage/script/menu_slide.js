const mapEuropeSvg = document.getElementById("map_of_europe");
const lightBulb = document.getElementById("light_bulb");
const camionSvg = document.getElementById("camion_slide");
const infoSvg = document.getElementById("info_svg");
var slideContainerTips = document.getElementById("slide_container_tips");
var slideContainerMap = document.getElementById("slide_container_map");
var slideContainerCamion = document.getElementById("slide_container_camion");
var slideContainerInfo = document.getElementById("slide_container_info");

mapEuropeSvg.style.visibility = "hidden";
lightBulb.style.visibility = "hidden";
camionSvg.style.visibility = "hidden";
infoSvg.style.visibility = "hidden";

function showOnOverMap() {
    slideContainerMap.classList.add("slide_transition_in");
    mapEuropeSvg.style.visibility = "visible";
    slideContainerMap.classList.remove("slide_transition_out");
}

function hideOnOutMap() {
    slideContainerMap.classList.remove("slide_transition_in");
    slideContainerMap.classList.add("slide_transition_out");
}

function showOnOverBulb() {
    slideContainerTips.classList.add("slide_transition_in");
    lightBulb.style.visibility = "visible";
    slideContainerTips.classList.remove("slide_transition_out");
}

function hideOnOutBulb() {
    slideContainerTips.classList.remove("slide_transition_in");
    slideContainerTips.classList.add("slide_transition_out");
}

function showOnOverCamion() {
    slideContainerCamion.classList.add("slide_transition_in");
    camionSvg.style.visibility = "visible";
    slideContainerCamion.classList.remove("slide_transition_out");
}

function hideOnOutCamion() {
    slideContainerCamion.classList.remove("slide_transition_in");
    slideContainerCamion.classList.add("slide_transition_out");
}

