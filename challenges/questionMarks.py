'''
https://www.coderbyte.com/editor/guest:Questions%20Marks:Python
Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters, and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10. If so, then your program should return the string true, otherwise it should return the string false. If there aren't any two numbers that add up to 10 in the string, then your program should return false as well. 

For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string. 
'''

def QuestionsMarks(str): 
    strNoAplha = ''
    for char in str:
        if not char.isalpha():
            strNoAplha += char
    currentChar = ''
    count = 0
    for char in strNoAplha:
        if char.isdigit():
            if currentChar == '':
                currentChar = char
                count = 0
            else:
                if int(currentChar) + int(char) == 10:
                    if count == 3:
                        return True

                    else:
                        currentChar = ''
                        count = 0
                else:
                    currentChar = ''
                    count = 0
        else:
            count += 1
    return False
    
# keep this function call here  
print(QuestionsMarks('acc?7??sss?3rr1??????5'))