with open("Input/Letters/starting_letter.txt") as letter:
    with open("Input/Names/invited_names.txt") as names:
        for without in names.readlines():
            name = without.strip("\n")
            with open(f"Output/ReadyToSend/letter_for_{name}", mode="w") as output_letter:
                new_file = open("Input/Letters/starting_letter.txt")
                change_name = new_file.read()
                changed = change_name.replace("[name]", name)
                output_letter.write(changed)
