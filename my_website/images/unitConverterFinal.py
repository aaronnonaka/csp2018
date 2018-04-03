def print_list():
    listOfUnits = ('1. in->cm','2. in->m','3. in->km','4. cm->in','5. cm->ft','6. cm->m','7. cm->km','8. m->km','9. mm->km','10.mm->m','11.g->kg','12.kg->g','13.l->gal')
    counter = 0
    while counter < len(listOfUnits):
        print listOfUnits[counter]
        counter += 1
        
def unit_converter():
    loop = 0 #loop control variable
    while loop < 1:
        input1 = raw_input('Do you want to convert units? ')
        if input1 == 'yes' or input1 == 'y':
            print_list()
            choice = int(raw_input('Which conversion do you want to do? (type the number associated with it) '))
            
            #These are the inch conversions
            if choice == 1:
                value = float(raw_input('Enter the value of the number to convert '))
                value = value * 2.54
                print 'Your conversion is', value, 'cm.'
            elif choice == 2:
                value = float(raw_input('Enter the value of the number to convert '))
                value = value * 0.0254
                print 'Your conversion is', value, 'm.'
            elif choice == 3:
                value = float(raw_input('Enter the value of the number to convert '))
                value = value * 0.0000254
                print 'Your conversion is', value, 'km.'
                
            #These are the centimeter conversions
            elif choice == 4:
                value = float(raw_input('Enter the value of the number to convert '))
                value = value * 0.393701
                print 'Your conversion is', value, 'in.'
            elif choice == 5:
                value = float(raw_input('Enter the value of the number to convert '))
                value = value * 0.0328084
                print 'Your conversion is', value, 'ft.'
            elif choice == 6:
                value = float(raw_input('Enter the value of the number to convert '))
                value = value * 0.01
                print 'Your conversion is', value, 'm.'
            elif choice == 7:
                value = float(raw_input('Enter the value of the number to convert '))
                value = value * 0.00001
                print 'Your conversion is', value, 'km.'
            
            #This is the meter conversion
            elif choice == 8:
                value = float(raw_input('Enter the value of the number to convert '))
                value = value * 0.001
                print 'Your conversion is', value, 'km.'
            
            #This is the millimeter conversions
            elif choice == 9:
                value = float(raw_input('Enter the value of the number to convert '))
                value = value * 0.000001
                print 'Your conversion is', value, 'km.'
            elif choice == 10:
                value = float(raw_input('Enter the value of the number to convert '))
                value = value * 0.001
                print 'Your conversion is', value, 'm.'
                
            #This is the gram conversion
            elif choice == 11:
                value = float(raw_input('Enter the value of the number to convert '))
                value = value * 0.001
                print 'Your conversion is', value, 'kg.'
                
            #This is the kilogram conversion
            elif choice == 12:
                value = float(raw_input('Enter the value of the number to convert '))
                value = value * 1000
                print 'Your conversion is', value, 'g.'
            
            #This is the liter conversion
            elif choice == 13:
                value = float(raw_input('Enter the value of the number to convert '))
                value = value * 0.264172
                print 'Your conversion is', value, 'gal.'
                
            else:
                print 'Invalid input. Please reenter.'
        elif input1 == 'no' or input1 == 'n':
            loop += 1 #Break out of the loop if user input
        else:
            print 'Invalid input. Please reenter.'
