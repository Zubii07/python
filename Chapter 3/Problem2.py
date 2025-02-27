# Write a program to fill in a letter template given below with name and date.

letter = '''Dear <|Name|>,
            You are selected!
            <|Date|>'''

print(letter.replace("<|Name|>", "Zohaib").replace("<|Date|>", "27-02-2025"))