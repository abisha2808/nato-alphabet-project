import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data1 = pandas.DataFrame(data)
# print(data1)
new_dict = {row.letter: row.code for (index, row) in data1.iterrows()}
print(new_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_nato():
    answer = input("enter the name: ").upper()

    try:
        list1 = [new_dict[letters] for letters in answer]

    except KeyError:
        print("Sorry, Only letters in alphabet please.")
        generate_nato()
    else:
        print(list1)

generate_nato()