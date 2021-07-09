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
            ...
            # write a test for this route
            response = client.get("/api/new-game")
            json = response.json


            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, "application/json")
            self.assertIsInstance(json["board"], list)
            self.assertIsInstance(json["gameId"], str)
            self.assertTrue(games)

    def test_api_score_word(self):
        """Testing verifying a word"""

        with self.client as client:
            response = client.get("/api/new-game")
            game_id = response.json["gameId"]
            game = games[game_id] # instance of the BoggleGame

            game.board = [['L', 'T', 'E', 'F', 'U'], 
                        ['L', 'O', 'I', 'T', 'H'], 
                        ['R', 'H', 'E', 'E', 'S'], 
                        ['H', 'D', 'B', 'R', 'A'], 
                        ['N', 'G', 'K', 'G', 'U']]

            
            
            import pdb
            pdb.set_trace()
            print("HERE HERE")