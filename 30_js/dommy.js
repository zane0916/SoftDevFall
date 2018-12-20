var addItem = function(e) {
    var list = document.getElementById( "thelist");
    var item = document.createElement("li");
    item.innerHTML = "WORD";
    list.appendChild(item);
}

var button = document.getElementById("b");
button.addEventListener( 'click', addItem);
