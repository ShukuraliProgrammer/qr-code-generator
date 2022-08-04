function changeColor(color1,color2){
    document.getElementById('change-color').style.backgroundColor=color1;
    document.getElementById('change-color-btn').style.backgroundColor=color2;

    document.getElementById('change-first-value').value = color1;
    document.getElementById('change-second-value').value = color1;

    document.getElementById('change-button-color-1').value = color2;
    document.getElementById('change-button-color-2').value = color2;
}
function changeImg(src){
    document.getElementById('change-image').src = src;
}
