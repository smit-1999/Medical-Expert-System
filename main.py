from experta import *
import ast


class MedicalExpert(KnowledgeEngine):
    username = "", 


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
        self.chest_pain = self.chest_pain.lower()
        self.declare(Fact(chestPain = self.chest_pain.strip().lower()))

    # @Rule(Fact(findDisease='true'), (Fact(chestPain = 'yes')),salience = 990)
    # def hasSevereChestPain(self):
    #     self.severe_chest_pain = input("\nIs it too severe?\nPlease type Yes/No\n")
    #     self.declare(Fact(severe_chestPain = self.severe_chest_pain.strip().lower()))
    
    @Rule(Fact(findDisease='true'), NOT (Fact(cough = W())),salience = 985)
    def hasCough(self):
        self.cough = input("\nDo you have cough?\nPlease type Yes/No\n")
        self.cough = self.cough.lower()
        self.declare(Fact(cough = self.cough.strip().lower()))

    
    # @Rule(Fact(findDisease='true'), (Fact(cough = 'yes')),salience = 980)
    # def hasSevereCough(self):
    #     self.severe_cough = input("\nDo you have severe cough?\nPlease type Yes/No\n")
    #     self.declare(Fact(severe_chestPain = self.severe_cough.strip().lower()))


    @Rule(Fact(findDisease='true'), NOT (Fact(fainting = W())),salience = 975)
    def hasFainting(self):
        self.fainting = input("\nDo you faint occasionally?\nPlease type Yes/No\n")
        self.fainting = self.fainting.lower()
        self.declare(Fact(fainting = self.fainting.strip().lower()))


   
#, low body temperature,
# restlessness, 

    @Rule(Fact(findDisease='true'), NOT (Fact(fatigue = W())),salience = 970)
    def hasFatigue(self):
        self.fatigue = input("\nDo you experience fatigue occasionally?\nPlease type Yes/No\n")
        self.fatigue = self.fatigue.lower()
        self.declare(Fact(fatigue = self.fatigue.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(headache = W())),salience = 965)
    def hasHeadache(self):
        self.headache = input("\nDo you experience headaches?\nPlease type Yes/No\n")
        self.headache = self.headache.lower()
        self.declare(Fact(headache = self.headache.strip().lower()))
    
    # @Rule(Fact(findDisease='true'), (Fact(headache = 'yes')),salience = 960)
    # def hasSevereheadache(self):
    #     self.severe_headache = input("\nIs it too severe?\nPlease type Yes/No\n")
    #     self.declare(Fact(severe_headache = self.severe_headache.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(back_pain = W())),salience = 955)
    def hasbackPain(self):
        self.back_pain = input("\nDo you experience back pains?\nPlease type Yes/No\n")
        self.back_pain = self.back_pain.lower()
        self.declare(Fact(back_pain = self.back_pain.strip().lower()))
    
    @Rule(Fact(findDisease='true'), NOT (Fact(sunken_eyes = W())),salience = 950)
    def hasSunkenEyes(self):
        self.sunken_eyes = input("\nDo you experience sunken eyes?\nPlease type Yes/No\n")
        self.sunken_eyes = self.sunken_eyes.lower()
        self.declare(Fact(sunken_eyes = self.sunken_eyes.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(fever = W())),salience = 945)
    def hasfever(self):
        self.fever = input("\nDo you experience fever?\nPlease type Yes/No\n")
        self.fever=self.fever.lower()
        self.declare(Fact(fever = self.fever.strip().lower()))

    @Rule(Fact(findDisease='true'), NOT (Fact(sore_throat = W())),salience = 940)
    def hassorethroat(self):
        self.sore_throat = input("\nDo you experience sore throat?\nPlease type Yes/No\n")
        self.sore_throat = self.sore_throat.lower()
        self.declare(Fact(sore_throat = self.sore_throat.strip().lower()))


    @Rule(Fact(findDisease='true'), NOT (Fact(restlessness = W())),salience = 935)
    def hasrestlessness(self):
        self.restlessness = input("\nDo you experience restlessness?\nPlease type Yes/No\n")
        self.restlessness = self.restlessness.lower()
        self.declare(Fact(restlessness = self.restlessness.strip().lower()))


    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'yes'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headche = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'yes'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'))
    def disease_0(self):
        self.declare(Fact(disease = 'Covid'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'yes'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'yes'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'))
    def disease_1(self):
        self.declare(Fact(disease = 'Alzheimers'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'yes'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'yes'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'))
    def disease_2(self):
        self.declare(Fact(disease = 'Asthma'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'yes'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'yes'))
    def disease_3(self):
        self.declare(Fact(disease = 'Diabetes'))


    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'yes'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'yes'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'))
    def disease_4(self):
        self.declare(Fact(disease = 'Epilepsy'))


    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'yes'),Fact(fever = 'yes'),Fact(sore_throat='yes'),
    Fact(restlessness = 'no'))
    def disease_5(self):
        self.declare(Fact(disease = 'Glaucoma'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'yes'),Fact(fatigue = 'no'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'))
    def disease_6(self):
        self.declare(Fact(disease = 'Heart Disease'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'yes'),Fact(fatigue = 'no'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'yes'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'))
    def disease_7(self):
        self.declare(Fact(disease = 'Heat Stroke'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'yes'),Fact(fever = 'no'),Fact(sore_throat='no'),
    Fact(restlessness = 'yes'))
    def disease_8(self):
        self.declare(Fact(disease = 'Hyperthyroidism'))
    
    @Rule(Fact(findDisease='true'),Fact(chestPain = 'yes'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'yes'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'no'),Fact(sore_throat='yes'),
    Fact(restlessness = 'no'))
    def disease_9(self):
        self.declare(Fact(disease = 'Hypothermia'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'yes'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'yes'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'yes'),Fact(sore_throat='no'),
    Fact(restlessness = 'no'))
    def disease_10(self):
        self.declare(Fact(disease = 'Jaundice'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'no'),
    Fact(headache = 'yes'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'no'),Fact(fever = 'yes'),Fact(sore_throat='yes'),
    Fact(restlessness = 'no'))
    def disease_11(self):
        self.declare(Fact(disease = 'Sinusitis'))

    @Rule(Fact(findDisease='true'),Fact(chestPain = 'no'), Fact(cough = 'no'), Fact(fainting = 'no'),Fact(fatigue = 'yes'),
    Fact(headache = 'no'),Fact(back_pain = 'no'),Fact(sunken_eyes = 'yes'),Fact(fever = 'yes'),Fact(sore_throat='no'),
    Fact(restlessness = 'yes'))
    def disease_12(self):
        self.declare(Fact(disease = 'Tuberculosis'))


    @Rule(Fact(findDisease='true'),NOT (Fact(disease = W())),salience = -1)
    def unmatched(self):
        self.declare(Fact(disease = 'unknown'))

    @Rule(Fact(findDisease = 'true'),Fact(disease = MATCH.disease),salience = 1)
    def getDisease(self, disease):
        
        if(disease == 'unknown'):
            mapDisease = []
            mapDisease.append('back_pain')
            mapDisease.append('chest_pain')
            mapDisease.append('cough')
            mapDisease.append('fainting')
            mapDisease.append('fatigue')
            mapDisease.append('fever')
            mapDisease.append('headache')
            mapDisease.append('sore_throat')
            mapDisease.append('restlessness')
            mapDisease.append('sunken_eyes') 
            print('\n\nWe checked the following symptoms',mapDisease)
            mapDisease_val=[self.back_pain,self.chest_pain,self.cough,self.fainting,self.fatigue
            ,self.fever,self.headache,self.sore_throat,self.restlessness,self.sunken_eyes]
            print('\n\nSymptoms in patients are :', mapDisease_val)
            
            file = open("disease_symptoms.txt", "r")
            contents = file.read()
            dictionary = ast.literal_eval(contents)
            file.close()
            
            yes_symptoms = []
            for i in range(0,len(mapDisease_val)):
                if mapDisease_val[i] == 'yes':
                    yes_symptoms.append(mapDisease[i])
            
            max_val = 0
            print('\n\nYes symptoms noticed are : ', yes_symptoms)
            for key in dictionary.keys():
                val = dictionary[key].split(",")
                count = 0
                print(key,":",val)
                for x in val:
                    if x in yes_symptoms:
                        count+=1
                #print('Count:',count)
                if count > max_val:
                    max_val = count
                    pred_dis = key
            
            if max_val == 0:
                print("No diseases found.You are healthy!")
            else:
                print("\n\nWe are unable to tell you the exact disease with confidence.But we believe that you suffer from",pred_dis)
                
                print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')

                print ('\n\nSome info about the disease:',pred_dis)
                
                f = open("disease/disease_descriptions/" + pred_dis + ".txt", "r")
                print(f.read())
                print('# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
                print('\n\nNo need to worry',self.username,'. We even have some preventive measures for you!\n')
                f = open("disease/disease_treatments/" + pred_dis + ".txt", "r")
                print(f.read())
                print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
        else:
            print('The most probable illness you are suffering from is:',disease)
            print('\n\n')
            print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
            print('Some info about the disease:\n')
            print(disease)
            f = open("disease/disease_descriptions/" + disease + ".txt", "r")
            print(f.read())
            print('\n# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
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
   