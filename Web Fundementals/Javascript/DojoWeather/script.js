function updateContent(self, element) {
    var lastoption;
    

    if (self.value == "℃elcius" && lastoption == "℉arenheight") {
        document.querySelectorAll(`.${element}`).forEach((spanTag, index) => {
            spanTag.textContent = Math.floor(parseInt(spanTag.textContent) / 33.8);
        });
        lastoption = "℃elcius"
        
    }else if (self.value == "℉arenheight") {
        document.querySelectorAll(`.${element}`).forEach((spanTag, index) => {
            spanTag.textContent = Math.floor(parseInt(spanTag.textContent) * 33.8);
        });
        lastoption = "℉arenheight"
        console.log(lastoption)
    }
    //

}


