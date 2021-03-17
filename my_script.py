# Read only 

# csv, txt, json, (for excel you convert to csv unless you use the pandas library)

def read_only():
    ''' a method that only reads the file '''
    try: 
        file1 = open('data.txt', 'r') # this is the path of the file you're opening the 'r' specifies to readonly - by default it is also only readonly
        text = file1.read()
        print(text)
        file1.close() # the reson for closing is because it will remain open in memory if you don't close. 
    except FileNotFoundError:
        text = None
        print(text)


def write_only():
    '''A method that writes to a file'''
    # if file exist, it will be overwritten
    # if file does not exist, it will be created
    file2 = open('more_data.txt', 'w')
    file2.write('tomatoes')
    file2.close()

# python will know to close this file (even if there are errors)
# with open('data.txt') as f:
#     txt = f.read()
#     print(txt)

def read_food_sales():
    all_dates = []
    all_regions = []
    all_cities = []
    with open('sampledatafoodsales.csv') as f:
        data = f.readlines()

        for food_sale in data:
            # food_sale (each element in list)
            split_food_sale = food_sale.split(',')
            regions = split_food_sale[1]
            cities = split_food_sale[2]
            all_regions.append(f" {regions}, {cities}")
            all_cities.append(cities)
            order_date = split_food_sale[0]
            print(order_date)
            # append order_date to all_dates list
            all_dates.append(order_date)
    print(all_dates)
    
    with open('dates.txt', 'w') as f:
        for date in all_dates:
            f.write(date)
            f.write('\n')
    with open('regions.txt', 'w') as f:
        for region in all_regions:
            f.write(region)
            f.write('\n')
    with open('cities.txt', 'w') as f:
        for city in all_cities:
            f.write(city)
            f.write('\n')

def append_text():
    '''Append data to an existing file'''
    with open('dates.txt', 'a') as f:
        f.write('3/17/2021')
        print('done')

# 2. Put all of the region inside of a region.txt (Region)















if __name__ == '__main__':
    # read_only()
    #write_only()
    read_food_sales()