function factorsOf() {
	var nmbr = prompt("Number");
	document.getElementById("factorsOfOutput").innerHTML = "The factors of " + nmbr + " are<br/>";
	for (var i = 1; i <= nmbr; i++) {
		if (nmbr / i === Math.round(nmbr / i)) {
			document.getElementById("factorsOfOutput").innerHTML += i + "<br/>"
		}
	}
}
