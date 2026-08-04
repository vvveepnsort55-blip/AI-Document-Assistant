const menuBtn =
document.getElementById(
    "menu-toggle"
);



const sidebar =
document.querySelector(
    ".sidebar"
);



menuBtn.addEventListener(
    "click",
    function(){


        sidebar.classList.toggle(
            "active"
        );


    }
);