#!/usr/bin/env python
import random
from faker import Faker
zipcode=[
    75850,	
    74700,	
    75760,	
	75990,	
	75700,	
	75900,	
	75890,	
	75840,	
 	74600,	
	75790,	
	75850,	
	75800,	
	74000,	
	75650,	
	75660,	
	75750,	
	75780,	
	75730,	
	75600,	
    74200,	
	75580,	
	75520,	
	75620,	
	75640,	
	75530,	
	75500,
	75510,	
    74400,	
    75950,	
 	75290,	
 	75300,	
 	75260,	
	75330,	
	75280,	
	75340,	
	75550,	
	75400,	
	75350,	
 	75270,	
 	75460,	
	74800]
zlength=len(zipcode)
faker = Faker()
data=[]
a0=0
a1=0
a2=0
a3=0
a4=0
a5=0
a6=0
a7=0
file=open("data2.txt","w")
for a0 in range(0,zlength-1):
    for a1 in range(0,2):
        for a2 in range(0,3):
            for a3 in range(0,1):
                for a4 in range(0,5):
                    for a5 in range(0,4):
                        for a6 in range(0,1):
                            for a7 in range(0,6):
                                d1=faker.profile()
                                gender=d1['sex']
                                dob=d1['birthdate']
                                if a0<9:
                                    a8='0'+str(a0)
                                else:    
                                    a8=str(a0)

                                cnic='42'+a8+'01-'+str(a1)+str(a2)+str(a3)+str(a4)+str(a5)+str(a6)+str(a7)+'-'+(str(random.choice([2,4,6,8])) if gender=='F' else str(random.choice([1,3,5,7,9])))    
                                # data.append(
                                #     {'name':faker.name(),'dob':str(dob),'cnic':str(cnic),'gender':gender,'city':'Karachi','address':faker.street_name(),'zipCode':str(zipcode[random.randint(0,zlength)])}
                                # )
                                file.write(faker.name()+"\t"+str(dob)+"\t"+str(cnic)+"\t"+gender+"\t"+'Karachi'+"\t"+faker.street_name()+"\t"+str(zipcode[random.randint(0,zlength-1)])+"\t"+random.choice(['vaccinated','notvaccinated'])+"\t"+random.choice(['positive','negative'])+"\n")

file.close()
