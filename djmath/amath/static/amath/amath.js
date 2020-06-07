let dEls = document.getElementsByClassName("test")
for (del of dEls) {
    let children = del.children
    let img = children[0]
    let input = children[1]

    let f = function () {
        if (input.value == input.className) {
            img.src = "static/amath/images/ok.png"
        } else {
            img.src = "static/amath/images/not_ok.png"
        }
    }
    input.addEventListener('input', f, false)
}