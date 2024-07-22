import pyautogui
import pytesseract
import google.generativeai as genai
from key import *

# API KEY
genai.configure(api_key=gemini_api_key)

def remove_non_alphanumeric(string):
  return "".join(char for char in string if char.isalnum())

def answer(extracted_question):
   # Choose Gemini Ai Model
  model = genai.GenerativeModel('gemini-pro')
  text = extracted_question

  # generate response for the extracted text
  response = model.generate_content(text, stream=True)
  # only print the text result from AI
  for chunk in response:
    print("-")
    final_answer = chunk.text
   
  return(final_answer)

def screenshot():
  # Takes screenshot of specific coordinates on screen
  screenshots_taken = []
  # left, top, width, and height
  left_value = 600
  width_value = 550
  question_height = 50
  #im = pyautogui.screenshot(region=(550, 250, 700, 700))
  question_screenshot = pyautogui.screenshot(region=(left_value,275,width_value,200))
  option1_screenshot = pyautogui.screenshot(region=(left_value,605,width_value, question_height))
  option2_screenshot = pyautogui.screenshot(region=(left_value,685,width_value,question_height))
  option3_screenshot = pyautogui.screenshot(region=(left_value,755,width_value,question_height))
  option4_screenshot = pyautogui.screenshot(region=(left_value,830,width_value,question_height))
  locate_region_screenshot = pyautogui.screenshot(region=(855,301,width_value,question_height))
  #print("image taken")
  # Saves the image, will update everytime, not create a new png file
  #im.save('screenshot_taken.png')
  question_screenshot.save('screenshots/question_ss_taken.png')
  option1_screenshot.save('screenshots/option1_ss_taken.png')
  option2_screenshot.save('screenshots/option2_ss_taken.png')
  option3_screenshot.save('screenshots/option3_ss_taken.png')
  option4_screenshot.save('screenshots/option4_ss_taken.png')
  locate_region_screenshot.save('screenshots/locate_region.png')
  screenshots_taken +=  question_screenshot, option1_screenshot, option2_screenshot, option3_screenshot, option4_screenshot
  print(len(screenshots_taken))
  return(screenshots_taken)

def text_extract(screenshotted):
  im = screenshotted[0]
  extracted_text_list = []
  for i in range(len(screenshotted)):
    try:
      text = pytesseract.image_to_string(screenshotted[i], lang='eng')
      #print("Text extracted:")
      print(text.strip())
      the_text = remove_non_alphanumeric(text)
      extracted_text_list += [the_text.strip()]
      extracted_text_list[1] = remove_non_alphanumeric(extracted_text_list[1])
      i+=1
    except Exception as e:
      print("Error occurred during OCR:", e)
  return(extracted_text_list)
    
def compareSolutions(gemini_answer, extracted_text_list):
  correct_option = []
  answer_number = 0
  for x in range(len(extracted_text_list)):
    print('xxxxxxxx')
    print(extracted_text_list[x])
    if (gemini_answer == extracted_text_list[x]):
      print('Same Answer Found')
      correct_option += (extracted_text_list[x])
      correct_option_together = "".join(correct_option)
      print(correct_option_together)
      break
    else:
      print("same answer not found")
      answer_number += 1
  
  return answer_number

def clickAnswer(theOptionNumber, grabbedScreenshot):
  print(theOptionNumber)


  if theOptionNumber == 1:
    choice_ss = 'screenshots/option1_ss_taken.png'
  elif theOptionNumber == 2:
    choice_ss = 'screenshots/option2_ss_taken.png'
  elif theOptionNumber == 3:
    choice_ss = 'screenshots/option3_ss_taken.png'
  elif theOptionNumber == 4:
    choice_ss = 'screenshots/option4_ss_taken.png'

  correct_option_location = ''
  print(choice_ss)
  while (correct_option_location == ''):
    try:
      correct_option_location = pyautogui.locateCenterOnScreen(choice_ss, region= (580, 275, 550, 650), grayscale=True, confidence=0.9)
    except pyautogui.ImageNotFoundException:
      print('The image could not be found.')
    print(str(correct_option_location))

  pyautogui.click(correct_option_location)

def main():
   grabbedScreenshot = screenshot()
   extractedText = text_extract(grabbedScreenshot)
   split_extracted_text = "\n".join(extractedText)
   answerChunk = answer(split_extracted_text)

   print(answerChunk)

   optionNumber = compareSolutions(answerChunk, extractedText)
   clickAnswer(optionNumber, grabbedScreenshot)
   
main()


   
