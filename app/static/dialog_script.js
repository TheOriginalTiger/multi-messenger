function CreateNewMessage() {
	var msgbox = document.getElementsByClassName('messageblock')[0].cloneNode(true);
	var name = 'Владимир';
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
};