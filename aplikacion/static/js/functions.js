// Contact
document.getElementById("contactForm").addEventListener('submit', function (event) {

    let name = document.getElementById("name").value
    let surname = document.getElementById("surname").value
    let email = document.getElementById("email").value
    let comment = document.getElementById("comment").value
    let sms = document.getElementById("alert")

    if (name === '' || surname === "" || email === '' || comment === "") {
        sms.textContent = 'Please fill in all fields.';
        sms.style.display = "block"
        sms.classList.add("alert-danger")
        event.preventDefault();
        return
    }

    if (!/^[a-zA-Z]+$/.test(name) || !/^[a-zA-Z]+$/.test(surname)) {
        sms.textContent = 'Name should only contain letters.';
        sms.style.display = "block"
        sms.classList.add("alert-danger")
        event.preventDefault();
        return
    }

    sms.textContent = 'Subscription successful!';
    sms.style.display = "block"
    sms.classList.remove("alert-danger")
    sms.classList.add("alert-success")
    event.preventDefault();

})
