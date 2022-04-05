class Criminal:
    def __init__(self,firstName,lastName,gender,crimeType,inJail,description):
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.crimeType = crimeType
        self.inJail = inJail
        self.description = description

    def isMatch(self, gender, crimeType):
        if self.inJail == False:
            return False
        
        if gender == self.gender and crimeType == self.crimeType:
            return True

            
    def display(self):
        jailDesc = "Not Incarcerated"
        if self.inJail == True:
            jailDesc = "Incarcerated"

        print(f"""
            {self.firstName} {self.lastName}
            Gender: {self.gender}
            Crime = {self.crimeType}
            {jailDesc} 
            {self.description}
        """)
        
        
