#!/usr/bin/node

exports.converter = function (radix) {
	return function based_converter(number) {
		return number.toString(radix);
	}
};
