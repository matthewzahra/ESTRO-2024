import math
import pandas as pd

#Treatment Object
class Treatment():
    def __init__(self,treatmentNo,doseScores):
        self.treatmentNo = treatmentNo      #is a string!
        self.doseScores = doseScores
        self.magnitude = self.getMagnitude()

    #find the magnitude of the doses score vector and return it
    def getMagnitude(self):
        total = 0
        for score in self.doseScores.values():
            total += score**2
        
        return math.sqrt(total)
    
#Patient Object
class Patient():
    def __init__(self,id,organs,treatments):
        self.id = id
        self.organs = organs
        self.treatments = treatments
        self.magnitudes = self.getMagnitudes()

    #return a dictionary of treatnmentNo:magnitude pairs
    def getMagnitudes(self):
        magnitudes = dict()
        for treatment in self.treatments:
            magnitudes[treatment.treatmentNo] = treatment.magnitude
        return magnitudes
    
#read data into a DataFrame
def extractData(fname):
    return pd.read_csv(fname)


#make a patient object given a record in the DataFrame
def makePatient(row,id,organs,fractions):
    treatments = []
    for frac in fractions:
        doseScores = dict()
        for org in organs:
            doseScores[frac + " " + org] = row.loc[frac + " " + org]
        t = Treatment(frac,doseScores)
        treatments.append(t)
    return Patient(row.loc[id],organs,treatments)



#turn each record in DataFrame into the relevant Patient object
#column name for patient id
#we need a list of the organ column names (including tumour name)
#list of prefixes for different treatments - way to signify if its the 1st, 2nd, ... treatment - called fractions, will also include a "Total" for aggregate dose
#and DataFrame of course
def genPatients(id,organs,fractions,df):
    patients = df.apply(lambda row: makePatient(row,id,organs,fractions), axis="columns")
    return patients

#write results to a .csv file
#patients is a Series of Patient objects - convert to a DataFrame by passing in a dictionary then write to csv
def writeData(fname,id,fractions,patients):
    data = dict()
    data[id] = []
    for frac in fractions:
        data[frac] = []
    for patient in patients.values:
        data[id].append(int(patient.id))
        for frac in fractions:
            data[frac].append(patient.magnitudes[frac])
    df = pd.DataFrame(data)
    print(df)
    df.to_csv(fname,index=False)
    print('#')


def main():
    df = extractData("C:/Users/matth/Documents/brachy/cx f1to3radar withtoxandOS.csv")
    patients = genPatients("Annonymised key", ["13minusD90","Bladder","Rectum","Sigmoid","Intestines"],["F1", "F2", "F3"],df)
    writeData('fractionsData.csv',"Annonymised key",["F1", "F2", "F3"],patients)
    #df = extractData("C:/Users/matth/Documents/brachy/cx f1to3radar withtoxandOS.csv")
    #patients = genPatients("Annonymised key", ["130minus D90","Bladder","Rectum","Sigmoid","Intestines"],["Total"],df)
    #writeData('data2.csv',"Annonymised key",["Total"],patients)


if __name__ == "__main__":
    main()