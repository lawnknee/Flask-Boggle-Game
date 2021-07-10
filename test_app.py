from unittest import TestCase

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get('/')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<button class="word-input-btn">Go</button>', html)

    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:
            response = client.post("/api/new-game")
            game = response.json


            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, "application/json")
            self.assertIsInstance(game["board"], list)
            self.assertIsInstance(game["gameId"], str)
            self.assertIn(game["gameId"], games)

    def test_api_score_word(self):
        """Testing verifying a word"""

        with self.client as client:
            response = client.post("/api/new-game")
            game_id = response.json["gameId"]
            game = games[game_id] # instance of the BoggleGame

            game.board = [['X', 'X', 'X', 'X', 'X'], 
                          ['L', 'O', 'I', 'T', 'X'], 
                          ['X', 'X', 'X', 'E', 'X'], 
                          ['X', 'X', 'X', 'R', 'X'], 
                          ['X', 'X', 'X', 'X', 'X']]

            # Verifies that a word is not in the dictionary.
            not_on_list = client.post("/api/score-word",
                            json = {
                                'gameId': game_id, 
                                "word": 'AAZ'
                                })
            
            self.assertEqual(not_on_list.json["result"], "not-word")

            # Verifies that a word is in the dictionary but not
            # on the board
            not_on_board = client.post("/api/score-word",
                            json = {
                                'gameId': game_id, 
                                "word": 'KING'
                                })
            
            self.assertEqual(not_on_board.json["result"], "not-on-board")

            # Verifies that a word is in the dictionary and on the board
            valid_word = client.post("/api/score-word",
                            json = {
                                'gameId': game_id, 
                                "word": 'LOITER'
                                })

            self.assertEqual(valid_word.json["result"], "ok")
            
