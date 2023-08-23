var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', { style: style });
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');
form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({ 'disabled': true });
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    var fullName = document.getElementById('id_full_name').value;
    var phoneNumber = document.getElementById('id_phone_number').value;
    var email = document.getElementById('id_email').value;
    var streetAddress1 = document.getElementById('id_street_address1').value;
    var streetAddress2 = document.getElementById('id_street_address2').value;
    var townOrCity = document.getElementById('id_town_or_city').value;
    var country = document.getElementById('id_country').value;
    var county = document.getElementById('id_county').value;

    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(fullName),
                    phone: $.trim(phoneNumber),
                    email: $.trim(email),
                    address: {
                        line1: $.trim(streetAddress1),
                        line2: $.trim(streetAddress2),
                        city: $.trim(townOrCity),
                        country: $.trim(country),
                        state: $.trim(county),
                    }
                }
            },
            shipping: {
                name: $.trim(fullName),
                phone: $.trim(phoneNumber),
                address: {
                    line1: $.trim(streetAddress1),
                    line2: $.trim(streetAddress2),
                    city: $.trim(townOrCity),
                    country: $.trim(country),
                    state: $.trim(county),
                }
            },
        }).then(function (result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                card.update({ 'disabled': false });
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        location.reload();
    });
});
