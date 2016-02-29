$(document).ready(function () {
    size_li = $("#myList li").size();
    x=2;
    $('#myList li:lt('+x+')').show();
    $('#loadMore').click(function () {
        x= (x+2 <= size_li) ? x+2 : size_li;
        $('#myList li:lt('+x+')').show();
    });
    $('#showLess').click(function () {
        x=(x-2<0) ? 2 : x-2;
        $('#myList li').not(':lt('+x+')').hide();
    });
});