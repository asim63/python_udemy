
with open(r"Day 24\Mail Merge Project Start\Input\Letters\starting_letter.txt") as file:
    with open(r"Day 24\Mail Merge Project Start\Input\Names\invited_names.txt") as name_file:
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
    
        