document.getElementById("icon-menu").addEventListener("click",mostrar_menu);

function mostrar_menu(){
    document.getElementById("move-content").classList.toggle('move-container-x')
    document.getElementById("show-menu").classList.toggle('show-lateral')
}

