#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(1);
const movie = 'https://swapi-api.hbtn.io/api/films/' + args[1];

const resp = (urls = [], names = []) => {
  if (urls.length > 0) {
    request(urls[0], (error, response, body) => {
      if (error) {
        console.log(error);
      } else {
        names.push(JSON.parse(body).name);
        urls.shift();
        return resp(urls, names);
      }
    });
  } else {
    for (const name of names) {
      console.log(name);
    }
  }
};

request(movie, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    const lists = [];
    resp(characters, lists);
  }
});
