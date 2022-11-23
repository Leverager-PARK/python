from selenium import webdriver
driver = webdriver.Chrome()
url = 'https://accounts.hancom.com/oauth2/authorize?client_id=5xusimMCZbLJQIfLl06i&redirect_uri=https%3A%2F%2Fwww.hancomdocs.com%2Flogin&response_type=code&scope=hancomOauth%3Awrite+hancomOauth%3Aread&state=eyJ0IjoiMTY2OTA3NDU5NzkwNyIsInJlZGlyZWN0IjoiL215ZHJpdmUvc2hhcmVzIn0%3D&token=true'
driver.get(url)

while(True):
    pass




ssss