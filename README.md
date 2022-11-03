# Python - Local Client - 5 second delay between session calls - TimeoutException: Message: timeout: Timed out receiving message from renderer


## Issue Description:
Using Python Binding for chromedriver (Local Client), navigate to a url ('https://google.com'), wait 5 seconds, then attempt to navigate to a different url ('https://example.com) =>TimeoutException: Message: timeout: Timed out receiving message from renderer
Expected an attempt to navigate to a different url successfully loads that webpage


## Steps to reproduce (if relevant, you MUST provide a simplified html page or link to public site):

### Test Repo
https://github.com/adambonsu/selenium-python-net-read-timeout

### Set up test environment:
```
brew install openssl readline sqlite3 xz zlib
curl https://pyenv.run | bash
pyenv install 3.11.0
pyenv global 3.11.0
python -m test
pip install selenium
pip install webdriver-manager
```

### Execute Test:
* Loads a chrome browser and visits google.com
* Delay of 5 seconds (by default) between url calls
* Attempts to visit example.com => TimeoutException
```
python test_selenium_chrome.py
```

### Environment:
* Browser: Chrome Version 107.0.5304.87
* Chromedriver: ChromeDriver 107.0.5304.62 (1eec40d3a5764881c92085aaee66d25075c159aa-refs/branch-heads/5304@{#942})
* Language Bindings: Python
* Python: 3.11.0
* OS: macOS Monterey version 12.5
  - Processor 2.9 GHz Quad-Core Intel Core i7
  - Memory 16GB 2133 MHz LPDDR3
  - Graphics Intel HD Graphics 630 1536 MB


### Short, Self Contained, Correct (Compilable), Example
test_selenium_chrome.py
```
from selenium import webdriver
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://google.com")
time.sleep(5)
driver.get("https://example.com")
driver.quit()
```




## Chromedriver log:
```
C02W63XEHTD6:selenium-python-net-read-timeout adambons$ python test_selenium_chrome.py 
/Users/adambons/Documents/workspace/itv/selenium-python-net-read-timeout/test_selenium_chrome.py:6: DeprecationWarning: executable_path has been deprecated, please pass in a Service object
  driver = webdriver.Chrome(PATH)
Traceback (most recent call last):
  File "/Users/adambons/Documents/workspace/itv/selenium-python-net-read-timeout/test_selenium_chrome.py", line 9, in <module>
    driver.get("https://example.com")
  File "/Users/adambons/.pyenv/versions/3.11.0/lib/python3.11/site-packages/selenium/webdriver/remote/webdriver.py", line 441, in get
    self.execute(Command.GET, {'url': url})
  File "/Users/adambons/.pyenv/versions/3.11.0/lib/python3.11/site-packages/selenium/webdriver/remote/webdriver.py", line 429, in execute
    self.error_handler.check_response(response)
  File "/Users/adambons/.pyenv/versions/3.11.0/lib/python3.11/site-packages/selenium/webdriver/remote/errorhandler.py", line 243, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.TimeoutException: Message: timeout: Timed out receiving message from renderer: 600.000
  (Session info: chrome=107.0.5304.87)
Stacktrace:
0   chromedriver                        0x0000000107f6e2c8 chromedriver + 4752072
1   chromedriver                        0x0000000107eee463 chromedriver + 4228195
2   chromedriver                        0x0000000107b51b18 chromedriver + 441112
3   chromedriver                        0x0000000107b3bf4d chromedriver + 352077
4   chromedriver                        0x0000000107b3bca2 chromedriver + 351394
5   chromedriver                        0x0000000107b3ab0d chromedriver + 346893
6   chromedriver                        0x0000000107b3aec2 chromedriver + 347842
7   chromedriver                        0x0000000107b3a351 chromedriver + 344913
8   chromedriver                        0x0000000107b48ec0 chromedriver + 405184
9   chromedriver                        0x0000000107b3a306 chromedriver + 344838
10  chromedriver                        0x0000000107b3b8fe chromedriver + 350462
11  chromedriver                        0x0000000107b3ab0d chromedriver + 346893
12  chromedriver                        0x0000000107b3aec2 chromedriver + 347842
13  chromedriver                        0x0000000107b3a351 chromedriver + 344913
14  chromedriver                        0x0000000107b45faa chromedriver + 393130
15  chromedriver                        0x0000000107b3a306 chromedriver + 344838
16  chromedriver                        0x0000000107b3b8fe chromedriver + 350462
17  chromedriver                        0x0000000107b3ab0d chromedriver + 346893
18  chromedriver                        0x0000000107b3aec2 chromedriver + 347842
19  chromedriver                        0x0000000107b3a351 chromedriver + 344913
20  chromedriver                        0x0000000107b4152c chromedriver + 374060
21  chromedriver                        0x0000000107b3a306 chromedriver + 344838
22  chromedriver                        0x0000000107b3b8fe chromedriver + 350462
23  chromedriver                        0x0000000107b3ab0d chromedriver + 346893
24  chromedriver                        0x0000000107b3aec2 chromedriver + 347842
25  chromedriver                        0x0000000107b3a351 chromedriver + 344913
26  chromedriver                        0x0000000107b34260 chromedriver + 320096
27  chromedriver                        0x0000000107b3a306 chromedriver + 344838
28  chromedriver                        0x0000000107b39872 chromedriver + 342130
29  chromedriver                        0x0000000107b39a3d chromedriver + 342589
30  chromedriver                        0x0000000107b39d37 chromedriver + 343351
31  chromedriver                        0x0000000107b39ced chromedriver + 343277
32  chromedriver                        0x0000000107b5325b chromedriver + 447067
33  chromedriver                        0x0000000107bc7768 chromedriver + 923496
34  chromedriver                        0x0000000107bafb33 chromedriver + 826163
35  chromedriver                        0x0000000107b809fd chromedriver + 633341
36  chromedriver                        0x0000000107b82051 chromedriver + 639057
37  chromedriver                        0x0000000107f3b30e chromedriver + 4543246
38  chromedriver                        0x0000000107f3fa88 chromedriver + 4561544
39  chromedriver                        0x0000000107f476df chromedriver + 4593375
40  chromedriver                        0x0000000107f408fa chromedriver + 4565242
41  chromedriver                        0x0000000107f162cf chromedriver + 4391631
42  chromedriver                        0x0000000107f5f5b8 chromedriver + 4691384
43  chromedriver                        0x0000000107f5f739 chromedriver + 4691769
44  chromedriver                        0x0000000107f7581e chromedriver + 4782110
45  libsystem_pthread.dylib             0x00007ff81cb834e1 _pthread_start + 125
46  libsystem_pthread.dylib             0x00007ff81cb7ef6b thread_start + 15

C02W63XEHTD6:selenium-python-net-read-timeout adambons$ 
```