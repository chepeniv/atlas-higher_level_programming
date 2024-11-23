#!/usr/bin/node
/* global $ */

// add the class red to <header> content to #ff0000 when
// div#red_header is clicked
// cannot use document.querySelector
// use the jquery api
$('div#red_header').click(() => {
  $('header').addClass('red');
});
