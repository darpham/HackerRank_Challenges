'''
https://www.coderbyte.com/editor/guest:Correct%20Path:Python

Have the function CorrectPath(str) read the str parameter being passed, which will represent the movements made in a 5x5 grid of cells starting from the top left position. The characters in the input string will be entirely composed of: r, l, u, d, ?. Each of the characters stand for the direction to take within the grid, for example: r = right, l = left, u = up, d = down. Your goal is to determine what characters the question marks should be in order for a path to be created to go from the top left of the grid all the way to the bottom right without touching previously travelled on cells in the grid. 

For example: if str is "r?d?drdd" then your program should output the final correct string that will allow a path to be formed from the top left of a 5x5 grid to the bottom right. For this input, your program should therefore return the string rrdrdrdd. There will only ever be one correct path and there will always be at least one question mark within the input string. 
'''

def CorrectPath(str): 
    location = {
        'horizontal': 0,
        'vertical': 0
    }

    for motion in str:

        if motion == 'r':
            location['horizontal'] += 1

        elif motion == 'l':
            location['horizontal'] -= 1

        elif motion == 'u':
            location['vertical'] -= 1

        elif motion == 'd':
            location['vertical'] += 1

    output = ''
    for s in str:
        if s == '?':

            if location['vertical'] == location['horizontal'] == 4:
                output += 'u'
                location['vertical'] -= 1
                continue

            if location['vertical'] < 4:
                output += 'd'
                location['vertical'] += 1
                continue
            else:
                output += 'u'
                location['vertical'] -= 1
                continue

            if location['horizontal'] < 4:
                output += 'r'
                location['horizontal'] += 1
                continue
            else:
                output += 'l'
                location['horizontal'] -= 1
                continue

        else:
            output += s
            
    return output

print(CorrectPath('drdr??rrddd?'))