#!/usr/bin/node

// toggle the class of <header> when div#toggle_header is clicked
// <header> must have exactly one class, either red or green
// cannot use document.querySelector 
// use the jquery api
$('div#toggle_header').click(() => {
  const header = $('header');
  if (header.hasClass('red')) {
    header.removeClass('red');
    header.addClass('green');
  } else {
    header.removeClass('green');
    header.addClass('red');
  }
});
