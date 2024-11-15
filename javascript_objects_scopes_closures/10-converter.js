#!/usr/bin/node

exports.converter = function (radix) {
  return function basedConverter (number) {
    return number.toString(radix);
  };
};
