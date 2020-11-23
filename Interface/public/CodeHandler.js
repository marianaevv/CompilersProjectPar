$('#codeGenerated').val('program;\n\tmain{\n\t\n\t}\n');

$('#run').click(function () {
	//String que se mandará al compilador.
	var str = $('#codeGenerated').val();
	console.log(str);
	jsonOBJ = { data: str };
	$.ajax({
		url: 'http://localhost:8080/compile',
		type: 'Post',
		data: JSON.stringify(jsonOBJ),
		headers: {
			'Content-Type': 'application/json',
		},
		error: function (err) {
			console.log(err);
		},
	});
});

$('textarea').keydown(function (e) {
	if (e.keyCode === 9) {
		var start = this.selectionStart;
		var end = this.selectionEnd;

		var $this = $(this);
		var value = $this.val();
		$this.val(value.substring(0, start) + '\t' + value.substring(end));

		this.selectionStart = this.selectionEnd = start + 1;

		e.preventDefault();
	}
});

$('#codeGenerated').click(function () {
	cursorPosition = $('#codeGenerated').prop('selectionStart');
});
