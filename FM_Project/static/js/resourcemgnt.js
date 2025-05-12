document.getElementsByClassName("f-container")[0].addEventListener('click', function() {
    var arrow = document.getElementsByClassName("arrow")[0];
    var insidecontainer = document.getElementsByClassName("inside-container")[0];

    
    if (arrow.classList.contains("hidden")) {
        arrow.classList.remove("hidden"); 
    } else {
        arrow.classList.add("hidden"); 
    }

    if (insidecontainer.classList.contains("hidden")) {
        insidecontainer.classList.remove("hidden"); 
    } else {
        insidecontainer.classList.add("hidden"); 
    }
});
