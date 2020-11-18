'''
    this script to get random user from "https://randomuser.me/api/" api 
    i only get name , full address( street, city , state and postcode) , and cell phone number ,
    if you want get more data feel free to print the object_data variable and add the information that you want
    P.S: the data stored into the path as a variable array
'''
# imports
import requests


class random_user:


    def __init__(self,number = 0):
        self.number = number
        self.full_name = ''
        self.location = ''
        self.cell = ''
        self.percentage = 0
        self.counter = 0
        self.url = "https://randomuser.me/api/"
        # list to store all users objects in 
        self.all_users = []
    
    # getting percentage of progress
    def get_percentage(self):
        return str(100 - (self.number - self.counter) / self.number * 100 ) + "%"

    # getting the user
    def get_user(self,path):
        #make new requests untill reach desired number of users
        while self.counter < self.number:
            #handling error while processing response data
            try:
                user = {}
                req = requests.get(self.url)
                # handling response data because sometimes the api block response because of ddos attack protection and response with html error page on json data
                try:
                    json_data = req.json()
                except:
                    continue
                
                object_data = json_data["results"][0]
                user["name"] = object_data["name"]["first"]+ " " + object_data["name"]["last"]
                user["location"] = str(object_data["location"]["street"]["number"]) + " " + object_data["location"]["street"]["name"] + " " +  object_data["location"]["city"] + " " +  object_data["location"]["state"] + " " +  str(object_data["location"]["postcode"])
                user["cell"] = object_data["cell"]
                #append current user to users list 
                self.all_users.append(user)

                self.counter += 1
                print("we are getting " + self.get_percentage())

            except Exception as e:
                print(e)

                
        # write users list in into text like a string
        with open(path,"w+") as file:
            file.writelines(str(self.all_users))


#for test 

#initialize the class and pass number of users you want
ona = random_user(80)
#grab them and pass path where you want to save the data
ona.get_user("test.txt")
