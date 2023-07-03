#!/bin/env python

##################################################
## This bot scrapes the US Embassy's website for you 
## to look for available visa appointments once every
## 60 seconds. It will play a loud buzzer if an appointment
## is found to notify you.
##################################################
## MIT License
##################################################
## Author: Mahdiar Edraki
## Copyright: Open-source
## Email: edrakimahdiar@gmail.com
##################################################

from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import keyboard
import time
import winsound
from selenium.webdriver import ChromeOptions, Chrome

def login_to_website(driver):
	time.sleep(1)
	Login_link="https://ais.usvisa-info.com/en-"+driver.country_code+"/niv/users/sign_in"
	driver.get(Login_link)
	time.sleep(1)

	Password = driver.password
	Email_Address= driver.email_address

	email_address_box = driver.find_element_by_id('user_email')
	pass_box = driver.find_element_by_id('user_password')

	email_address_box.send_keys(Email_Address)
	pass_box.send_keys(Password)

	time.sleep(2)
	I_Have_Understood_button = driver.find_element_by_xpath("//input[@type='checkbox']")
	ActionChains(driver).click(I_Have_Understood_button).perform()
	time.sleep(5)

	# Click login
	login_button = driver.find_element_by_name('commit')
	login_button.click()

	time.sleep(1)

def logout_to_website(driver):
	time.sleep(1)
	Logout_link="https://ais.usvisa-info.com/en-"+driver.country_code+"/niv/users/sign_out"
	driver.get(Logout_link)
	time.sleep(1)

def group_applicants(driver):
	All_applicants = driver.find_elements_by_xpath("//input[@type='checkbox']")

	applicant1 = All_applicants[0]
	applicant2 = All_applicants[1]
	applicant3 = All_applicants[2]
	if Choose_applicant_1 != '1':
		ActionChains(driver).click(applicant1).perform()
	if Choose_applicant_2 != '2':
		ActionChains(driver).click(applicant2).perform()
	if Choose_applicant_3 != '3':
		ActionChains(driver).click(applicant3).perform()	
	
	# Click Continue
	continue_button = driver.find_element_by_name('commit')
	continue_button.click()


def found_appointment(driver):
	## Script below is run when an appointment is found
	# Open the calendar box
	Calendar_button = driver.find_element_by_id("appointments_consulate_appointment_date")
	Calendar_button.click()
	#winsound.Beep(440, 500)
	current_year = 2022
	Date_selected = False
	stopKey = "s" #The stopKey is the button to press to stop. you can also do a shortcut like ctrl+s
	
	while True:
		current_year_element = driver.find_element_by_class_name("ui-datepicker-year")
		current_year = int(current_year_element.get_attribute('innerHTML'))

		current_month_element_left = driver.find_elements_by_class_name("ui-datepicker-month")[0]
		current_month_left = current_month_element_left.get_attribute('innerHTML')

		time.sleep(1)
		if current_year == (int(driver.Year_up_to)):
			if current_month_left == driver.Month_up_to:
				break

		Date_Available_List = driver.find_elements_by_css_selector("a[class='ui-state-default']")
		if not Date_Available_List: # 1. Check left and right boxes if date is available
			Right_button_calendar = driver.find_element_by_css_selector("span[class='ui-icon ui-icon-circle-triangle-e']")
			Right_button_calendar.click()
		else:
			Date_Available = driver.find_element_by_css_selector("a[class='ui-state-default']")
			Date_Available.click()
			Date_selected = True

			winsound.Beep(440, 500)
			break
	if Date_selected:
		# Close calendar
		winsound.Beep(440, 500)
		
		Consulate_Location_Button= driver.find_element_by_id("appointments_consulate_address")
		Consulate_Location_Button.click()

		winsound.Beep(440, 500)
		
		Appointment_Time_Button = driver.find_element_by_id("appointments_consulate_appointment_time")
		Appointment_Time_Button.click()
		while True:
			if keyboard.is_pressed(stopKey):
				while True:
					time.sleep(1)
			else:
				winsound.Beep(440, 500)
	else:
		# print("something went wrong cause it didnt find the date that was available")
		return True
		# IF reached 2025, it means no date was available.

def create_driver():
	options = ChromeOptions()
	options .add_experimental_option("detach", True)
	# options.headless = True
	options.add_experimental_option("excludeSwitches", ["enable-logging"])
	time.sleep(1)
	driver = Chrome(options=options)
	return driver

def run_bot(driver):
	stopKey = "s" #The stopKey is the button to press to stop. you can also do a shortcut like ctrl+s
	pause_between_commands = 1
	Try_Again = True
	log_off_log_in_time= 2
	start_time = time.time()
	Appointment_Not_Early_Enough = True
	while Appointment_Not_Early_Enough:
		while Try_Again:
			elapsed_time = (time.time())- start_time
			if elapsed_time //3600 == log_off_log_in_time:
				log_off_log_in_time +=2
				logout_to_website(driver)
				time.sleep(1)
				login_to_website(driver)
				time.sleep(1)
			try:
				driver.window_handles

				# Find and click on list of courses
				continue_button = driver.find_element_by_link_text("Continue")
				continue_button.click()
				time.sleep(pause_between_commands)
				Schedule_Appointment_button = driver.find_element_by_link_text("Reschedule Appointment")
				Schedule_Appointment_button.click()
				time.sleep(pause_between_commands)
				Schedule_Appointment_button = driver.find_elements_by_link_text("Reschedule Appointment")[1]
				Schedule_Appointment_button.click()
				
				# group_applicants(driver)

				select = Select(driver.find_element_by_id("appointments_consulate_appointment_facility_id"))
				select.select_by_value(driver.city_code)

				time.sleep(2)
				element = driver.find_element_by_id("consulate_date_time")
				attributeValue = element.value_of_css_property("display")
				if ('none' in attributeValue) or (attributeValue is None):
					Try_Again = True
					cancel_button = driver.find_element_by_css_selector("a[class='button secondary']")
					cancel_button.click()
					time.sleep(30)
				else:
					Try_Again = False
					#winsound.Beep(440, 500)
					break
			except:
				print("Driver doesn't have active window.")
				return
		
		Appointment_Not_Early_Enough = found_appointment(driver)
		if Appointment_Not_Early_Enough:
			Try_Again = True	
			cancel_button = driver.find_element_by_css_selector("a[class='button secondary']")
			cancel_button.click()
			time.sleep(30)
	return

if __name__ == "__main__":
	driver = create_driver()
	
	driver.minimize_window()
	Embassy_Country_Code = {
		"1" : 	"ae",
		"2" : 	"am",
		"3" : 	"tr",
		"4" : 	"ca",
	}

	Canada_City_Code = {
		"1" : 	'89',
		"2" : 	'90',
		"3" : 	'91',
		"4" : 	'92',
		"5" : 	'93',
		"6" : 	'94',
		"7" : 	'95',
	}

	UAE_City_Code = {
		"1" : 	'49',
		"2" : 	'50',
	}

	Selected_country_code = input(	  "UAE = 1 \n"
									+ "Armenia = 2 \n"
									+ "Turkey = 3 \n"
									+ "Canada = 4 \n"
									+ "Type the number for your country and press Enter:\n")
	
	# UAE Cities
	if Selected_country_code == '1':
		Selected_city_code = input(	  	"Abu Dhabi = 1 \n"
										+ "Dubai = 2 \n"
										+ "Type the number for your city and press Enter:\n")
		Selected_city_code = UAE_City_Code[Selected_city_code]
		
	# Canadian Cities
	if Selected_country_code == '4':
		Selected_city_code = input(	  	"Calgary = 1 \n"
										+ "Halifax = 2 \n"
										+ "Montreal = 3 \n"
										+ "Ottawa = 4 \n"
										+ "Quebec City = 5 \n"
										+ "Toronto = 6 \n"
										+ "Vancouver = 7 \n"
										+ "Type the number for your city and press Enter:\n")
		Selected_city_code = Canada_City_Code[Selected_city_code]

					
	email_address = input("Enter your login email address and press Enter:\n")
	password = input("Enter your login password and press Enter:\n")

	driver.Year_up_to = input("Enter the year up to which you want the algorithm to search for appointments and press Enter: (e.g. 2024)\n")
	driver.Month_up_to = input("Enter the Month up to which you want the algorithm to search for appointments and press Enter: (e.g. March)\n")
	driver.maximize_window()

	while True:
		driver.password = password
		driver.email_address = email_address
		driver.country_code = Embassy_Country_Code[Selected_country_code]
		driver.city_code = Selected_city_code
		
		login_to_website(driver)

		run_bot(driver)
