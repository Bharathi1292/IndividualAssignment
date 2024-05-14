import unittest
from check import isliving

class TestIsLiving(unittest.TestCase):
    def test_when_Country_is_Sverige_and_ConsentToContact_is_True_should_return_True(self):
        # ARRANGE
        Country = "Sverige"
        CountryCode = "SE"
        TelephoneCountryCode = "+46"
        Telephone = "123456789"
        Birthday = "2000-01-01"
        ConsentToContact = "True"
        # ACT
        result = isliving(Country, CountryCode, TelephoneCountryCode, Telephone, Birthday, ConsentToContact)
        # ASSERT
        self.assertTrue(result)

    def test_when_Country_is_not_Sverige_or_ConsentToContact_is_False_should_return_False(self):
        # ARRANGE
        Country = "Norway"
        CountryCode = "NO"
        TelephoneCountryCode = "+47"
        Telephone = "987654321"
        Birthday = "2000-01-01"
        ConsentToContact = "False"
        # ACT
        result = isliving(Country, CountryCode, TelephoneCountryCode,Telephone,Birthday, ConsentToContact)
        # ASSERT
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()