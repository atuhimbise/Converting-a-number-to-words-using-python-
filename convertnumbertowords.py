#Create a unique list of names of numbers below 20 
under_20 = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']

#create another unique list of tens
tens = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety'] 
#create a dictionary with key:value pairs for hundred, thousand, million, billion and trillion which is our limit for this particular program.
above_100 = {100: 'Hundred',1000:'Thousand', 1000000:'Million', 1000000000:'Billion', 1000000000000:'Trillion'}
#Let's start by defining a function that takes num, our user input as a parameter
def num2words(num):
    
    if num < 20:
        return under_20[num]#This returns words for any number below 20
    if num < 100:
        return  tens[(int)(num/10)-2] + '-' + (''if num%10==0 else'' + under_20[num%10])
#This converts num to tens and ones and combines them to get words for any given num   
# find the appropriate pivot - 'Million' in 3,603,550, or 'Thousand' in 603,550 
    pivot = max([key for key in above_100.keys() if key <= num])
    return num2words((int)(num/pivot)) + ' ' + (above_100[pivot] + ' and'if above_100[pivot]=='Hundred' else above_100[pivot]) + (' 'if num%pivot==0  else ' ' + num2words(num%pivot)) 
num = int(input("Enter a number: "))
#This outputs the input num to words.
print(num2words(num))
