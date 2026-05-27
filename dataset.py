import json
import pandas as pd

with open("hospital_data.json") as f:
    data=json.load(f)

questions=[]
answers=[]

# Location
location_q=[
"where is hospital",
"hospital address",
"location",
"how to reach hospital",
"nearest hospital",
"hospital in pune"
]

questions+=location_q
answers+=[data["address"]]*len(location_q)

# Timing
timing_q=[
"hospital timing",
"opening time",
"closing time",
"working hours",
"is hospital open"
]

questions+=timing_q
answers+=[data["timing"]]*len(timing_q)

# Doctors
doctor_q=[
"doctor list",
"available doctors",
"heart doctor",
"dentist",
"specialist",
"doctor details"
]

questions+=doctor_q
answers+=[
"Doctors: "+
", ".join(
[d["name"] for d in data["doctors"]]
)
]*len(doctor_q)

# Services
service_q=[
"services",
"heart treatment",
"root canal",
"child care",
"brain scan",
"skin treatment"
]

questions+=service_q
answers+=[
", ".join(
data["services"]
)
]*len(service_q)

# Emergency
emergency_q=[
"emergency",
"icu",
"accident case",
"urgent treatment"
]

questions+=emergency_q
answers+=[data["emergency"]]*len(emergency_q)

# Ambulance
ambulance_q=[
"ambulance",
"need ambulance",
"ambulance service"
]

questions+=ambulance_q
answers+=[data["ambulance"]]*len(ambulance_q)

# Insurance
insurance_q=[
"insurance",
"cashless",
"medical insurance"
]

questions+=insurance_q
answers+=[data["insurance"]]*len(insurance_q)

# Contact
contact_q=[
"contact number"
"phone number"
"how to contact hospital"
"hospital contact"
]

questions+=contact_q
answers+=[data["contact"]]*len(contact_q)


# Appointment
appointment_q=[
"appointment",
"book doctor",
"visit doctor"
]

questions+=appointment_q
answers+=[data["appointment"]]*len(appointment_q)

#Create dataset
df=pd.DataFrame({"question":questions,
"answer":answers
})

df.to_csv("hospital_dataset.csv",index=False)


print("Dataset created successfully")