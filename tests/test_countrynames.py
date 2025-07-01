from countrynames import to_code, to_code_3


def test_to_code():
    assert to_code("Germany") == "DE"
    assert to_code("UK") == "GB"
    assert to_code("North Macedonia") == "MK"
    assert to_code("Nothing") is None


def test_to_code_3():
    assert to_code_3("Germany") == "DEU"
    assert to_code_3("UK") == "GBR"
    assert to_code_3("Nothing") is None


def test_unicode():
    assert to_code(u"Российская Федерация") == "RU"


def test_fuzzy_matching():
    # assert to_code("Rossiyskaya Federacia", fuzzy=True) == "RU"
    assert to_code("Falklands Islands", fuzzy=True) == "FK"
    assert to_code("TGermany", fuzzy=True) == "DE"
    assert to_code_3("State of Palestine", fuzzy=True) == "PSE"


def test_non_standard_codes():
    assert to_code("European Union") == "EU"
    assert to_code_3("European Union") == "EUU"
    assert to_code("Kosovo") == "XK", to_code("Kosovo")
    assert to_code_3("Kosovo") == "XKX"


def test_GB():
    assert to_code("Scotland") == "GB-SCT"
    assert to_code("Wales") == "GB-WLS"
    assert to_code("Northern Ireland") == "GB-NIR"
    assert to_code("Northern Ireland", fuzzy=True) == "GB-NIR"
    text = "United Kingdom of Great Britain and Northern Ireland"
    assert to_code(text) == "GB"
    text = "United Kingdom of Great Britain and Northern Ireland"
    assert to_code(text, fuzzy=True) == "GB"


def test_alternative_english_names():
    """Test alternative English names for countries"""
    # US alternatives
    assert to_code("United States of America") == "US"
    assert to_code("USA") == "US"
    assert to_code("U.S.A.") == "US"
    assert to_code("U.S.") == "US"
    assert to_code("America") == "US"
    assert to_code("U.S. of A.") == "US"
    assert to_code("US of A") == "US"
    
    # UK alternatives
    assert to_code("UK") == "GB"
    assert to_code("U.K.") == "GB"
    assert to_code("Britain") == "GB"
    assert to_code("Great Britain") == "GB"
    assert to_code("England") == "GB"
    assert to_code("British Isles") == "GB"


def test_common_misspellings():
    """Test mapping of common misspellings to correct country codes"""
    # Argentina misspellings
    assert to_code("Argintina") == "AR"
    assert to_code("Argentena") == "AR"
    assert to_code("Argentinia") == "AR"
    assert to_code("Argantina") == "AR"
    
    # US misspellings
    assert to_code("Untied States") == "US"
    assert to_code("United Staes") == "US"
    assert to_code("United State") == "US"
    assert to_code("Amercia") == "US"
    
    # Germany misspellings
    assert to_code("Germny") == "DE"
    assert to_code("Gremany") == "DE"
    
    # Spain misspellings
    assert to_code("Span") == "ES"
    assert to_code("Spian") == "ES"
    
    # France misspellings
    assert to_code("Frace") == "FR"
    assert to_code("Frannce") == "FR"
    
    # Italy misspellings
    assert to_code("Itally") == "IT"
    assert to_code("Itlay") == "IT"
    
    # UK misspellings
    assert to_code("Untied Kingdom") == "GB"
    assert to_code("Britian") == "GB"


def test_enhanced_translations():
    """Test enhanced translations for major languages"""
    # German translations
    assert to_code("Deutschland") == "DE"
    assert to_code("Bundesrepublik Deutschland") == "DE"
    
    # Spanish translations
    assert to_code("España") == "ES"
    assert to_code("Reino de España") == "ES"
    
    # French translations
    assert to_code("République française") == "FR"
    
    # Italian translations
    assert to_code("Italia") == "IT"
    assert to_code("Repubblica Italiana") == "IT"


def test_three_letter_codes_enhanced():
    """Test that enhanced names also work with 3-letter codes"""
    assert to_code_3("USA") == "USA"
    assert to_code_3("Deutschland") == "DEU"
    assert to_code_3("España") == "ESP"
    assert to_code_3("Italia") == "ITA"
    assert to_code_3("Argintina") == "ARG"
