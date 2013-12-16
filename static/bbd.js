
var rest_root = "http://localhost:8080";

function restGet(what) {
    var xmlHttp = null;
    xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", rest_root + what, false);
    xmlHttp.send(null);
    var response = xmlHttp.responseText;
    return JSON.parse(response);
}

function createNameButton(id, name) {
    var button = document.createElement('button');
    button.className = "namebutton";
    button.innerHTML = name;
    button.onclick = openUserOverview(id);
    return button;
}

function openUserOverview(id) {

    return function () {
        var userinfo = document.getElementById('userinfo');
        var title = document.getElementById('userinfotitle');
        var user = restGet("/users/" + id);
        title.innerHTML = user.name + ", saldo " + user.saldo;

        console.log(user);
    };
}

function display_userlist() {
    var userlist = document.getElementById("userlist");

    /* List of items */
    var users = restGet("/users");
    for (var key in users) {
        var button = createNameButton(key, users[key]);
        userlist.appendChild(button);
    }
}


function display_menu() {
    var menu = document.getElementById("menu");
    var items = restGet("/menu");
    for (var key in items) {
        var button = document.createElement('button');
        menu.appendChild(button);
        button.innerHTML = items[key];
    }
}
