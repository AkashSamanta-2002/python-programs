def age_validation(age):
    if age >= 18:
        print("Eligible for voting")
    else:
        raise Exception("Not eligible for voting")

while True:
    age = int(input("Enter your age: "))

    try:
        age_validation(age)
    except Exception as err:
        print(f"There is an exception: {err}")
    finally:
        end = input("Do you want to continue? (Y/N): ")
        if(end == "N" or end == "n"):
            break