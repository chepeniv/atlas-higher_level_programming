#!/usr/bin/node
/* global $ */

// update the content of <header> to 'New Header!!!'
// whenever div#update_header is clicked
// cannot use document.querySelecto
// must use the jquery api
$('div#update_header').click(() => {
  $('header').text('New Header!!!');
});
