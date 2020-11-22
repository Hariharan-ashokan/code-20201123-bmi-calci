import data
import HealthRiskReference

user_data = data.data
ref_table = HealthRiskReference.bmi_reference

def add_into_dict(d,k,v):
    d.update({k:v})

def write_file(data, file_name):
    with open(file_name, mode='w') as write_file:
        write_file.write(str(data))
        write_file.close()


for d in user_data:
    height_in_meter_sq = pow(d["HeightCm"]/100, 2)
    weight = d["WeightKg"]
    bmi = round((weight/height_in_meter_sq), 2)
    for vd in ref_table.values():
        range = vd["range"]
        if range[0] <= bmi <= range[1]:
            bmi_category = vd["bmi_category"]
            health_risk = vd["health_risk"]
            add_into_dict(d, "Body Mass Index", bmi)
            add_into_dict(d, "BMI Category", bmi_category)
            add_into_dict(d, "Health Risk", health_risk)
            write_file(str(user_data),"output.txt")


overweight_people = 0

for d in user_data:
    if d["BMI Category"] == "Overweigth":
        overweight_people+=1

print("No of Overweight people {}".format(overweight_people))

