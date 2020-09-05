const sendHttpRequest = (method, url) => {
    const promise = new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.responseType = 'json';

        xhr.open(method, url);
        // xhr.setRequestHeader('Access-Control-Allow-Origin', '*')

        xhr.onload = () => {
            resolve(xhr.response);
        }

        xhr.send();
    });
    return promise

};


const getData = () => {
    // https://www.youtube.com/watch?v=4K33w-0-p2c
    sendHttpRequest('GET', 'https://kpchvq2a30.execute-api.us-west-2.amazonaws.com/prod/states')
        .then(responseData => {
            console.log(responseData)
            let count_element = document.getElementById('counter');
            count_element.innerHTML = responseData
        })

}

// when the webpage loads run the counter function
window.onload = getData


