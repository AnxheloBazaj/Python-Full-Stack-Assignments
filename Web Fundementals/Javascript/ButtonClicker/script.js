function logout(element) {
    if (element.innerText == "Log in") {
        element.innerText = "Log out"
    }
    else {
        element.innerText = "Log in"
    }
}

function removeDef(element) {
    element.remove()
}

function likes(){
    alert("You liked a post ;)");
    
}