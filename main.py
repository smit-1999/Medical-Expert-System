from experta import *



class MedicalExpert(KnowledgeEngine):
    username = "", 
    chest_pain = "",severe_chest_pain="",
    cough="",severe_cough="",
    fainting="",fatigue="",






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
        self.chest_pain = input("\nDo you have chest pain?\nPlease type Yes/No\n")
        self.declare(Fact(chestPain = self.chest_pain.strip().lower()))

    # @Rule(Fact(findDisease='true'), (Fact(chestPain = 'yes')),salience = 990)
    # def hasSevereChestPain(self):
    #     self.severe_chest_pain = input("\nIs it too severe?\nPlease type Yes/No\n")
    #     self.declare(Fact(severe_chestPain = self.severe_chest_pain.strip().lower()))
    
    @Rule(Fact(findDisease='true'), NOT (Fact(cough = W())),salience = 985)
    def hasCough(self):
        self.cough = input("\nDo you have cough?\nPlease type Yes/No\n")
        self.declare(Fact(cough = self.cough.strip().lower()))

    
    # @Rule(Fact(findDisease='true'), (Fact(cough = 'yes')),salience = 980)
    # def hasSevereCough(self):
    #     self.severe_cough = input("\nDo you have severe cough?\nPlease type Yes/No\n")
    #     self.declare(Fact(severe_chestPain = self.severe_cough.strip().lower()))


    @Rule(Fact(findDisease='true'), NOT (Fact(fainting = W())),salience = 975)
    def hasFainting(self):
        self.fainting = input("\nDo you faint occasionally?\nPlease type Yes/No\n")
        self.declare(Fact(fainting = self.fainting.strip().lower()))


   
#, low body temperature,
# restlessness, 

    @Rule(Fact(findDisease='true'), NOT (Fact(fatigue = W())),salience = 970)
    def hasFatigue(self):
        self.fatigue = input("\nDo you experience fatigue occasionally?\nPlease type Yes/No\n")
        self.declare(Fact(fatigue = self.fatigue.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(headache = W())),salience = 965)
    def hasHeadache(self):
        self.headache = input("\nDo you experience headaches?\nPlease type Yes/No\n")
        self.declare(Fact(headache = self.headache.strip().lower()))
    
    # @Rule(Fact(findDisease='true'), (Fact(headache = 'yes')),salience = 960)
    # def hasSevereheadache(self):
    #     self.severe_headache = input("\nIs it too severe?\nPlease type Yes/No\n")
    #     self.declare(Fact(severe_headache = self.severe_headache.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(back_pain = W())),salience = 955)
    def hasbackPain(self):
        self.back_pain = input("\nDo you experience back pains?\nPlease type Yes/No\n")
        self.declare(Fact(back_pain = self.back_pain.strip().lower()))
    
    @Rule(Fact(findDisease='true'), NOT (Fact(sunken_eyes = W())),salience = 950)
    def hasSunkenEyes(self):
        self.sunken_eyes = input("\nDo you experience sunken eyes?\nPlease type Yes/No\n")
        self.declare(Fact(sunken_eyes = self.sunken_eyes.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(fever = W())),salience = 945)
    def hasfever(self):
        self.fever = input("\nDo you experience fever?\nPlease type Yes/No\n")
        self.declare(Fact(fever = self.fever.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(sore_throat = W())),salience = 940)
    def hassorethroat(self):
        self.sore_throat = input("\nDo you experience sore throat?\nPlease type Yes/No\n")
        self.declare(Fact(sore_throat = self.sore_throat.strip().lower()))


    @Rule(Fact(findDisease='true'), NOT (Fact(restlessness = W())),salience = 935)
    def hasrestlessness(self):
        self.restlessness = input("\nDo you experience restlessness?\nPlease type Yes/No\n")
        self.declare(Fact(restlessness = self.restlessness.strip().lower()))


    @Rule(Fact(findDisease='true'), Fact(chestPain = 'yes'), Fact(cough='no'))
    def disease_0(self):
        self.declare(Fact(disease = 'Covid'))

    @Rule(Fact(findDisease='true'),salience = 1)
    def unmatched(self):
        self.declare(Fact(disease = 'unknown'))

    @Rule(Fact(findDisease = 'true'),Fact(disease = MATCH.disease),salience = -1)
    def getDisease(self, disease):
        
        if(disease == 'unknown'):
            print(self.back_pain)
            print('We are unable to tell you the exact disease with confidence.But we believe that')

        else:
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
   