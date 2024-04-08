// var like1 = document.querySelector("span");
// function addLike() {
//     var like2 =parseInt(like1.innerText,10)+1
//     like1.innerHTML = like2.toString()
//     console.log(like1.innerText)
// }

function addLike(element) {
    document.getElementById(element).innerText = parseInt( document.getElementById(element).innerText) + 1
}
