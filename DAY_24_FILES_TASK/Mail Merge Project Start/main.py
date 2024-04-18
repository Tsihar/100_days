#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    names_list = names.readlines()


with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
    letter_text = letter.read()
    for name in names_list:
        mod_item = name.strip()
        new_text = letter_text.replace("[name]", mod_item)
        with open(f"../Mail Merge Project Start/Output/ReadyToSend/letter_for_{mod_item}.txt", "w") as file:
            file.write(new_text)


