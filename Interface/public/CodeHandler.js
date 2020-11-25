$('#codeGenerated').val('program;\n\tvar\n\t\n\tmain(){\n\t\n\t}\n');

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

var cursorPosition = 0;

function getVariables() {
	return 'int VARIABLE_NAME, VARIABLE_NAME, ETC;\n\tfloat VARIABLE_NAME, VARIABLE_NAME, ETC;\n\tchar VARIABLE_NAME, VARIABLE_NAME, ETC;';
}
function getVoidFunction() {
	return '\tmodule TIPO NOMBRE_FUNCION (TIPO PARAMETER_NAME) {\n\t}';
}
function getRetFunction() {
	return '\tmodule TIPO NOMBRE_FUNCION (TIPO PARAMETER_NAME) {\n\t return RETURN_VALUE }';
}
function getCallFunc() {
	return 'FUNC_NAME(PARAMETER1, PARAMETER2,..);\n';
}
function getRead() {
	return 'read(ID);\n';
}
function getWrite() {
	return 'write(ID);\n';
}
function getIf() {
	return 'if (expresion) {\n\t\n\t}';
}

function getElse() {
	return 'else {\n\n\t}';
}

function getIfElse() {
	return getIf() + '\n\t' + getElse();
}

function getWhileLoop() {
	return 'while (EXPRESION) do {\n\t\t\n\t}';
}
function getForLoop() {
	return 'for ID = EXPRESION to EXPRESION do{\n\t\t\n\t}';
}

$('#codeGenerated').click(function () {
	cursorPosition = $('#codeGenerated').prop('selectionStart');
});

$('#var').click(function () {
	//String del codeGenerated.
	var str = $('#codeGenerated').val();
	//Substring hasta donde está el cursor.
	var strN = str.substring(0, cursorPosition);
	//Substring desde donde está el cursor hasta el final.
	var strRest = str.substring(cursorPosition, str.length);
	//Inserta el código entre los 2 substrings y los pone en el form.
	var strF = strN + '\n\t' + getVariables() + strRest;
	$('#codeGenerated').val(strF);
});
$('#voidFunc').click(function () {
	var str = $('#codeGenerated').val();
	var strN = str.substring(0, cursorPosition);
	var strRest = str.substring(cursorPosition, str.length);
	var strF = strN + '\n' + getVoidFunction() + strRest;
	$('#codeGenerated').val(strF);
});
$('#retFunc').click(function () {
	var str = $('#codeGenerated').val();
	var strN = str.substring(0, cursorPosition);
	var strRest = str.substring(cursorPosition, str.length);
	var strF = strN + '\n' + getRetFunction() + strRest;
	$('#codeGenerated').val(strF);
});
$('#callFunc').click(function () {
	var str = $('#codeGenerated').val();
	var strN = str.substring(0, cursorPosition);
	var strRest = str.substring(cursorPosition, str.length);
	var strF = strN + '\n' + getCallFunc() + strRest;
	$('#codeGenerated').val(strF);
});
$('#if').click(function () {
	//String del codeGenerated.
	var str = $('#codeGenerated').val();
	//Substring hasta donde está el cursor.
	var strN = str.substring(0, cursorPosition);
	//Substring desde donde está el cursor hasta el final.
	var strRest = str.substring(cursorPosition, str.length);
	//Inserta el código entre los 2 substrings y los pone en el form.
	var strF = strN + '\n\t' + getIf() + strRest;
	$('#codeGenerated').val(strF);
});

$('#else').click(function () {
	var str = $('#codeGenerated').val();
	var strN = str.substring(0, cursorPosition);
	var strRest = str.substring(cursorPosition, str.length);
	var strF = strN + '\n\t' + getElse() + strRest;
	$('#codeGenerated').val(strF);
});

$('#ifelse').click(function () {
	var str = $('#codeGenerated').val();
	var strN = str.substring(0, cursorPosition);
	var strRest = str.substring(cursorPosition, str.length);
	var strF = strN + '\n\t' + getIfElse() + strRest;
	$('#codeGenerated').val(strF);
});

$('#whileloop').click(function () {
	var str = $('#codeGenerated').val();
	var strN = str.substring(0, cursorPosition);
	var strRest = str.substring(cursorPosition, str.length);
	var strF = strN + '\n\t' + getWhileLoop() + strRest;
	$('#codeGenerated').val(strF);
});
$('#forloop').click(function () {
	var str = $('#codeGenerated').val();
	var strN = str.substring(0, cursorPosition);
	var strRest = str.substring(cursorPosition, str.length);
	var strF = strN + '\n\t' + getForLoop() + strRest;
	$('#codeGenerated').val(strF);
});

$('#read').click(function () {
	var str = $('#codeGenerated').val();
	var strN = str.substring(0, cursorPosition);
	var strRest = str.substring(cursorPosition, str.length);
	var strF = strN + '\n' + getRead() + strRest;
	$('#codeGenerated').val(strF);
});
$('#write').click(function () {
	var str = $('#codeGenerated').val();
	var strN = str.substring(0, cursorPosition);
	var strRest = str.substring(cursorPosition, str.length);
	var strF = strN + '\n' + getWrite() + strRest;
	$('#codeGenerated').val(strF);
});
