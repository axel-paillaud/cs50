const mapEuropeSvg = document.getElementById("map_of_europe");
const lightBulb = document.getElementById("light_bulb");
const camionSvg = document.getElementById("camion_slide");
const infoSvg = document.getElementById("info_svg");
var slideContainerTips = document.getElementById("slide_container_tips");
var slideContainerMap = document.getElementById("slide_container_map");
var slideContainerCamion = document.getElementById("slide_container_camion");
var slideContainerInfo = document.getElementById("slide_container_info");
var onClick = False;

mapEuropeSvg.style.visibility = "hidden";
lightBulb.style.visibility = "hidden";
camionSvg.style.visibility = "hidden";
infoSvg.style.visibility = "hidden";

function showOnOver(svg, containerSvg) {
    containerSvg.classList.add("slide_transition_in");
    svg.style.visibility = "visible";
    containerSvg.classList.remove("slide_transition_out");
}

function hideOnOut(containerSvg, click) {
    if (click == True) {
        
    }
    containerSvg.classList.remove("slide_transition_in");
    containerSvg.classList.add("slide_transition_out");
}

function stayOnClick(containerSvg, click) {
    click = True;
}
