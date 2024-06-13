

class Session:

    _instance = None

    id: int = None
    username: str = None
    name: str = None
    email: str = None
    @staticmethod
    def get_instance():
        _instance = None

        if Session._instance == None:
           Session(None,None,None,None) 
        return Session._instance

    def __init__(self, id, username, name, email):
        if Session._instance != None:
            
            raise Exception("La instancia ya existe")
            
        else:
            Session._instance = self
            self.id = id
            self.username = username
            self.name = name
            self.email = email
            
    
    def print_data(self):
        print(self.id,self.username,self.name,self.email)

    # def get_user(self):
    #     return f"{self.id}, {self.username}, {self.name}, {self.email}"

    # def clear_user(self):
    #     self.id = None
    #     self.username = None
    #     self.name = None
    #     self.email = None


jesus = Session(1, "Jesusway69", "Jesus", "jesusway60@midominio.es")
jesus.print_data()
jose = Session(2, "Pepe84", "Jose", "pepepepe@midominio.es")


print(jesus , " -- ", jose)
print(f"Jesus = id: {jesus.id}, username: {jesus.username}, name: {jesus.name}, email: {jesus.email}")
print(f"Jose = id: {jose.id}, username: {jose.username}, name: {jose.name}, email: {jose.email}")

#remove_instance(jose)
print(jesus)
print(f"Jesus = id: {jesus.id}, username: {jesus.username}, name: {jesus.name},email: {jesus.email}")