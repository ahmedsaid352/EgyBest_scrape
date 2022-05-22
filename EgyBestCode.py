from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


print("what is your Choice\n\n")
print("1) Whatching a Film\n\n")
print("2) Whatching a serie \n\n")
choice =int(input("your choice\n\n").strip())


if choice == 1 : 
    film_name = input("what is the name of the film?\n\n")
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://www.google.com/")
    browser.implicitly_wait(3)
    browser.find_element_by_xpath("//input[@name='q']").send_keys(f"{film_name} site egybest")
    act = ActionChains(browser)
    act.send_keys(Keys.ENTER).perform()
    browser.implicitly_wait(3)
    browser.find_element_by_css_selector("#rso a:first-of-type").click()
    browser.implicitly_wait(3)
    if True :
        browser.find_element_by_xpath("//a[@class='NotificationIgnore api']").click()
    else :
        pass     
    
    browser.implicitly_wait(3)
    browser.maximize_window()
    handles = browser.window_handles
    egybest_title = "EgyBest"
    for handle in handles :
        browser.switch_to.window(handle)
        title = browser.title
        if egybest_title in title :
            pass
        else :
     
           browser.close() 
    handles = browser.window_handles

    for handle1 in handles :
       browser.switch_to.window(handle1)
       title = browser.title
       if egybest_title in title :
           egybest_handle = handle1
       
       
           
        
    
    browser.switch_to.window(egybest_handle)
    browser.implicitly_wait(7)
    browser.find_element_by_xpath("//iframe[@class='auto-size']").click()
    browser.implicitly_wait(3)
    handles = browser.window_handles
    for handle3 in handles :
        browser.switch_to.window(handle3)
        title = browser.title
        if egybest_title in title :
            pass
        else :
     
           browser.close() 

    browser.switch_to.window(egybest_handle)  
    browser.implicitly_wait(7) 
    browser.find_element_by_xpath("//iframe[@class='auto-size']").click()
    browser.implicitly_wait(3)
    handles = browser.window_handles
    for handle4 in handles :
        browser.switch_to.window(handle4)
        title = browser.title
        if egybest_title in title :
            pass
        else :
     
           browser.close() 

    browser.switch_to.window(egybest_handle)  
    browser.implicitly_wait(7)
    act.double_click(browser.find_element_by_xpath("//iframe[@class='auto-size']")).perform()


    # browser.find_element_by_css_selector(".auto-size #video .vjs-control-bar .vjs-fullscreen-control vjs-control vjs-button").click()

    # browser.find_element_by_xpath("//iframe[@class='auto-size']").click()
    # browser.implicitly_wait(1)
    # handles = browser.window_handles
    # for handle4 in handles :
    #     browser.switch_to.window(handle4)
    #     title = browser.title
    #     if egybest_title in title :
    #         pass
    #     else :
     
    #        browser.close() 




    # browser.switch_to.window(egybest_handle)  
    # browser.implicitly_wait(3)
    # browser.find_element_by_xpath("//iframe[@class='auto-size']").click()
    # browser.implicitly_wait(3)
    # handles = browser.window_handles
    # for handle4 in handles :
    #     browser.switch_to.window(handle4)
    #     title = browser.title
    #     if egybest_title in title :
    #         pass
    #     else :
     
    #        browser.close() 

    # browser.switch_to.window(egybest_handle)  
    # browser.implicitly_wait(3)

    # browser.find_element_by_css_selector(".vjs-control-bar button:last-of-type").click()
elif choice == 2 :
    serie = input("what is the name of the serie?\n").strip().lower()
    serie = serie.replace(" ", "-")
    season = input("which season you whant?\n").strip()
    episode = input("which episode you whant?\n").strip()
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(f"https://tone.egybest.xyz/episode/{serie}-season-{season}-ep-{episode}/")
    browser.implicitly_wait(3)
    browser.find_element_by_xpath("//a[@class='NotificationIgnore api']").click()
    browser.implicitly_wait(3)
    browser.maximize_window()
    handles = browser.window_handles
    egybest_title = "EgyBest"
    for handle in handles :
        browser.switch_to.window(handle)
        title = browser.title
        if egybest_title in title :
            pass
        else :
     
           browser.close() 
         
    handles = browser.window_handles

    for handle1 in handles :
       browser.switch_to.window(handle1)
       title = browser.title
       if egybest_title in title :
           egybest_handle = handle1
       
       
           
        
    
    browser.switch_to.window(egybest_handle)
    browser.find_element_by_xpath("//iframe[@class='auto-size']").click()
    browser.implicitly_wait(3)
    handles = browser.window_handles
    for handle3 in handles :
        browser.switch_to.window(handle3)
        title = browser.title
        if egybest_title in title :
            pass
        else :
     
           browser.close() 

    browser.switch_to.window(egybest_handle)  
    browser.implicitly_wait(3) 
    browser.find_element_by_xpath("//iframe[@class='auto-size']").click()
    browser.implicitly_wait(3)
    handles = browser.window_handles
    for handle4 in handles :
        browser.switch_to.window(handle4)
        title = browser.title
        if egybest_title in title :
            pass
        else :
     
           browser.close() 

    browser.switch_to.window(egybest_handle)  
    browser.implicitly_wait(7)
    act = ActionChains(browser)
    


    act.double_click(browser.find_element_by_xpath("//iframe[@class='auto-size']")).perform()        


