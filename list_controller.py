import os
from os import path
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def main ():
    print('*************************************************************')
    print('list_controller.exe was developed in MatCol by @CamiloQuiceno')
    print('*************************************************************')
    print('************** Welcome to List Controller V1.0 **************')
    print('*************************************************************')
    print('*************************************************************')
    
    WEBSITE = "https://m3s.materialise.net"
    operation_time = int(input('Input operation time (in minutes): '))

    if not os.path.exists('.\\imgs'):
        os.mkdir('.\\imgs')
        print('Folder imgs created')

    date = datetime.datetime.now()
    today = '%s-%s-%s' % (date.day, date.month, date.year)

    if not os.path.exists('.\\imgs\\%s' % (today)):
        os.mkdir('.\\imgs\\%s' % (today))
        print('Folder: %s was created' % (today))
        
    print('Your images will be stored at folder: %s' % (today))

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(WEBSITE)

    for i in range(operation_time + 1):

        time.sleep(40)

        if i % 5 == 0:  
            date = datetime.datetime.now()
            name_image = 'Date %s.%s' % (date.hour, date.minute)

            el = driver.find_element(By.TAG_NAME, 'html')
            driver.execute_script("document.body.style.zoom='60%'")
            el.screenshot('.\\imgs\\%s\\%s.png' % (today,name_image))
            driver.refresh()

            print("Say Cheese, Image: %s" % (name_image))

        else:
            driver.execute_script("window.scrollTo(0, 5000);")
            driver.find_element(By.TAG_NAME, 'html').click()
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, -5000);")
            time.sleep(2)
    
    driver.close()

if __name__ == '__main__':
    main()