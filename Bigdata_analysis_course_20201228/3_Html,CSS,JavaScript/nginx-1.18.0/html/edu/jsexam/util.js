function write(content, tag) {                          // 자주 사용하는 함수를 모아놓은 것
	document.write("<"+tag+">"+content+"</"+tag+">");	
}
function hr() {
	document.write("<hr>");
}
function writeColor(content, tag, color) {
	document.write("<"+tag+" style='color:"+color+"'>"+
			  content+"</"+tag+">");	
}
function writeNewLine(content) {
	document.write(content+"<br>");	
}