var objects = 1;

function addObjectBox() {
	objects++;

	var newObject = document.createElement("input");
	var container = document.getElementById("objects");

	newObject.type = "text";
	newObject.id = "object" + objects;
	newObject.name = "object" + objects;
	//newObject.value = '{{ request.GET.object5 }}';
	newObject.className = "form-control mt-2";

	container.appendChild(newObject);

	//var html = '<input type="text" id="objects' + objects + '" name="object' + objects + '" value="" class="form-control mt-2">';

	//document.getElementById("objects").innerHTML += html;
	//document.getElementById("object" + objects).value = "{{ request.GET.object" + parseInt(objects) + " }}";
}