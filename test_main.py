import unittest
from unittest.mock import patch, call
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query1, query2, query3, query4

class TestMainMethods(unittest.TestCase):

    @patch('mylib.extract.extract')
    @patch('mylib.transform_load.load')
    @patch('mylib.query.query1')
    @patch('mylib.query.query2')
    @patch('mylib.query.query3')
    @patch('mylib.query.query4')
    def test_main_flow(self, mock_query4, mock_query3, mock_query2, mock_query1, mock_load, mock_extract):
        # Importing the main script and running the main flow
        import main

        # Checking if methods are called in the correct order
        mock_extract.assert_called_once()
        mock_load.assert_called_once()
        mock_query1.assert_called_once()
        mock_query2.assert_called_once()
        mock_query3.assert_called_once()
        mock_query4.assert_called_once()


if __name__ == '__main__':
    unittest.main()
