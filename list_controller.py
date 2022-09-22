import os
from os import path
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def capture_function(page_number,driver, today, name_image):
    driver.execute_script("window.scrollTo(0, 200);")
    driver.get_screenshot_as_file(f'.\\imgs\\{today}\\{page_number}\\{name_image}.png')
    print(f"Say Cheese, Image page {page_number}: {name_image}")

def print_welcome():
    print('*************************************************************')
    print('list_controller.exe was developed in MatCol by @Camilo.Quiceno')
    print('*************************************************************')
    print('************** Welcome to List Controller V2.0 **************')
    print('*************************************************************')
    print('*************************************************************')


def main ():
    
    print_welcome()
    
    WEBSITE = "https://m3s.materialise.net"
    LINK_PAGE_TWO = '//*[@id="maincontent"]/ng-component/div/div[2]/div[2]/div[2]/form/div[2]/pagination/div/ul/li[4]/a'
    HTML_XPATH = "/html"

    operation_time = int(input('Input operation time (in minutes): '))

    if not os.path.exists('.\\imgs'):
        os.mkdir('.\\imgs')
        print('Folder imgs created')

    date = datetime.datetime.now()
    today = '%s-%s-%s' % (date.day, date.month, date.year)

    if not os.path.exists('.\\imgs\\%s' % (today)):
        os.mkdir('.\\imgs\\%s' % (today))
        os.mkdir('.\\imgs\\%s\\1' % (today))
        os.mkdir('.\\imgs\\%s\\2' % (today))
        print('Folder: %s was created' % (today))

    print('Your images will be stored at folder: %s' % (today))

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(WEBSITE)

    time.sleep(20)

    for i in range(operation_time + 1):

        time.sleep(30)

        if i % 5 == 0:  

            date = datetime.datetime.now()
            name_image = 'Date %s.%s' % (date.hour, date.minute)

            capture_function(1,driver,today,name_image)

            try:
                driver.find_element(By.XPATH, LINK_PAGE_TWO).click()
                time.sleep(20)
            
                capture_function(2,driver,today,name_image)

            except:
                print('Page 2 is not available')
                time.sleep(20)

            driver.refresh()

        else:
            driver.execute_script("window.scrollTo(0, 5000);")
            driver.find_element(By.TAG_NAME, 'html').click()
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, -5000);")
            time.sleep(2)
    
    driver.close()

if __name__ == '__main__':
    main()