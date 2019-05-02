var namespace = '/main';
var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

socket.on('get_new_message', function(msg){
	$('#' + msg.id).children('a').children('.message').text(msg.message);
});

socket.on('timer', function(data){
	alert(data)
});

socket.on('info_responder', function(data) {
	window.self_name = data.self_name;
});

function CreateNewMessage() {
		var msgbox = document.getElementsByClassName('messageblock')[0].cloneNode(true);
		var name = window.self_name;
		var messagebox = document.getElementsByClassName('send_form')[0];
		var sender = msgbox.getElementsByClassName('sender')[0];
		var msg = msgbox.getElementsByClassName('message_text')[0];
		var storage = document.getElementsByClassName('messages')[0];
		message  = messagebox.childNodes[3].firstChild;		
		sender.firstChild.innerHTML = name;
		msg.innerHTML = message.value;
		storage.appendChild(msgbox);
		socket.emit('get_message', {messaga: message.value});
		message.value = '';
		return false;	
	}; 
	