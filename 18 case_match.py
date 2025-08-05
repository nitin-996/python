fruit = ['mango','orange','apple']


# for new_fruit in fruit:
    
match fruit[1]:
        case "mango":
            print(f"{fruit[0]} is here")
            # break

            # default
        case _:
            print("no fruit found")    


