#!/usr/bin/node

exports.nbOccurences = function (list, target) {
  let occurs = 0;
  let i = 0;
  while (i < list.length) {
    if (list[i] === target) {
      occurs++;
    }
    i++;
  }
  return occurs;
};
