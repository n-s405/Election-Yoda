import csv 




def get_subject_keys(subject):
    # Returns a list containing all the keys in a subject 

    return_list = list()
    if subject == 'c' :
        target = f'data/celeb.csv'
    elif subject == 'l':
        target = f'data/leaders.csv'
    elif subject == 'n':
        target = f'data/news_outlet.csv'
    elif subject == 'p':
        target = f'data/parties.csv'
    else:
        target = f'data/{subject}.csv'
    print(target)
    with open(target) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count+=1 
            else:
                return_list.append(row[0])
                line_count += 1
    return return_list

def get_list_of_subjects():
    return 'celebs , leaders , news_outlets , parties'

def write_to_csv(subject,data):
    li = [data]
    if subject == 'c' :
        target = f'data/celeb.csv'
    elif subject == 'l':
        target = f'data/leaders.csv'
    elif subject == 'n':
        target = f'data/news_outlet.csv'
    elif subject == 'p':
        target = f'data/parties.csv'
    else:
        target = f'data/{subject}.csv'

    print(f'write target is : {target}')

    with open(target, mode='a') as open_file:
        # employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # employee_writer.writerow(li)
        open_file.write(f'{data}\n')
    return 0


def add_key_to_subject(subject,addition):
    lst = get_subject_keys(subject)
    if addition in lst:
        print('already present')
        return 0 
    else:
        write_to_csv(subject , addition)





def main():
    pass
    


if __name__ == "__main__":
    main()