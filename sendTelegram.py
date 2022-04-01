from threading import local
import telegram_send
from numpy import NaN, float64, little_endian
import time
import datetime

#Changer le PATH
#path_file_dat="/home/angelz/Bots/Trading/TrixStrategy/historiques-soldes.dat"

class TelegramMessage():
    def __init__(self, path_file):
        global message
        self.path_file_dat=path_file
        self.message=" "
        self.soldeLastExec=""
        self.solde6heures=""
        self.solde12heures=""
        self.solde1jours=""
        self.solde3jours=""
        self.solde7jours=""
        self.solde14jours=""
        self.solde1mois=""
        self.solde2mois=""
        

    def addMessageComponent(self, string):
        self.message=self.message+"\n"+string

    def getDateTelegramMessage(self):
        date = datetime.datetime.now()
        todayJour=date.day
        todayMois=date.month
        todayAnnee=date.year
        todayHeure=date.hour
        todayMinutes=date.minute
        self.addMessageComponent(f"{todayJour}/{todayMois}/{todayAnnee} {todayHeure}:{todayMinutes}")
        #print(self.message)
        

    def readFileDat(self):
        date = datetime.datetime.now()
        todayJour=date.day
        todayMois=date.month
        todayAnnee=date.year
        todayHeure=date.hour
        todayMinutes=date.minute
        with open(self.path_file_dat, "r") as f:
            for line in f:
                if "#" in line:
                    # on saute la ligne
                    continue
                data = line.split()
                jour=int(data[0])
                mois=int(data[1])
                annee=int(data[2])
                heure=int(data[3])
                minutes=int(data[4])
                solde=float(data[5])

                #permet de trouver le solde de 6 heures auparavant
                if(todayHeure<=6):
                    if ((todayJour-1==jour) and (todayMois==mois) and (todayAnnee==annee)) :
                        if((24-(6-todayHeure)==heure)):
                            self.solde6heures=solde
                    elif (todayJour==1 and ((todayMois-1==mois) and (todayAnnee==annee)) or ((todayMois==1) and (todayAnnee-1==annee) and (jour==31))) :
                        if((24-(6-todayHeure)==heure)):
                            self.solde6heures=solde
                elif ( (todayHeure-6==heure) and (todayJour==jour) and (todayMois==mois) and (todayAnnee==annee) ) :
                    self.solde6heures=solde
                    
                #permet de trouver le solde de 12 heures auparavant
                if(todayHeure<=12):
                    if ((todayJour-1==jour) and (todayMois==mois) and (todayAnnee==annee)) :
                        if((24-(12-todayHeure)==heure)):
                            self.solde12heures=solde
                    elif (todayJour==1 and ((todayMois-1==mois) and (todayAnnee==annee)) or ((todayMois==1) and (todayAnnee-1==annee) and (jour==31))) :
                        if((24-(12-todayHeure)==heure)):
                            self.solde12heures=solde
                elif ( (todayHeure-12==heure) and (todayJour==jour) and (todayMois==mois) and (todayAnnee==annee) ) :
                    self.solde12heures=solde
                    
                #permet de trouver le solde de 1 jours auparavant
                if(todayJour<=1):
                    if ((todayMois-1==mois) and (todayAnnee==annee)) or ((todayMois==1 and mois==12) and (todayAnnee-1==annee)) :
                        if (mois==1 or mois==3 or mois==5 or mois==7 or mois==8 or mois==10 or mois==12) :
                            if((31-todayJour+1==jour)):
                                self.solde1jours=solde
                        else :
                            if((30-todayJour+1==jour)):
                                self.solde1jours=solde
                elif ( (todayJour-1==jour) and (todayMois==mois) and (todayAnnee==annee) ) :
                    self.solde1jours=solde
                    
                #permet de trouver le solde de 3 jours auparavant
                if(todayJour<=3):
                    if ((todayMois-1==mois) and (todayAnnee==annee)) or ((todayMois==1 and mois==12) and (todayAnnee-1==annee)) :
                        if (mois==1 or mois==3 or mois==5 or mois==7 or mois==8 or mois==10 or mois==12) :
                            if((31-todayJour+3==jour)):
                                self.solde3jours=solde
                        else :
                            if((30-todayJour+3==jour)):
                                self.solde3jours=solde
                elif ( (todayJour-3==jour) and (todayMois==mois) and (todayAnnee==annee) ) :
                    self.solde3jours=solde
                
                #permet de trouver le solde de 7 jours auparavant
                if(todayJour<=7):
                    if ((todayMois-1==mois) and (todayAnnee==annee)) or ((todayMois==1 and mois==12) and (todayAnnee-1==annee)) :
                        if (mois==1 or mois==3 or mois==5 or mois==7 or mois==8 or mois==10 or mois==12) :
                            if((31-todayJour+7==jour)):
                                self.solde7jours=solde
                        else :
                            if((30--todayJour+7==jour)):
                                self.solde7jours=solde
                elif ( (todayJour-7==jour) and (todayMois==mois) and (todayAnnee==annee) ) :
                    self.solde7jours=solde
                    
                #permet de trouver le solde de 14 jours auparavant
                if(todayJour<=14):
                    if ((todayMois-1==mois) and (todayAnnee==annee)) or ((todayMois==1 and mois==12) and (todayAnnee-1==annee)) :
                        if (mois==1 or mois==3 or mois==5 or mois==14 or mois==8 or mois==10 or mois==12) :
                            if((31-todayJour+14==jour)):
                                self.solde14jours=solde
                        else :
                            if((30-todayJour+14==jour)):
                                self.solde14jours=solde
                elif ( (todayJour-14==jour) and (todayMois==mois) and (todayAnnee==annee) ) :
                    self.solde14jours=solde
                    
                #permet de trouver le solde de 1 mois auparavant
                if(todayMois==1 and mois==12 and annee==todayAnnee-1 and todayJour==jour) :
                    self.solde1mois=solde
                elif(todayMois-1==mois and annee==todayAnnee and todayJour==jour) :
                    self.solde1mois=solde
                    
                #permet de trouver le solde de 2 mois auparavant
                if(todayMois==1 and mois==11 and annee==todayAnnee-1 and todayJour==jour) :
                    self.solde2mois=solde
                if(todayMois==2 and mois==12 and annee==todayAnnee-1 and todayJour==jour) :
                    self.solde2mois=solde
                elif(todayMois-2==mois and annee==todayAnnee and todayJour==jour) :
                    self.solde2mois=solde
                self.soldeLastExec=solde

    def writeFileDat(self, todaySolde):
       # usdAmount = ftx.get_balance_of_one_coin('USD')
        print(f"Solde du compte => {todaySolde} $")
        date = datetime.datetime.now()
        todayJour=date.day
        todayMois=date.month
        todayAnnee=date.year
        todayHeure=date.hour
        todayMinutes=date.minute

        with open(self.path_file_dat, "a") as f:
            f.write(f"{todayJour} {todayMois} {todayAnnee} {todayHeure} {todayMinutes} {todaySolde} \n")

    def sendMessageResume(self, todaySolde, message_action, name):
        self.getDateTelegramMessage()
        self.readFileDat()
        self.writeFileDat(todaySolde)
        #==================================================
        # Affiche les messages de comparaison dans le bot
        #==================================================
        self.addMessageComponent("===================")
        self.addMessageComponent("Bilan d'évolution "+ name +":\n")
        
       
        if self.soldeLastExec != "":
            bonus=100*(todaySolde-self.soldeLastExec)/self.soldeLastExec 
            gain=bonus/100*self.soldeLastExec
            bonus=round(bonus,3)
            gain=round(gain,5)
            self.soldeLastExec=round(self.soldeLastExec,5)
            if gain<0 :
                self.addMessageComponent(f" - Dernière execution du bot : {bonus}% ({self.soldeLastExec}$ {gain}$)")
            else :
                self.addMessageComponent(f" - Dernière execution du bot : +{bonus}% ({self.soldeLastExec}$ +{gain}$)")
        if self.solde6heures != "":
            bonus=100*(todaySolde-self.solde6heures)/self.solde6heures 
            gain=round(bonus/100*todaySolde,2)
            bonus=round(bonus,3)
            gain=round(gain,5)
            self.solde6heures=round(self.solde6heures,5)
            if gain<0 :
                self.addMessageComponent(f" - il y a 6h : {bonus}% ({self.solde6heures}$ {gain}$)")
            else :
                self.addMessageComponent(f" - il y a 6h : +{bonus}% ({self.solde6heures}$ +{gain}$)")
        if self.solde12heures != "":
            bonus=100*(todaySolde-self.solde12heures)/self.solde12heures 
            gain=round(bonus/100*todaySolde,2)
            bonus=round(bonus,3)
            gain=round(gain,5)
            self.solde12heures=round(self.solde12heures,5)
            if gain<0 :
                self.addMessageComponent(f" - il y a 12h : {bonus}% ({self.solde12heures}${gain}$)")
            else :
                self.addMessageComponent(f" - il y a 12h : +{bonus}% ({self.solde12heures}$ +{gain}$)")
        if self.solde1jours != "":
            bonus=100*(todaySolde-self.solde1jours)/self.solde1jours
            gain=round(bonus/100*todaySolde,2)
            bonus=round(bonus,3)
            gain=round(gain,5)
            self.solde1jours=round(self.solde1jours,5)
            if gain<0 :
                self.addMessageComponent(f" - il y a 1j : {bonus}% ({self.solde1jours}$ {gain}$)")
            else :
                self.addMessageComponent(f" - il y a 1j : +{bonus}% ({self.solde1jours}$ +{gain}$)")
        if self.solde3jours != "":
            bonus=100*(todaySolde-self.solde3jours)/self.solde3jours
            gain=round(bonus/100*todaySolde,2)
            bonus=round(bonus,3)
            gain=round(gain,5)
            self.solde3jours=round(self.solde3jours,5)
            if gain<0 :
                self.addMessageComponent(f" - il y a 3j : {bonus}% ({self.solde3jours}$ {gain}$)")
            else :
                self.addMessageComponent(f" - il y a 3j : +{bonus}% ({self.solde3jours}$ +{gain}$)")
        if self.solde7jours != "":
            bonus=100*(todaySolde-self.solde7jours)/self.solde7jours
            gain=round(bonus/100*todaySolde,2)
            bonus=round(bonus,3)
            gain=round(gain,5)
            self.solde7jours=round(self.solde7jours,5)
            if gain<0 :
                self.addMessageComponent(f" - il y a 7j : {bonus}% ({self.solde7jours}$ {gain}$)")
            else :
                self.addMessageComponent(f" - il y a 7j : +{bonus}% ({self.solde7jours}$ +{gain}$)")
        if self.solde14jours != "":
            bonus=100*(todaySolde-self.solde14jours)/self.solde14jours
            gain=round(bonus/100*todaySolde,2)
            bonus=round(bonus,3)
            gain=round(gain,5)
            self.solde14jours=round(self.solde14jours,5)
            if gain<0 :
                self.addMessageComponent(f" - il y a 14j : {bonus}% ({self.solde14jours}$ {gain}$)")
            else :
                self.addMessageComponent(f" - il y a 14j : +{bonus}% ({self.solde14jours}$ +{gain}$)")
        if self.solde1mois != "":
            bonus=100*(todaySolde-self.solde1mois)/self.solde1mois
            gain=round(bonus/100*todaySolde,2)
            bonus=round(bonus,3)
            gain=round(gain,5)
            self.solde1mois=round(self.solde1mois,5)
            if gain<0 :
                self.addMessageComponent(f" - il y a 1 mois : {bonus}% ({self.solde1mois}$ {gain}$)")
            else :
                self.addMessageComponent(f" - il y a 1 mois : +{bonus}% ({self.solde1mois}$ +{gain}$)")
        if self.solde2mois != "":
            bonus=100*(todaySolde-self.solde2mois)/self.solde2mois
            gain=round(bonus/100*todaySolde,2)
            bonus=round(bonus,3)
            gain=round(gain,5)
            solde2mois=round(self.solde2mois,5)
            if gain<0 :
                self.addMessageComponent(f" - il y a 2 mois : {bonus}% ({self.solde2mois}$ {gain}$)")
            else :
                self.addMessageComponent(f" - il y a 2 mois : +{bonus}% ({self.solde2mois}$ +{gain}$)")
        self.addMessageComponent("\n")
        self.addMessageComponent(f"SOLDE TOTAL => {todaySolde} $")
        print(f"{self.message}")
        telegram_send.send(messages=[f"{message_action} \n{self.message}"])
    