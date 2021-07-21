// Alan Baines

'use strict';

document.body.style.backgroundColor = "red";

const index = window.location.href
const home = index.substr(0, index.lastIndexOf("/"))
const wordsLoc = home + "/words.out"

console.log("home", home)
console.log("wordsLoc", wordsLoc)

function shuffle(array) 
{
   for (var index = array.length - 1; index > 0; index--)
   {
      const rnd = Math.floor(Math.random() * (index + 1));

      const swap = array[index];
      array[index] = array[rnd];
      array[rnd] = swap;
   }
}

function capitalize(element,index,array)
{
   const word = element.charAt(0).toUpperCase() + element.slice(1);
   array[index] = word;
}

function randomDigit()
{
   return Math.floor(Math.random()*10);
}

fetch(wordsLoc)
   .then(
      response =>
      {
         console.log(response.status, response.statusText, response.url);

         response.text().then(function (text)
         {
            const words = text.trim().split(/\s+/);
            shuffle(words);
            words.forEach(capitalize);
            console.log(words);

            const magicDiv = document.getElementById("all-the-magic");
            const node = document.createTextNode(words.join(' '));
            magicDiv.appendChild(node);

            document.body.style.backgroundColor = "orange";
         })
      })
   .catch(error =>
   {
      console.log(error);
   })

