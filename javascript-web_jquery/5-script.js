#!/usr/bin/node
/* global $ */

// add <li>Item</li> to UL.my_list whenever div#add_item is clicked
// cannot use document.querySelecto
// use the jquery api
$('div#add_item').click(() => {
  $('<li>Item</li>').appendTo('ul.my_list');
});
