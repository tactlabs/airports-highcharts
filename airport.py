import pandas as pd 

def get_data():
    
    df = pd.read_csv('data.csv')

    print(df['country'].tolist())

    country            = df['country'].tolist()

    count               = df['count'].tolist()

   

    # print(df['quebec'].tolist())

    result_dict = {
        'country'            : country,
        'count'             : count,
        
    }

    # print(result_dict)

    return result_dict

def add_row(country, count):

    df = pd.read_csv('data.csv') 

    new_row = {
    
        'country'       : country, 
        'count'         : count, 
        
    }

    print(df)

    df = df.append(new_row, ignore_index=True)

    print(df)

    df.to_csv('data.csv')

if __name__ == "__main__":
    get_data()