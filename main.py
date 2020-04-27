from experta import *



class MedicalExpert(KnowledgeEngine):
    username = "", 
    chest_pain = "",

    @DefFacts()
    def needed_data(self):
        """ 
        This is a method which is called everytime engine.reset() is called.
        It acts like a constructor to this class.
        """        
        yield Fact(findDisease = 'true')
        print("Hi! I am Mr.Expert.\n\nYou can get yourself diagnosed here free of cost!\nI will ask you 10 questions.\n\n")
        

    @Rule(Fact(findDisease = 'true'),NOT(Fact(name=W())),salience = 1000)
    def ask_name(self):
        self.username = input("What's your name?\n")
        self.declare(Fact(name=self.username))

    @Rule(Fact(findDisease='true'), NOT (Fact(chestPain = W())),salience = 995)
    def hasChestPain(self):
        chest_pain = input("\nDo you have chest pain?\nPlease type Yes/No\n")
        self.declare(Fact(chestPain = chest_pain.strip().lower()))

    @Rule(Fact(findDisease='true'), (Fact(chestPain = 'yes')),salience = 990)
    def hasSevereChestPain(self):
        severe_chest_pain = input("\nIs it too severe?\nPlease type Yes/No\n")
        self.declare(Fact(severe_chestPain = severe_chest_pain.strip().lower()))
    
    @Rule(Fact(findDisease='true'), NOT (Fact(cough = W())),salience = 985)
    def hasCough(self):
        cough = input("\nDo you have cough?\nPlease type Yes/No\n")
        self.declare(Fact(cough = cough.strip().lower()))

    
    @Rule(Fact(findDisease='true'), (Fact(cough = 'yes')),salience = 980)
    def hasSevereCough(self):
        severe_cough = input("\nDo you have severe cough?\nPlease type Yes/No\n")
        self.declare(Fact(severe_chestPain = severe_cough.strip().lower()))


    @Rule(Fact(findDisease='true'), NOT (Fact(fainting = W())),salience = 975)
    def hasFainting(self):
        fainting = input("\nDo you faint occasionally?\nPlease type Yes/No\n")
        self.declare(Fact(fainting = fainting.strip().lower()))


   
#  sunken eyes, low body temperature,
# restlessness, sore throat, fever

    @Rule(Fact(findDisease='true'), NOT (Fact(fatigue = W())),salience = 970)
    def hasFatigue(self):
        fatigue = input("\nDo you experience fatigue occasionally?\nPlease type Yes/No\n")
        self.declare(Fact(fatigue = fatigue.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(headache = W())),salience = 965)
    def hasHeadache(self):
        headache = input("\nDo you experience headaches?\nPlease type Yes/No\n")
        self.declare(Fact(headache = headache.strip().lower()))
    
    @Rule(Fact(findDisease='true'), (Fact(headache = 'yes')),salience = 960)
    def hasSevereheadache(self):
        severe_headache = input("\nIs it too severe?\nPlease type Yes/No\n")
        self.declare(Fact(severe_headache = severe_headache.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(back_pain = W())),salience = 955)
    def hasbackPain(self):
        back_pain = input("\nDo you experience back pains?\nPlease type Yes/No\n")
        self.declare(Fact(back_pain = back_pain.strip().lower()))
    







    @Rule(Fact(findDisease='true'), Fact(severe_chestPain = 'yes'), Fact(cough='no'))
    def disease_0(self):
        self.declare(Fact(disease = 'Covid'))



    @Rule(Fact(findDisease = 'true'),Fact(disease = MATCH.disease),salience = -1)
    def getDisease(self, disease):
        print('The most probable illness you are suffering from is:',disease)
        print('\n\n')
        print('Some info about the disease:\n')
        
        f = open("disease/disease_descriptions/" + disease + ".txt", "r")
        print(f.read())

        print('\n\nNo need to worry',self.username,'. We even have some preventive measures for you!\n')
        f = open("disease/disease_treatments/" + disease + ".txt", "r")
        print(f.read())
    # @Rule(Fact(findDisease = 'true'),
    # Fact(name=MATCH.name))
    # def greet(self, name):
    #     print("Hi!",name, "How is the weather?")
if __name__ == "__main__":
    engine = MedicalExpert()
    engine.reset()
    engine.run()
    print('Printing engine facts after 1 run',engine.facts)
   