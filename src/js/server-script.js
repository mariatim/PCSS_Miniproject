// GET ALL PRODUCTS
//#region

// Server request to load all events
$("document").ready(function () {
    $.ajax({
        async: true,
        crossDomain: true,
        url: "http://127.0.0.1:5000/get/allproducts",
        dataType: 'jsonp',
        method: "GET",
        error: function (xhr, ajaxOptions, thrownError) {
            if (xhr.status != 200) {
                console.log(xhr.status);
                console.log(thrownError);
            }
        }
    })
})

// Callback for loading all events
function getAllCallback(response) {
    response.forEach(element => {
        products.push(JSON.parse(element));
    })

    // Fill the HTML
    products.forEach(element => {
        $("#fillHere").append(
            `<div class="col-lg-4 col-md-6 col-12">
                    <div class="card">
                        <div class="card-body">
                            <h5 class="card-title">` + element.name + `</h5>
                            <p class="card-text">` + element.description + `</p>
                            <b style="float: right;">` + element.price + ` kr.</b>
                            <a href="#" class="btn btn-primary cartButton" onclick="cartButtonClick(event)" id="` + element.id + `">Add to cart</a>
                        </div>
                    </div>
                </div>`);
    });
}
//#endregion

// GET ONE PRODUCT INFORMATION
//#region 
// Server request to load all events
function getProduct (_id) {
    $.ajax({
        async: true,
        crossDomain: true,
        crossOrigin: true,
        url: "http://127.0.0.1:5000/get/product/",
        dataType: 'json',
        data: { "id": _id.toString() },
        method: "GET",
        success: function (response) {
            // Fill the HTML
            document.getElementById("cart").innerHTML +=
                `<li class="list-group-item d-flex justify-content-between align-items-center">` + response.name + `
                    <span class="badge badge-primary badge-pill ">` + response.price + ` kr.</span>
                    <a href="#" class="badge badge-danger badge-pill" onClick=remove(this)>` + "Remove" + `</a>
                </li>`;

            // Add to order
            order.push(new Product(response.id, response.name, response.price, response.description, response.tickets));
        }
    })
}
//#endregion

// PUT ORDER
//#region
function postOrder(order) {
    $.ajax({
        async: true,
        crossDomain: true,
        crossOrigin: true,
        url: "http://127.0.0.1:5000/put/order/",
        dataType: 'json',
        data: { "products": JSON.stringify(order) },
        method: "GET",
        success: function (response) {
            window.location.reload();
            alert('Order placed successfully');
        },
        error: function (xhr, ajaxOptions, thrownError) {
            if (xhr.status != 200) {
                console.log(xhr.status);
                console.log(thrownError);
            }
        }
    })
}
//#endregion