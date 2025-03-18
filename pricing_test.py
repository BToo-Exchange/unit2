import unittest
from unittest.mock import mock 
from pricing import *



class PricingTestInit(unittest.TestCase):
    def setUp(self):
        
        self.mock_pricing_data = Mock()
        self.mock_tax_calc = Mock()
        self.mock_discount_calc = Mock()
        
        self.service = ProductPricingService(
            self.mock_pricing_data,
            self.mock_tax_calc,
            self.mock_discount_calc
        )
    def test_calculate_final_price_with_taxes_and_discounts(self):
        """Test final price calculation with normal taxes and discounts"""
        self.mock_pricing_data_provider.get_base_price.return_value = 100.0
        self.mock_tax_calculator.calculate_taxes.return_value = 10.0
        self.mock_discount_calculator.calculate_discounts.return_value = 5.0

        result = self.service.calculate_final_price(product_id=1, user_id=42)
        self.assertEqual(result, 105.0)

    def test_calculate_final_price_no_user(self):
            # Arrange
            product_id = "prod123"
            self.mock_pricing_data.get_base_price.return_value = 100.0
            self.mock_tax_calc.calculate_taxes.return_value = 10.0
            self.mock_discount_calc.calculate_discounts.return_value = 20.0
            
            # Act
            result = self.service.calculate_final_price(product_id)
            
            # Assert
            self.assertEqual(result, 90.0)  # 100 + 10 - 20 = 90
            self.mock_pricing_dat


if __name__ == "__main__":
    unittest.main()
