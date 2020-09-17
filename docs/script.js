// Alan Baines

'use strict';

document.body.style.backgroundColor = "red";

const index = window.location.href
const home = index.substr(0, index.lastIndexOf("/"))
const wordsLoc = home + "/words.out"

console.log("home", home)
console.log("wordsLoc", wordsLoc)

fetch(wordsLoc)
   .then(
      response =>
      {
         console.log(response.status, response.statusText, response.url);

         response.text().then(function (text)
         {
            const words = text.trim().split(/\s+/);
            console.log(words);

            const magicDiv = document.getElementById("all-the-magic");
            const node = document.createTextNode(text);
            magicDiv.appendChild(node);

            document.body.style.backgroundColor = "orange";
         })
      })
   .catch(error =>
   {
      console.log(error);
   })

