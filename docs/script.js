// Alan Baines

'use strict';

document.body.style.backgroundColor = "orange";

const index = window.location.href
const home = index.substr(0, index.lastIndexOf("/"))
const wordsLoc = home + "/words.out"

console.log("home", home)
console.log("wordsLoc", wordsLoc)

fetch(wordsLoc)
   .then(
      response => {
         console.log(response);
         console.log(response.body);
         response.text().then(function (text) {
            console.log(text);
         })
      })
   .catch(error => {
      console.log(error);
   })

