var namespace = '/main';
var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

socket.on('get_new_message', function(msg){
	var url = window.location.href;
	url = url.split('/');
	if (url[3]==='dialogs' || url[3]=='dialogs.html') {
		console.log('kek');
		$('#' + msg.id).children('a').children('.message').text(msg.message);
	}
	
	else {
		if (msg.id- 1 == window.location.pathname.split('/')[2]) {
			CreateNewMessage(msg.name, msg.message);
		};		
	};	
	
});

socket.on('timer', function(data){
	alert(data)
});

socket.on('info_responder', function(data) {
	window.self_name = data.self_name;
});

function send_message() {
	var messagebox = document.getElementsByClassName('send_form')[0];
	var message = messagebox.childNodes[3].firstChild
	var id_ = window.location.pathname.split('/')[2]
	console.log(window.location.pathname.split('/'))
	CreateNewMessage(window.self_name, message.value );
	
	socket.emit('get_message', {messaga: message.value, user_id :id_});
	message.value = '';
};

function CreateNewMessage(nm, msg) {
	var msgbox = document.getElementsByClassName('messageblock')[0].cloneNode(true);
	var sender = msgbox.getElementsByClassName('sender')[0];
	var msg_ = msgbox.getElementsByClassName('message_text')[0];
	var storage = document.getElementsByClassName('messages')[0];
	sender.firstChild.innerHTML = nm;
	msg_.innerHTML = msg;
	storage.appendChild(msgbox);
	
	return false;	
	}; 
	