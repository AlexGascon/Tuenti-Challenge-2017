from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def positon_to_id(position):
    return "{}-{}".format(position[1], position[0])

def possible_end_positions(start_position, length):

    length = length-1
    row, column = start_position
    possible_positions = [[row - length, column - length], [row - length, column], [row - length, column + length],
                          [row, column - length], [row, column + length],
                          [row+length, column-length], [row+length, column], [row+length, column+length]]
    return possible_positions

def clickOnStaleElement(id, driver):
    try:
        driver.find_element_by_id(id).click()
    except StaleElementReferenceException:
        clickOnStaleElement(id, driver)

def read_stale_element(elem, id, driver):
    try:
        text = elem.text
        return text
    except StaleElementReferenceException:
        elem = driver.find_element_by_id(id)
        read_stale_element(elem, id, driver)


# Loading the site
site = 'http://52.49.91.111:8036/word-soup-challenge'
driver = webdriver.Firefox()
driver.get(site)

# Getting words
try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'words')))
except TimeoutException:
    pass

words_list = driver.find_element_by_id('words')
words = [word.text for word in words_list.find_elements_by_tag_name('div')[:-2]]  # The last two divs are the time and an empty div

# Setting the start, end an length of all the words to seek
start_letters = [word[0] for word in words]
end_letters = [word[-1] for word in words]
length = [len(word) for word in words]

# Setting a table array
table_lines = driver.find_elements_by_tag_name('tr')
table_arr = []
for table_line in table_lines:
    letters = table_line.find_elements_by_tag_name('td')
    letters_arr = []
    for letter in letters:
        text = letter.text
        letters_arr.append(text)
    table_arr.append(letters_arr)
#table = np.array(table_arr)


words_done = 0
for row_index in range(len(table_arr)):
    row = table_arr[row_index]
    print('In row {}'.format(row_index))
    #for start_letter_index in range(len(start_letters)):
    start_letter_index = -1

    while start_letter_index < len(start_letters):
        start_letter_index += 1
        try:
            letter = start_letters[start_letter_index]
        except IndexError:
            break
        print('LETTER {}'.format(letter))

        times = row.count(letter)
        last_position = 0
        time = 0
        repeat_letter = True
        while repeat_letter:
        #for time in range(times):

            try:
                letter_index = row.index(letter, last_position)
            except ValueError:
                repeat_letter = False
                break
            last_position = letter_index
            position = (row_index, letter_index)
            print(position)
            x = possible_end_positions(position, length[start_letter_index])
            print(length[start_letter_index])
            print(x)

            start_cell = driver.find_element_by_id(positon_to_id(position))
            for table_row, table_column in x:

                if table_row <= 5 and table_row >= 0 and table_column <= 5 and table_column >= 0:
                    end_cell = driver.find_element_by_id(positon_to_id([table_row, table_column]))
                    end_cell_text = read_stale_element(end_cell, positon_to_id([table_row, table_column]), driver)

                    if end_cell_text == end_letters[start_letter_index]:
                        print(positon_to_id(position))
                        print(positon_to_id([table_row, table_column]))
                        clickOnStaleElement(positon_to_id(position), driver)
                        clickOnStaleElement(positon_to_id([table_row, table_column]), driver)

                        # If we've find a word
                        if len(driver.find_elements_by_class_name("word-done")) > words_done:
                            words_done += 1
                            start_letter_index -= 1
                            print("WORD FOUND")
                            #start_letters.pop(start_letter_index)
                            #end_letters.pop(start_letter_index)
                            #length.pop(start_letter_index)

                            time -= 1
                            repeat_letter = True
                            break
                        else:
                            last_position += 1
                            repeat_letter = False


                            #last_position -= 1  # We want to check the same letter again, in case it starts other words

            time += 1
            last_position += 1
        #start_letter_index += 1



# Going on to the next level
try:
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'btn-level-2')))
except TimeoutException:
    pass

to_level2 = driver.find_element_by_id('btn-level-2')
to_level2.click()

# Getting words
try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'words')))
except TimeoutException:
    pass

words_list = driver.find_element_by_id('words')
words = [word.text for word in words_list.find_elements_by_tag_name('div')[:-2]]  # The last two divs are the time and an empty div

# Setting the start, end an length of all the words to seek
start_letters = [word[0] for word in words]
end_letters = [word[-1] for word in words]
length = [len(word) for word in words]

# Setting a table array
table_lines = driver.find_elements_by_tag_name('tr')
table_arr = []
for table_line in table_lines:
    letters = table_line.find_elements_by_tag_name('td')
    letters_arr = []
    for letter in letters:
        text = letter.text
        letters_arr.append(text)
    table_arr.append(letters_arr)
#table = np.array(table_arr)


words_done = 0
for row_index in range(len(table_arr)):
    row = table_arr[row_index]
    start_letter_index = -1

    while start_letter_index < len(start_letters):
        start_letter_index += 1
        try:
            letter = start_letters[start_letter_index]
        except IndexError:
            break

        last_position = 0
        repeat_letter = True
        while repeat_letter:

            try:
                letter_index = row.index(letter, last_position)
            except ValueError:
                repeat_letter = False
                break
            last_position = letter_index
            position = (row_index, letter_index)
            x = possible_end_positions(position, length[start_letter_index])

            for table_row, table_column in x:

                if table_row <= 19 and table_row >= 0 and table_column <= 19 and table_column >= 0:
                    end_cell = driver.find_element_by_id(positon_to_id([table_row, table_column]))
                    end_cell_text = read_stale_element(end_cell, positon_to_id([table_row, table_column]), driver)

                    if end_cell_text == end_letters[start_letter_index]:
                        clickOnStaleElement(positon_to_id(position), driver)
                        clickOnStaleElement(positon_to_id([table_row, table_column]), driver)

                        # If we've find a word
                        if len(driver.find_elements_by_class_name("word-done")) > words_done:
                            words_done += 1
                            start_letter_index -= 1

                            repeat_letter = True
                            break
                        else:
                            last_position += 1
                            repeat_letter = False


                            #last_position -= 1  # We want to check the same letter again, in case it starts other words

            last_position += 1