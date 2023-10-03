import json

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# GITHUB: https://github.com/backpackerdeveloper
# Linkedin : https://www.linkedin.com/in/shubhamtripz/
# Made with ♥ by Shubham

# Configure Chrome to run in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")

# Ask for user input for Consumer No. and Office Address
consumer_no = input("Enter the Consumer No.: ")
office_address_value = input("Enter the Office Address value: ")

# Create a Selenium webdriver with headless mode
driver = webdriver.Chrome(options=chrome_options)  # Use ChromeOptions

driver.get("https://www.jseb.co.in/WSS/WSSUI/frmpwlEnergyBillPayment.aspx")

# Wait for the page to load and the JavaScript to execute
driver.implicitly_wait(10)

# Select the "Consumer No." radio button
consumer_radio_button = driver.find_element(By.ID, "ctl00_cphpwl_rbtAccountNumber")
consumer_radio_button.click()

# Enter the Consumer No. in the input box
consumer_input = driver.find_element(By.ID, "ctl00_cphpwl_txtConsumerNumber")
consumer_input.send_keys(consumer_no)

# Select the Office Address from the dropdown menu
office_address_dropdown = driver.find_element(By.ID, "ctl00_cphpwl_ddlOfficeAddress")
for option in office_address_dropdown.find_elements(By.TAG_NAME, 'option'):
    if option.get_attribute("value") == office_address_value:
        option.click()
        break

# Click the "Get Bill Details" button using JavaScript
driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "ctl00_cphpwl_btnGetBillDetail"))

# Wait for the page to redirect and load
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "ctl00_cphpwl_lblConsumerName")))

# Extract data from the redirected page
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")

# Find the required data and store it in a dictionary
data = {
    "Consumer Name": soup.find("span", {"id": "ctl00_cphpwl_lblConsumerName"}).text.strip(),
    "Bill No.": soup.find("span", {"id": "ctl00_cphpwl_lblBillNo"}).text.strip(),
    "KNo": soup.find("span", {"id": "ctl00_cphpwl_lblKNo1"}).text.strip(),
    "Bill Month": soup.find("span", {"id": "ctl00_cphpwl_lblBillMonth"}).text.strip(),
    "Due Date": soup.find("span", {"id": "ctl00_cphpwl_lblDueDate"}).text.strip(),
    "Bill Amount (Rs.)": soup.find("span", {"id": "ctl00_cphpwl_lblBilledAmount"}).text.strip(),
    "Amount Payble (Rs.)": soup.find("span", {"id": "ctl00_cphpwl_lblAmountPayble"}).text.strip(),
}

# Close the browser
driver.quit()

# Convert the data to JSON format
output_json = json.dumps(data, indent=4)

# Print the JSON data
print(output_json)

"""

 here below values are for Areas; so select your area value from value and input it when Office Address value will asked: 

Jab Office Address value enter krne ka option aaye tab, apne area ka jo value enter kren,
 niche values diya area wise wo usme se select kro

            <option value="1401210">   ADITYAPUR-1
             <option value="1401220">  ADITYAPUR-2-
             <option value="1203220">  AMRAPADA
              <option value="1601430">  ASHOK NAGAR
            <option value="1203120">   BARHARWA
			<option value="1301130">   BARHI HAZARIBAGH
			<option value="1301520">   BARKATTA-1301520
			<option value="1101220">  BARWADDA-1101220
			<option value="1501210">   Barwahdih-1501210
			<option value="1201130">  BASUKINATH-1201130
			<option value="1201230">   BASUKINATH(JAMTARA)
			<option value="1102430">  BERMO-1102430
			<option value="1102410">  BERMO (TENUGHAT)
			<option value="1303220">  BHURKUNDA-1303220
			<option value="1601130">  BUNDU-1601130
			<option value="1402120">  CHAIBASA (RURAL) 
			<option value="1402110">  CHAIBASA (URBAN)
			<option value="1402210">  CHAKRADHARPUR
			<option value="1401330">  CHAKULIA
			<option value="1102350">  CHANDANKIYARI
			<option value="1402330">  CHANDIL
			<option value="1102320">  CHAS (RURAL)
			<option value="1102310">  CHAS (URBAN)
			<option value="1301410">  CHATRA (NORTH)
			<option value="1301420">  CHATRA( SOUTH)
			<option value="1501310">  CHHATARPUR
			<option value="1501130">  CHHATARPUR (DALTONGANJ)
			<option value="1401130">  CHHOTAGOVINDPUR
			<option value="1101330">  CHIRKUNDA
			<option value="1301510">  CHOUPARAN
			<option value="1301340">  CHOUPARAN
			<option value="1501120">  DALTONGANJ 
			<option value="1501110">  DALTONGANJ 
			<option value="1202110">  DEOGHAR
			<option value="1703110">  DEOGHAR
			<option value="1703120">  DEOGHAR
			<option value="1401350">  Dhalbhugarh
			<option value="1101420">  DHIGWADIH
			<option value="1304130">  DOMCHANCH
			<option value="1702130">  Domchanch (KODERMA)
			<option value="1601510">  DORANDA
			<option value="1201120">  DUMKA (RURAL)
			<option value="1201110">  DUMKA (URBAN)
			<option value="1701130">  Dumri-1701130
			<option value="1401320">  DVM-1401320
			<option value="1102330">  GANESHPUR
			<option value="1502110">  GARHWA I
			<option value="1502120">  GARHWA II
			<option value="1602120">  GHAGRA
			<option value="1401310">  GHATSHILA
			<option value="1701120">  GIRIDIH (RURAL)
			<option value="1701110">  GIRIDIH (URBAN)
			<option value="1703210">  GODDA-1703210
			<option value="1202210">  GODDA (GODDA)
			<option value="1402230">  GOELKERA
			<option value="1303120">  Gola-
			<option value="1102340">  GOMOH
			<option value="1101210">  GOVINDPUR
			<option value="1602110">  GUMLA
			<option value="1601420">  HARMU
			<option value="1301120">  HAZARIBAGH (RURAL)
			<option value="1301110">  HAZARIBAGH (URBAN)
			<option value="1601530">  HEC
			<option value="1101110">  HIRAPUR
			<option value="1401340">  JADUGOR
			<option value="1102440">  JAINAMORE-
			<option value="1201210">  JAMTARA
			<option value="1701210">  Jamua
			<option value="1501320">  JAPLA-
			<option value="1501140">  JAPLA (DALTONGANJ)
			<option value="1703130">  JASIDIH-
			<option value="1202120">  JASIDIH (DEOGHAR)
			<option value="1101410">  JHARIA-
			<option value="1304110">J  HUMARI TELAIYA
			<option value="1702110">  JHUMARI TELAIYA (KODERMA)
			<option value="1401110">  JSR (KARANDIH)-
			<option value="1401140">  JUGSALI
			<option value="1602130">  KAMDARA
			<option value="1601310">  KANKE
			<option value="1101130">  KARKEND
			<option value="1102420">  KATHARA (GOMIA)
			<option value="1301150">  KATKAMSANDI
			<option value="1102120">  KATRAS
			<option value="1601710">  Khunti
			<option value="1304120">  KODERMA
			<option value="1702120">  KODERMA (KODERMA)
			<option value="1601210">  KOKAR
			<option value="1602320">  KOLEBIRA
			<option value="1303210">  KUJJU
			<option value="1602220">  KURU
			<option value="1601220">  LALPUR
			<option value="1501220">  Latehar
			<option value="1602210">  LOHARDAGA
			<option value="1102110">  LOYABAD
			<option value="1703310">  MADHUPUR
			<option value="1202130">  MADHUPUR. (DEOGHAR)
			<option value="1202220">  MAHAGAMA
			<option value="1703220">  MAHGAMA
			<option value="1601410">  MAIN ROAD
			<option value="1601620">  MANDAR
			<option value="1401120">  MANGO
			<option value="1401410">  MANGO
			<option value="1401420">  MANGO-2-
			<option value="1402140">  MANJHARI
			<option value="1402220">  MANOHARPUR
			<option value="1201220">  MIHIJAM
			<option value="1101440">  MUKUNDA
			<option value="1502210">  NAGARUNTARI
			<option value="1402130">  NAVAMUNDI
			<option value="1101120">  NAYA BAZAAR
			<option value="1101310">  NIRSA 1-
			<option value="1101320">   NIRSA 2-
			<option value="1601120">  ORMANJHI-
			<option value="1203210">  PAKUR-
			<option value="1203230">  PAKUR (RURAL)
			<option value="1501150">  PATAN-
			<option value="1701220">  Rajdhanwar-
			<option value="1402320">  RAJKARSAVA-
			<option value="1203130">  RAJMAHAL-
			<option value="1303110">  RAMGARH-
			<option value="1601630">  RATU CHATTI-
			<option value="1601610">  RATU ROAD-
			<option value="1601230">  RMCH-
			<option value="1203150">  SAHEBGANJ (RURAL)
			<option value="1203110">  SAHIBGANJ
			<option value="1402310">  SARAIKELA
			<option value="1703320">  SARAT
			<option value="1202140">  SARAT (DEOGHAR)
			<option value="1701140">  SARIA
			<option value="1602310">  SIMDEGA
			<option value="1101430">  SINDRI
			<option value="1601110">  TATISILWAI
			<option value="1203140">  TINPAHAR
			<option value="1701230">  Tisri
			<option value="1102360">  Topchanchi-
			<option value="1601720">  Torpa-
			<option value="1101230">  TUNDI-
			<option value="1601520">  TUPUDANA-
			<option value="1601320">  UPPER BAZAAR
			"""

# GITHUB: https://github.com/backpackerdeveloper
# Linkedin : https://www.linkedin.com/in/shubhamtripz/
# Made with ♥ by Shubham
