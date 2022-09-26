gender = float(input("Enter hemoglobin value:"))


if gender >=134:
    print("Hemoglobin value is low for male but normal for female")
if gender >167:
    print("Hemoglobin value is both  high for male and female")
if gender ==156-167:
    print("Hemoglobin value is normal for male but high for female ")
if gender <117:
    print("Hemogloibn value is both low for male and female")
