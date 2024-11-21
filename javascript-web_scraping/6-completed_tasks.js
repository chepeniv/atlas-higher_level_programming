#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

let tasks;
const summary = {};
let completedTasks = [];

request(url, (err, response, body) => {
  if (err) console.log(err);
  else {
    // turn webdata to json
    tasks = JSON.parse(body);
    // extract only completed task
    completedTasks = tasks.filter((item) => item.completed);
    // iterate through each user id
    for (let i = 0; i < 11; i++) {
      // get current user's completed tasks
      let count = completedTasks.filter((item) => item.userId === i);
      // count the completed tasks and if not zero
      // add them to the summary
      count = count.length;
      if (count !== 0) summary[i] = count;
    }
    console.log(summary);
  }
});
