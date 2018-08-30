
# coding: utf-8

# In[1]:


def payments(bill,ppl):
    try:
        return round((bill,ppl),2)
    except:
        print('Error occured')

def tip(bill,perc,ppl):
    try:
        return round(((bill * (perc/100.00))/ppl),2)
    except:
        print('Error occured')


def main():
    print('How much was the bill?')
    while True:
        try:
            total_bill = float(input('>> $'))
            break
        except:
            print (" ")
            print('Must be a number value')
            print(' ')
    print(' ')
    
    print('How many people?')
    while True:
        try:
            total_people = int(input('>>'))
            break
        except:
            print (" ")
            print('Must be a number value')
            print(' ')
    print(' ')
    
    print('What percentage of tip?')
    while True:
        try:
            perc = int(input('>> %'))
            break
        except:
            print (" ")
            print('Must be a number value')
            print(' ')
    print(' ')
    
    print('Calculating payment....')
    
    bill_payment = (total_bill/total_people)
    
    tip_payment = ((total_bill*(perc/100.00))/(total_people))
    
    total_payment = float(bill_payment)+float(tip_payment)
    
    print(f'Each person pays ${bill_payment} for the bill')
    
    print(f'Each person pays ${tip_payment} for the tip')
    
    print(f'Which means each person will pay a total of ${total_payment}')


# In[2]:


main()

