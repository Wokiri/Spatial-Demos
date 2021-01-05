const clientName = document.getElementById('client_name').value
const clientEmail = document.getElementById('client_email').value
const clientMessage = document.getElementById('client_message').value
const inquiryForm = document.getElementById('inquiryForm')


function sendEmail(){
    Email.send({
        SecureToken : "328ca5c9-e164-47f4-b584-a40539c09334",
        To : ['wokirijoe@gmail.com', clientEmail],
        From : clientEmail,
        Subject : `You have a Project Inquiry from ${clientName}`,
        Body : clientMessage
    }).then(
    message => alert(message)
    );
}

submitForm.addEventListener('submit', sendEmail)