function addToCart(productId) {
    fetch('/add_to_cart', {
        method: 'POST',
        body: new URLSearchParams({ 'product_id': productId }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            updateCart();
        } else {
            console.error(data.message);
        }
    });
}

function removeFromCart(productId) {
    fetch('/remove_from_cart', {
        method: 'POST',
        body: new URLSearchParams({ 'product_id': productId }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            updateCart();
        } else {
            console.error(data.message);
        }
    });
}

function updateCart() {
    const cartItemsList = document.getElementById("cartItems");
    cartItemsList.innerHTML = "";

    fetch('/get_cart_items')
    .then(response => response.json())
    .then(cartItems => {
        cartItems.forEach(item => {
            const listItem = document.createElement("li");
            listItem.textContent = `${item.name} - $${item.price.toFixed(2)}`;
            cartItemsList.appendChild(listItem);
        });
    });
}