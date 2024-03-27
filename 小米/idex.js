const img1 = document.querySelector('.lbtim')
let arr = 0;



const a1data = [
    { url: './素材/picture/10194.png' },
    { url: './素材/picture/10195.png' },
    { url: './素材/picture/10196.png' }

]

setInterval(function () {
    if (arr <= a1data.length) {
        arr++;
    }
    else {
        arr = 0;
    }

    img1.src = a1data[arr].url;

}, 1000)


// 按钮
const fan = document.querySelector('.lbu')
const ran = document.querySelector('.rbu')

fan.onclick = function () {
    // random = - 1;

    if (arr > 0) {
        arr--;
    }
    else {
        arr = 2;
    }
    console.log(arr)
    img1.src = a1data[arr].url
    


}
ran.onclick = function () {
    // random = + 1;

    if (arr < 2) {
        arr++;
    }
    else {
        arr = 0;
    }
    console.log('按钮' + arr)
    img1.src = a1data[arr].url


}


//购物车
const gwcd = document.querySelector('.gwc1')
const gwcli = document.querySelector('#gwcli')
console.log(gwcli)


gwcli.onmouseover = function () {
    gwcd.style.display = 'block'
}

gwcli.onmouseout = function () {
    gwcd.style.display = 'none'
}


