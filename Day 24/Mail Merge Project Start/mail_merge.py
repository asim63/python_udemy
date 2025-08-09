#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        

with open(r"Day 24\Mail Merge Project Start\Input\Letters\starting_letter.txt", mode = 'r') as file:
    with open(r"Day 24\Mail Merge Project Start\Input\Names\invited_names.txt",mode = 'r') as name_file:
        name_list = name_file.readlines()
        text = file.read()
        # print(text)
        # print(name_list)
        for name in name_list:
            name = name.strip()
            # print(name)
            print(name)
            new_text = text.replace("[name],", name)
            with open(f"Day 24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", mode = 'w') as new_file:
                new_file.write(new_text)
    
        