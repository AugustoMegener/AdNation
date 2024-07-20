document.getElementById('content').innerHTML = twemoji.parse(marked.parse(document.getElementById('content').innerHTML))
document.getElementById('form').innerHTML = twemoji.parse(document.getElementById('form').innerHTML)

document.getElementById('plus').addEventListener('click', function(event) {
    event.preventDefault(); 
    document.getElementById('ad-amount-content').innerHTML =  1 + +document.getElementById('ad-amount-content').innerHTML 
});

document.getElementById('sub').addEventListener('click', function(event) {
    event.preventDefault(); 
    document.getElementById('ad-amount-content').innerHTML =  Math.max(1, +document.getElementById('ad-amount-content').innerHTML - 1)
});