## Set up test environment
```
brew install openssl readline sqlite3 xz zlib
curl https://pyenv.run | bash
pyenv install 3.11.0
pyenv global 3.11.0
python -m test
pip install selenium
```

## Execute Selenium test script
```
python test_selenium_chrome.py
```