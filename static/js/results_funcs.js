function formatViews() {
	var elements = document.getElementsByClassName('views');
	for (var i = 0; i < elements.length; i++) {
		elements[i].innerHTML = elements[i].innerHTML.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
	}
}

function formatLength() {
	var secondsLength;
	var minutes;
	var seconds;
	var hours;
	var elements = document.getElementsByClassName('length');

	for (var i = 0; i < elements.length; i++) {
		secondsLength = parseInt(elements[i].innerHTML);
		hours = Math.floor(secondsLength/3600);
		minutes = Math.floor((secondsLength - (hours * 3600))/60);
		seconds = Math.floor(secondsLength - (minutes * 60) - (hours * 3600));
		elements[i].innerHTML = ""
		if (hours != 0) {
			elements[i].innerHTML = hours + ":";
		}

		if (seconds < 10) {
			seconds = "0" + seconds;
		}

		elements[i].innerHTML = elements[i].innerHTML + minutes + ":" + seconds;
	}
}

formatViews();
formatLength();