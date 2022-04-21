gross_income=int(input("Please enter gross income"))
nod=int(input("Please enter no. of dependents"))
taxincome= gross_income-10000-(3000*nod)
tax=taxincome*0.2
print("Your tax is ", tax)
