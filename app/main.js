var canvas = document.querySelector("canvas");

canvas.style.border = "black solid 5px"

console.log(canvas.width, canvas.height)

var sendButton = document.getElementById("send-button")

var clearButton = document.getElementById("clear-button")

var signaturePad = new SignaturePad(canvas, {
    minWidth: 5,
    maxWidth: 10,
    penColor: "rgb(256,128,0)"
});

sendButton.addEventListener("click", async()=> {
    let image = signaturePad.toDataURL("image/jpeg")
    let options = {
        method:"POST",
        headers: {"content-type":'image/jpeg'},
        body: image
    }
    fetch("http://127.0.0.1:5000/", options).then(response => {
      return response.json()
    }).then(data => {
        return "The Prediction is " + data[0] + " with a confidence of " + data[1] + "%"
    }).then(data => {
        alert(data)
    })
})

clearButton.addEventListener("click", ()=>{
    signaturePad.clear();
})