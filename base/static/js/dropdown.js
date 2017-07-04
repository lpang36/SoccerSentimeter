function select (elem,num) {
	document.getElementById("team"+num).innerText = elem.innerText;
	document.getElementById("team"+num).setAttribute('class', "comp "+elem.getAttribute('class'));
}

function compare (elem) {
	str1 = document.getElementById("team1").getAttribute('class').split(" ")[1];
	str2 = document.getElementById("team2").getAttribute('class').split(" ")[1];
	elem.setAttribute('href', "{% url 'game' "+str1+" "+str2+" %}");
}