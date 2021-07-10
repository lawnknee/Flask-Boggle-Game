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
$form.on("submit", checkWord);


// data
async function checkWord() {
  let word = $wordInput.val().toUpperCase();
  debugger;
  let response = await axios.post("/api/score-word", { data: {gameId: gameId, word: word }});
  debugger;
  return response.data
}

// UI
function displayResult(result) {

}


// conductor
async function handleSubmit() {
  let response = await checkWord();
  displayResult(result);
}

start();