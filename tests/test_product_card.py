import os
import sys
import unittest
from unittest.mock import patch

# Ensure the package root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from streamlit_product_card import product_card


class ProductCardTestCase(unittest.TestCase):
    @patch("streamlit_product_card._component", return_value={"clickEventId": None})
    def test_product_card_returns_false_without_click(self, mock_component):
        result = product_card(product_name="Sample", key="test_card")
        self.assertFalse(result)
        mock_component.assert_called_once()


if __name__ == "__main__":
    unittest.main()
