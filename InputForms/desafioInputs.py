import time
from selenium import webdriver
import pandas as pd


dados = pd.read_excel('challenge.xlsx')

driver = webdriver.Firefox(executable_path='C:/tools/selenium/geckodriver.exe')
driver.get('http://www.rpachallenge.com')

StartButton = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button")
StartButton.click()

for i in range(10):

    FirstNameInput= driver.find_element_by_xpath("//*[contains(text(),'First Name')]//following-sibling::input")
    FirstNameInput.send_keys(dados.loc[i, :][0])

    LastNameInput= driver.find_element_by_xpath("//*[contains(text(),'Last Name')]//following-sibling::input")
    LastNameInput.send_keys(dados.loc[i, :][1])

    CompanyNameInput= driver.find_element_by_xpath("//*[contains(text(),'Company Name')]//following-sibling::input")
    CompanyNameInput.send_keys(dados.loc[i, :][2])

    RoleNameInput= driver.find_element_by_xpath("//*[contains(text(),'Role in Company')]//following-sibling::input")
    RoleNameInput.send_keys(dados.loc[i, :][3])

    AddressNameInput= driver.find_element_by_xpath("//*[contains(text(),'Address')]//following-sibling::input")
    AddressNameInput.send_keys(dados.loc[i, :][4])

    EmailInput= driver.find_element_by_xpath("//*[contains(text(),'Email')]//following-sibling::input")
    EmailInput.send_keys(dados.loc[i, :][5])

    PhoneInput= driver.find_element_by_xpath("//*[contains(text(),'Phone Number')]//following-sibling::input")
    PhoneInput.send_keys(int(dados.loc[i, :][6]))

    SubmitButton = driver.find_element_by_xpath("/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input")
    SubmitButton.click()


time.sleep(3)
driver.close()
