# TODO: Create a letter using starting_letter.txt

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: ht tps://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()

with open("./Input/Letters/starting_letter.txt") as text:
    letter = text.read()
    print(letter)

for name in names:
    # 이름 사이의 빈칸을 줄여주는 것이 필요하다 str으로서 읽지를 못한다 ??\n <- 이것도
    stripped_name = name.strip()
    new_letter = letter.replace("[name]", stripped_name)
    print(new_letter)
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as new_letters:
        new_letters.write(new_letter)

# with open("letter for {name}", mode="w") as new_letter:
#     new_letter.write(f"{letter}")
