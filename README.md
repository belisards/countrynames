# countrynames

[![build](https://github.com/opensanctions/countrynames/actions/workflows/build.yml/badge.svg)](https://github.com/opensanctions/countrynames/actions/workflows/build.yml)

This library helps with the mapping of country names to their respective
two or three letter codes. The idea is
to incorporate common names for countries, and even some limited misspellings,
as they occur in source data.

There is also support for fuzzy matching, which uses a heuristic based on levenshtein distance.

## Features

* **Alternative English names**: Map common alternative names like 'USA', 'U.S.A.', 'America' for United States
* **Common misspellings**: Handle frequent typos like 'Argintina' for Argentina, 'Germny' for Germany
* **Translations**: Support for country names in major languages like 'Deutschland', 'España', 'Italia'
* **Fuzzy matching**: Intelligent matching for variations and minor spelling errors
* **Unicode support**: Handle country names in various scripts and character sets

## Usage

```python
import countrynames

# Standard names
assert 'DE' == countrynames.to_code('Germany')
assert 'US' == countrynames.to_code('United States')

# Alternative English names
assert 'US' == countrynames.to_code('USA')
assert 'US' == countrynames.to_code('U.S.A.')
assert 'US' == countrynames.to_code('America')
assert 'US' == countrynames.to_code('United States of America')
assert 'GB' == countrynames.to_code('UK')
assert 'GB' == countrynames.to_code('Britain')

# Common misspellings
assert 'AR' == countrynames.to_code('Argintina')  # Argentina
assert 'US' == countrynames.to_code('Untied States')  # United States
assert 'DE' == countrynames.to_code('Germny')  # Germany

# Enhanced translations
assert 'DE' == countrynames.to_code('Deutschland')
assert 'ES' == countrynames.to_code('España')
assert 'IT' == countrynames.to_code('Italia')
assert 'FR' == countrynames.to_code('République française')

# Fuzzy matching for more variations
assert 'DE' == countrynames.to_code('Bundesrepublik Deutschlan', fuzzy=True)

# Three-letter codes
assert 'DEU' == countrynames.to_code_3('Germany')
assert 'USA' == countrynames.to_code_3('USA')
```

## Non-standard country codes

* ``XK`` or ``XKX`` - Kosovo
* ``EU`` or ``EUU`` - European Union

For some dissolved countries (e.g. `SUHH` for Soviet Union) and sub-regions
(e.g. `GB-SCT` for Scotland) special codes are defined and returned from both
`to_code` and `to_code_3`.

## How to release

```sh
make test compile
git commit countrynames/data.py -m "update data.py"
bump2version --verbose patch
git push --tags && git push origin main
```
