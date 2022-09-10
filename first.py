#Chapter 2


# print('10%2 =',10%2)
# print('Quotient of 7//3 =',7//3)
# print('Remainder of 7%3 =',7%3)

# print('10 + 15',10+15)
# print('\'10\' + \'15\'','10'+'15')
# print('Aye'*3)

# hours = int(input('Enter Hours: '))
# rate = float(input('Enter Rate: '))
# pay = hours * rate
# print(round(pay))

# tempCelsius = float(input("Enter temperature in Celcius:\n"))
# tempFahrenheit = (tempCelsius*9/5)+32
# print(tempCelsius,'degree celsius =',tempFahrenheit,'degree fahrenheit')


#Chapter 3 Conditional Execution

# try :
#     hour = float(input('Enter Hours: '))
#     rate = float(input('Enter Rate: '))
#     if hour>40 :
#         extra = (hour - 40) * (10*1.5)
#         pay = 40 * rate + extra
#     else :
#         pay = hour * rate
#         print(pay)

# except :
#     print('Error, please enter numeric input')

# score = input('Enter score: ')
# try :
#     score = float(score)
#     if score<=1.0 and score>=0.0 :
#         if score >= 0.9:
#             print('A')
#         elif score >= 0.8 :
#             print('B')
#         elif score >= 0.7 :
#             print('C')
#         elif score >= 0.6 :
#             print('B')
#         else :
#             print('F')
#     else :
#         print('Bad score')
# except :
#     print('Bad score')

#chapter 4




# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()

# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print('I sleep all night and I work all day.')

# repeat_lyrics()
# def computepay(hour,rate):
#     try :
#         print('Enter Hours:',hour)
#         print('Enter Rate:',rate)
#         if hour>40 :
#             extra = (hour - 40) * (10*1.5)
#             pay = 40 * rate + extra
#             print(pay)
#         else :
#             pay = hour * rate
#             print(pay)

#     except :
#         print('Error, please enter numeric input')

# computepay(45,10)

#chapter 5 iteration


# sum =0
# count = 0
# while True:
#     try:
#         number = input('Enter a number: ')
#         if number == 'done':
#             break
#         number = float(number)
#     except:
#         print('Invalid input')
#         continue

#     sum += number
#     count+=1

# print(sum,count,(sum/count))

#chapter 6

# c = 0
# def count(line, letter):
#     global c
#     for l in line:
#         if l == letter:
#             c+= 1

#     return c

# a = count('banana', 'a')
# print(a)

# str = 'X-DSPAM-Confidence:0.8475'
# spos = str.find(':')
# extracted = str[spos+1:]
# extracted = extracted.strip()
# extracted = float(extracted)
# print(extracted)

#chapter 8 files

# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     count = count + 1
#     if line.startswith('From:'):
#         line = line.rstrip()
#         print(line)

# print('Line Count:',count)

# inp = fhand.read()
# print(len(inp))
# print(inp[:20])

# for line in fhand:
#     line = line.rstrip();
#     if line.find('@uct.ac.za') == -1:
#         continue
#     print(line)

#chapter 

fhand = open('dictkey.txt','w')
fhand.write('key1 ')
fhand.write('key2 ')
fhand.write('key3 ')
fhand.close()
fhand = open('dictkey.txt')
anewdict = dict()
for line in fhand:
    lis = line.split()
    for k in lis:
        if k not in anewdict:
            anewdict[k] = ''

fhand.close()
print(anewdict)