#!/usr/bin/node

// update the color of <header> content to #ff0000 when
// div#red_header is clicked
// cannot use document.querySelector
// use the jquery api
$('div#red_header').click(() => {
  $('header').css('color', '#ff0000');
});
