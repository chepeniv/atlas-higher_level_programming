#!/usr/bin/node

// fetch from https://hellosalut.stefanbohacek.dev/?lang=fr
// extract hello and insert its value into div#hello
// document.querySelector is not allowed
// use the jquery api
// script must work when imported from head
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(url, (data, stat) => {
  console.log(data);
  $('div#hello').text(data.hello);
  $('div#hello').attr('translation', data.code);
});
