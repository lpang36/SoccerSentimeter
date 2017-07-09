function adjustOnEnter() {
	if ($(window).width()<1200)
	    $("main").css("margin-left","200px");
}

function adjustOnExit() {
    if ($(window).width()<1200)
	    $("main").css("margin-left","0px");
}