while True:
    while True:
        while True:
            unit= input ('Do you want to convert temperature(t), distance(d), area(a) or volume(v)? ')
            if unit == 't':
                print('The units you can convert are:\nCelsius(c)\nFahrenheit(f)\nKelvin(k)\n')
                while True:
                    while True:
                        from1=input('What do you want to convert from? ')
                        if from1 == 'c':
                            to=input('What do you want to convert to? ')
                            c=float(input("\nThe temperature in Celsius is: "))
                            if to == 'f':
                                f=c*9/5+32
                                f1=round(f,1)
                                print("The temperature is: "+str(f1)+'˚F'+'\n')
                                break
                            elif to == 'k':
                                k=c+273.15
                                k1=round(k,1)
                                print("The temperature is: "+str(k1)+' K'+'\n')
                                break
                            else:
                                print("I didn’t quite get that, please anser Fahrenheit(f) or Kelvin(k).\n")
                            break
                        elif from1 == 'f':
                            to=input('What do you want to convert to? ')
                            f=float(input("\nThe temperature in Fahrenheit is: "))
                            if to == 'c':
                                c=(f-32)*5/9
                                c1=round(c,1)
                                print("The temperature is: "+str(c1)+'˚C'+'\n')
                                break
                            elif to == 'k':
                                k=(f+459.67)*5/9
                                k1=round(k,1)
                                print("The temperature is: "+str(k1)+' K'+'\n')
                                break
                            else:
                                print("I didn’t quite get that, please anser Celsius(c) or Kelvin(k).\n")
                            break
                        elif from1 == 'k':
                            to=input('What do you want to convert to? ')
                            k=float(input("\nThe temperature in Kelvin is: "))
                            if to == 'c':
                                c=k-273.15
                                c1=round(c,1)
                                print("The temperature is: "+str(c1)+'˚C'+'\n')
                                break
                            elif to == 'f':
                                f=k*9/5-459.67
                                f1=round(f,1)
                                print("The temperature is: "+str(f1)+'˚F'+'\n')
                                break
                        else:
                            print("I didn’t quite get that, please anser Celsius(c) or Fahrenheit(f).\n")
                        break
                    else:
                        print("I didn’t quite get that, please anser Celsius(c), Fahrenheit(f) or Kelvin(k).\n")
                    while True:
                        redo=input('Do you want to do another temperature convertion? ')
                        if redo is 'y':
                            break
                        elif redo is 'n':
                            break
                        else:
                            print("I didn’t quite get that, please anser yes(y) or no(n).\n")
                        break
                if redo is 'y':
                    print('Ok')
                elif redo is 'n':
                    print('Ok\n')
                    break
                break
            elif unit == 'd':
                print('distance converter coming soon.\n')
                break
            elif unit == 'a':
                print('area converter coming soon.\n')
                break
            elif unit == 'v':
                print('volume converter coming soon.\n')
                break
            else:
                print("I didn’t quite get that, please anser temperature(t), distance(d), area(a) or volume(v).\n")
        while True:
            redo1=input('Do you want to do another convertion? ')
            if redo1 is 'y':
                break
            elif redo1 is 'n':
                break
            else:
                print("I didn’t quite get that, please anser yes(y) or no(n).\n")
        if redo1 is 'y':
            print('Ok\n')
        elif redo1 is 'n':
            print('Ok, good bye.')
            break
    if redo1 is 'y':
        print('')
    elif redo1 is 'n':
        break
