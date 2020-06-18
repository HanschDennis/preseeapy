from selenium import webdriver
import time
from CorpusDefinition import Corpus
from CorpusPreseea import PRESEEA
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://preseea.linguas.net/Corpus.aspx')
time.sleep(1)

#Get search fields
searchField_TextoABuscar = driver.find_element_by_id('dnn_ctr520_TranscriptionQuery_txtFtValue')

searchField_Nombre = driver.find_element_by_id('dnn_ctr520_TranscriptionQuery_txtFirstname')
searchField_Apellidos = driver.find_element_by_id('dnn_ctr520_TranscriptionQuery_txtSurname')
searchField_Institucion = driver.find_element_by_id('dnn_ctr520_TranscriptionQuery_txtInstitution')

checkBox_Sexo_Cualquiera = driver.find_element_by_id('dnn_ctr520_TranscriptionQuery_chkFtSex_0')
checkBox_Sexo_Hombre = driver.find_element_by_id('dnn_ctr520_TranscriptionQuery_chkFtSex_1')
checkBox_Sexo_Mujer = driver.find_element_by_id('dnn_ctr520_TranscriptionQuery_chkFtSex_2')

#fill search fields
searchField_TextoABuscar.send_keys('hago')

searchField_Nombre.send_keys('Dennis')
searchField_Apellidos.send_keys('Hansch')
searchField_Institucion.send_keys('Disney')

checkBox_Sexo_Hombre.click()
checkBox_Sexo_Mujer.click()

#search!
button_Buscar = driver.find_element_by_id('dnn_ctr520_TranscriptionQuery_btnFtSearch')
button_Buscar.click()

time.sleep(1)

#save as html-file
page = driver.page_source
file_ = open('example2.html', 'w', encoding="utf-8")
file_.write(page)
file_.close()

#parse html

corpus_preseea = PRESEEA()
corpus_preseea.set_search_phrase('hago')
corpus_preseea.set_filter(city="Pereira", gender="Mujer", age="Grupo 1", education="Medio")

# TODO: Read correctly from CorpusDefinition request
test_list = corpus_preseea.retrieve_phrase_data()

corpus_preseea.write_csv("testfile.csv")


#driver.quit()

