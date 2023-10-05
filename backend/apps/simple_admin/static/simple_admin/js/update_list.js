



async function update_list(elementId, elementName) {
    var list = document.getElementById(elementId);
    var token = localStorage.getItem('jwt_token')
    var response = await fetch('/api/v1/event/', {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    })
    if (response.status === 401) {
        console.log('here')
        var refresh_data = {
            "refresh": localStorage.getItem('refresh')
        };
        var response = await fetch('/api/v1/auth/jwt/refresh', {
            method: 'POST',
            body: JSON.stringify(refresh_data),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        });
        var result = await response.json();
        var token = result.result.access;
        localStorage.setItem('jwt_token', token);
        update_list(elementId, elementName);
    } else {
        buf = await response.json();
        var result = buf.result.results;
        var list = document.getElementById(elementId);
        var liLength = list.getElementsByTagName('li').length
        if (liLength < result.length) {
            for (let i = liLength; i < result.length; i++) {
                console.log('here')
                var elementLi = document.createElement('li');
                var elementLink = document.createElement('a')
                elementLink.setAttribute('href', `/${elementName}/${result[i].id}`)
                var textnode = document.createTextNode(`${result[i].title}`);
                elementLink.appendChild(textnode)
                elementLi.appendChild(elementLink)
                list.appendChild(elementLi);
            }
        }
        console.log(buf);
    }
}
