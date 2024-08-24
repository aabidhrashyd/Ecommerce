(function ($) {
    "use strict";

    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });


    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({ scrollTop: 0 }, 1500, 'easeInOutExpo');
        return false;
    });


    // Vendor carousel
    $('.vendor-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0: {
                items: 2
            },
            576: {
                items: 3
            },
            768: {
                items: 4
            },
            992: {
                items: 5
            },
            1200: {
                items: 6
            }
        }
    });


    // Related carousel
    $('.related-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 2
            },
            768: {
                items: 3
            },
            992: {
                items: 4
            }
        }
    });


    // Product Quantity
    $('.quantity button').on('click', function () {
        var button = $(this);
        var oldValue = button.parent().parent().find('input').val();
        if (button.hasClass('btn-plus')) {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            if (oldValue > 0) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 0;
            }
        }
        button.parent().parent().find('input').val(newVal);
    });

})(jQuery);

document.getElementById('registration-form').addEventListener('submit', function (event) {
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;

    if (password !== confirmPassword) {
        event.preventDefault();
        alert("Passwords do not match!");
    }
    //////



});


//////

document.addEventListener('DOMContentLoaded', () => {
    const cart = [];

    document.querySelectorAll('.add-to-cart-btn').forEach(button => {
        button.addEventListener('click', () => {
            const productId = button.getAttribute('data-product');
            const productPrice = button.getAttribute('data-price');

            // Add product to cart
            cart.push({ id: productId, price: productPrice, quantity: 1 });

            // Update cart display
            updateCart();
        });
    });

    function updateCart() {
        const cartTableBody = document.querySelector('.cart tbody');
        cartTableBody.innerHTML = ''; // Clear current cart items

        let subtotal = 0;

        cart.forEach(item => {
            const totalPrice = item.price * item.quantity;
            subtotal += totalPrice;

            cartTableBody.innerHTML += `
                <tr>
                    <td>Product ${item.id}</td>
                    <td>$${item.price}</td>
                    <td>
                        <button class="quantity-btn">-</button>
                        <input type="text" value="${item.quantity}">
                        <button class="quantity-btn">+</button>
                    </td>
                    <td>$${totalPrice}</td>
                    <td><button class="remove-btn">X</button></td>
                </tr>
            `;
        });

        document.querySelector('.cart-summary .subtotal').innerText = `Subtotal: $${subtotal}`;
        document.querySelector('.cart-summary .total').innerText = `Total: $${subtotal + 10}`; // Adding $10 shipping
    }
});