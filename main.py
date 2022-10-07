# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome('/Users/icdev/Documents/Indonesia College/Registrasi/Driver/Chrome/chromedriver')
browser.get('https://registrasi.indonesiacollege.id/')

action = ActionChains(browser)

# ======================= form lokasi
malang = browser.find_element(by=By.XPATH, value="//div[@onclick='get_program(104)']")
selanjutnya = browser.find_element(by='id', value='forward')
malang.click()
selanjutnya.click()

# ======================= form data diri
nama = browser.find_element(by='id', value='nama')
email = browser.find_element(by='id', value='email')
hp = browser.find_element(by='id', value='phone')
islam = browser.find_element(by=By.XPATH, value="//option[@value='Islam']")
laki = browser.find_element(by=By.XPATH, value="//option[@value='Laki-laki']")
sekolah = browser.find_element(by='id', value='sekolah')
th_lulus = browser.find_element(by='id', value='th_lulus')
tpt_lahir = browser.find_element(by='id', value='select2-kabupatenkota_lahir-container')
tgl_lahir = browser.find_element(by='id', value='tgl_lahir')


# isi form data diri
nama.send_keys('Tri yulianto')
email.send_keys('tri@gmail.com')
hp.send_keys('089912341234')
islam.click()
laki.click()
sekolah.send_keys('SMKN 5 YK')
th_lulus.send_keys('2010')
tpt_lahir.click()
simulue = browser.find_element(by=By.CLASS_NAME, value='select2-results')
cari = browser.find_element(by=By.CLASS_NAME, value='select2-search__field')
cari.send_keys(Keys.ARROW_DOWN, Keys.RETURN)
tgl_lahir.send_keys("13071995")
selanjutnya.click()


# ======================= form Alamat
# Province
provinsi = browser.find_element(by='id', value='select2-propinsi-container')
provinsi.click()
selectProvinsi = browser.find_element(by=By.CLASS_NAME, value='select2-search__field')
selectProvinsi.send_keys(Keys.ARROW_DOWN, Keys.RETURN)

# Kabupaten
kabupaten = browser.find_element(by='id', value='select2-kabupatenkota-container')
browser.implicitly_wait(10)
# ActionChains(browser).move_to_element(kabupaten).click().perform()
kabupaten.click()
# kabupaten = browser.find_element(by=By.XPATH, value='//*[text()="Pilih Kabupaten/Kota"]')
# kabupaten.click()
selectKabupaten = browser.find_element(by=By.CLASS_NAME, value='select2-search__field')
selectKabupaten.send_keys(Keys.ARROW_DOWN, Keys.RETURN)

# Kecamatan
kecamatan = browser.find_element(by='id', value='select2-kecamatan-container')
browser.implicitly_wait(10)
kecamatan.click()
selectKecamatan = browser.find_element(by=By.CLASS_NAME, value='select2-search__field')
selectKecamatan.send_keys(Keys.ARROW_DOWN, Keys.RETURN)

# Desa
desa = browser.find_element(by='id', value='select2-desa-container')
browser.implicitly_wait(10)
desa.click()
selectDesa = browser.find_element(by=By.CLASS_NAME, value='select2-search__field')
selectDesa.send_keys(Keys.ARROW_DOWN, Keys.RETURN)

#
# Detail
jalan = browser.find_element(by='id', value='jalan')
browser.implicitly_wait(10)
jalan.send_keys('jalan rumah sendiri')

selanjutnya.click()

# ======================= form Data Wali
# nama-wali
namawali = browser.find_element(by='id', value='nama-wali')
namawali.send_keys('Suwardi')

# Pengawai Negeri Sipil
kerja = browser.find_element(by=By.XPATH, value="//option[@value='Pengawai Negeri Sipil']")
kerja.click()

# nowa-wali
nowawali = browser.find_element(by='id', value='nowa-wali')
nowawali.send_keys('089912341234')

selanjutnya.click()

# ======================= form Isian
program = browser.find_element(by='id', value='program-bimbel')
opsiprogram = [x for x in program.find_elements(by=By.TAG_NAME, value="option")]
program.click()
browser.implicitly_wait(10)

# opsi = browser.find_element(by=By.XPATH, value='//option[]')
# opsiprogram = element
pOpsiProgram = len(opsiprogram)
for element in opsiprogram:
    # nilai = opsiprogram[i].find_element(by=By.XPATH, value="//option[@value]")
    nilai = element.find_element(by=By.XPATH, value="//option[@value]")
    if nilai != 0:
        nilai.click()

# print(pOpsiProgram)
# for i in opsiprogram:
#     print("isi dari i = " + i)
# program.click()
# program.send_keys(Keys.ARROW_DOWN, Keys.RETURN)
