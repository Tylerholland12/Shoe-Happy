<script src="myscripts.js"></script>

function randomString() {
    var chars = '01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghiklmnopqrstuvwxyz'; 
    var stringlength = 5; 
    var text = '';
    for (var i = 0; i < stringlength; i++) {
    var rnum = Math.floor(Math.random() * chars.length);
    text += chars.substring(rnum,rnum+1);
    }

    var source = 'https://www.flickr.com/search/?text=shoes' + text + '.jpg';

    var image = new Image();
    image.onload = function() {
        if (this.width == 161) {
        randomString();
        } else {
        $('.stuff img').replaceWith(this);
        $('#output').text(text);
        }
    };
    image.src = source;
}

$(document).ready(function() { 
randomString();
});