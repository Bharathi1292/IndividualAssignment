def isliving(Country, Countrycode, TelephoneCountryCode, Telephone, Birthday, ConsentToContact):
    if Country == "Sverige" and ConsentToContact == "True":
        return True
    return False