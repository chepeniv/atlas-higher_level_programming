#!/usr/bin/node
/* global $ */

// toggle the class of <header> when div#toggle_header is clicked
// <header> must have exactly one class, either red or green
// cannot use document.querySelector
// use the jquery api
$('div#toggle_header').click(() => {
  const header = $('header');
  header.toggleClass('red');
  header.toggleClass('green');
});
