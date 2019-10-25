// When the Add to cart button is clicked
function cartButtonClick(event) {
    var id = event.target.id;
    var orderedProduct = products[id];

    getProduct(orderedProduct.id);

    // Get rid of 'nothing in the cart'
    if (document.getElementById("cart").childElementCount == 0) {
        document.getElementById("cartGuide").classList.toggle("invisible");
        document.getElementById("price").innerHTML = "0 kr.";
    }

    // Update price
    var initPriceElementValue = document.getElementById("price").innerHTML;
    var processedValue = parseFloat(initPriceElementValue.replace(" kr.", ""));
    var output = processedValue + orderedProduct.price + " kr.";
    document.getElementById("price").innerHTML = output;
}

// Remove one order item
function remove (element) {
    element.parentNode.parentNode.removeChild(element.parentNode);

    if (document.getElementById("cart").childElementCount == 0) {
        document.getElementById("cartGuide").classList.toggle("invisible");
        document.getElementById("price").innerHTML = "Such empty!";
    } else {
        var canceledProduct = element.parentNode.childNodes[1].innerHTML;
        var initPriceElementValue = document.getElementById("price").innerHTML;
        var processedValue = parseFloat(initPriceElementValue.replace(" kr.", ""));
        var processedPrice = parseFloat(canceledProduct.replace(" kr.", ""));
        var output = processedValue - parseFloat(processedPrice) + " kr.";
        document.getElementById("price").innerHTML = output;
    }
}

function reload(){
    window.location.reload();
}

function checkout(){
    postOrder(order);
    order = [];
}