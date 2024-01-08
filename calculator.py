def calculate():
    operation = input('''
Select airthmetic operator for calculation:               
                    for addition press + :
                      for substraction press - :
                      for multiplication press * :
                      for division press / :
                      for module press % :
                      for power press ** :
                    ''' )
    
    num_1 = int(input('Enter the first number:'))
    num_2 = int(input('Enter the second number:'))

    if operation == '+':
        print('{} + {} =' .format(num_1, num_2))
        print(num_1 + num_2)

    elif operation == '-':
        print('{} - {} =' .format(num_1, num_2))
        print(num_1 - num_2)

    elif operation == '*':
        print('{} * {} =' .format(num_1, num_2))
        print(num_1 * num_2)

    elif operation == '/':
        print('{} / {} =' .format(num_1, num_2))
        print(num_1 / num_2)

    elif operation == '%':
        print('{} % {} =' .format(num_1, num_2))
        print(num_1 % num_2)

    elif operation == '**':
        print('{} ** {} =' .format(num_1, num_2))
        print(num_1 ** num_2)
    else:
        print('invalid operation: try again!')

#Add aain function to calculate() function
        again()

def again():
   calc_again = input('''                
do you want to calculate again?
please type Y for yes and N for no:                                                                                                                                                                                                                                                                                                                                                                                                                       
                       ''')
   if calc_again.upper() == 'Y':
       calculate()
   elif calc_again.upper() == 'N':
       print('Thankyou!')
   else:
       again()
        
calculate()






