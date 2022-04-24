function updateKeyInput(val) {
    document.getElementById('keySecureness').value = val; 
  }

function updateRangeInput(val) {
  document.getElementById('keySecurenessLevel').value = val;
}

function buttonClick(){
var num = $('#keySecureness').val();
console.log(num);
$.get( "/hello?num="+num, function( data ) {
    $('#displayKey').text(data);
});
}

function encrypt(){
var key = $('#inputKey').val();
var mess = $('#orignalMessageInput').val();
$.get( "/encryptMess?key=" + key + "&mess=" + mess , function( data ) {
    $('#encryptedMessage').text(data);
    });
}