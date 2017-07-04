function select (elem,num) {
	$("#"+num+"dropdown").html(elem.innerText);
	document.getElementById(num).setAttribute('class', "comp "+elem.getAttribute('class'));
}

function compare (elem) {
	str1 = document.getElementById("team1").getAttribute('class').split(" ")[1];
	str2 = document.getElementById("team2").getAttribute('class').split(" ")[1];
	$(elem).attr("href","/game/"+str1+"_"+str2+"/");
}