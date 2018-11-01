function hello(evt) {
	var moreButton = $( this );
	// console.log(moreButton.attr("href"));
	// alert("I am hello function. "+moreButton.attr("id"));
	var divID = moreButton.attr("id")+'_moreInfo';
	// console.log(divID)
	// http://api.jquery.com/show/
	$("#"+divID).toggle(400);
	evt.preventDefault();
}

function expandAll(evt) {
	// alert("expanding all");
	$(".expandableDIV").toggle();


}

jQuery(document).ready(function() {
	//the document is ready for lolcat insertion
	// alert("Hello from jQuery");
	$(".moreStyle").click(hello)
	$("#expandAllLink").click(expandAll)
});
