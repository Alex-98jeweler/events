


// async function get_token(event) {
//     event.preventDefault()
//     var data = new FormData(event.srcElement)
//     console.log(data)
    
// }


var form = document.getElementById('form-login')

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    username = form['username'].value;
    password = form['password'].value;
    data = {
        "username": username,
        "password": password
    }
    var response = await fetch('/api/v1/auth/jwt/create', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })
    var result = await response.json();
    var token = result.result.access
    localStorage.setItem('jwt_token', token)
    form.submit();
})