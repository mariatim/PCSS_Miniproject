function cancel (element) {
    element.parentNode.parentNode.removeChild(element.parentNode);

    if (document.getElementById("cart").childElementCount == 0) {
        document.getElementById("cartGuide").classList.toggle("invisible");
        document.getElementById("price").innerHTML = "You have nothing in your cart!";
    } else {
        var canceledProduct = element.parentNode.childNodes[1].innerHTML;
        console.log(canceledProduct);
        var initPriceElementValue = document.getElementById("price").innerHTML;
        var processedValue = parseFloat(initPriceElementValue.replace(" kr.", ""));
        var processedPrice = parseFloat(canceledProduct.replace(" kr.", ""));
        var output = processedValue - parseFloat(processedPrice) + " kr.";
        document.getElementById("price").innerHTML = output;
    }
}


