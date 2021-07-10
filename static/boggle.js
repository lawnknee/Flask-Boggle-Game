"use strict";

const $playedWords = $("#words");
const $form = $("#newWordForm");
const $wordInput = $("#wordInput");
const $message = $(".msg");
const $table = $("table");

let gameId;


/** Start */

async function start() {
  let response = await axios.post("/api/new-game");
  gameId = response.data.gameId;
  let board = response.data.board;

  console.log(response)
  displayBoard(board);
}

/** Display board */

function displayBoard(board) {
  $table.empty();
  let $tbody = $("<tbody></tbody>");

  for (let row of board) {
    let $row = $("<tr></tr>");

    for (let letter of row) {
      let $cell = $(`<td>${letter}</td>`);
      $row.append($cell);
    }
    $tbody.append($row);
  }

  $table.append($tbody);
}

// need conductor function
$form.on("submit", handleSubmit);


// data
async function checkWord(word) {
  let response = await axios.post("/api/score-word", { gameId: gameId, word: word });

  console.log(response.data)
}

// UI
function displayResult(result) {

}


// conductor
async function handleSubmit(evt) {
  evt.preventDefault()
  let word = $wordInput.val().toUpperCase();
  let response = await checkWord(word);
  // displayResult(result);
}

start();