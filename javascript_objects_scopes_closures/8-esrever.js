#!/usr/bin/node

exports.esrever = function (list) {
  let reversed = [];
  for (let i = 0; i < list.length; i++) {
    reversed.push(list[list.length - 1 - i]);
  }
  return reversed;
};
