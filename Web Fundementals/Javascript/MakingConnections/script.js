function changeNameInput(element) {
    document.getElementById(element).innerHTML = `
        <input id="myInput" type="text" placeholder="New Name">
        <button type="button" onclick="changeName('name', 'myInput','inputField')">Save</button>
    `;

}
function changeName(id1, id2, id3) {
    document.getElementById(id1).innerText = document.getElementById(id2).value
    document.getElementById(id3).innerHTML = `
    <div id="inputField">
        <p  onclick="changeNameInput('inputField')"><img src="icons/gear.png" alt="gear" class="icon-s"> edit profile</p>
    </div>  
    `;
}

function accept(element, element2, element3){
    element.closest('li').remove();
    document.getElementById(element2).innerText = parseInt(document.getElementById(element2).innerText)-1
    document.getElementById(element3).innerText = parseInt(document.getElementById(element3).innerText)+1

}

function del(element, element2){
    element.closest('li').remove();
    document.getElementById(element2).innerText = parseInt(document.getElementById(element2).innerText)-1
}


