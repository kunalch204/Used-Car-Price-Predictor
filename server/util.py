import pickle
import json
import numpy as np

__brands = None
__exterior_names = None
__interior_names = None
__data_columns = None
__model = None





def get_estimated_price(brand, interior, exterior, age, miles, accidents, owners):
    try:
        brand_index = __data_columns.index(brand.lower())
        exterior_index = __data_columns.index(exterior.lower())
        interior_index = __data_columns.index(interior.lower())
    except:
        brand_index = -1
        exterior_index = -1
        interior_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = miles
    x[1] = accidents
    x[2] = owners
    x[3] = age
    if brand_index>=0:
        x[brand_index] = 1
    if exterior_index>=0:
        x[exterior_index] = 1
    if interior_index>=0:
        x[interior_index] = 1

    return round(__model.predict([x])[0],2)

def get_brand_names():
    return __brands

def get_exterior_names():
    return __exterior_names

def get_interior_names():
    return __interior_names


def get_data_columns():
    return __data_columns

def load_saved_artifacts():
    print ("Loading saved artifacts... start")
    global __data_columns
    global __brands
    global __exterior_names
    global __interior_names
    
    with open("./artifacts/columns.json", "r") as f:
            __data_columns = json.load(f)['data_columns']
            __brands = __data_columns[4:32]  # first 4 columns are not brands
            __interior_names =  __data_columns[32:40]
            __exterior_names = __data_columns[40: ] 


    global __model
    if __model is None:
        with open('./artifacts/used_car_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")




if __name__ == '__main__':
    load_saved_artifacts()
    # print(get_brand_names())
    # print(get_exterior_names())
    # print(get_interior_names())
    print(get_estimated_price('BMW', 'Black','White', 3, 50000, 0, 1))