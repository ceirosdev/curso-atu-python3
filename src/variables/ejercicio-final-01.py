persona1 = input('Primera persona: ').strip()
persona2 = input('Segunda persona: ').strip()

personas_ordenadas = sorted([persona1, persona2])

orden = 0

for persona in personas_ordenadas:
    orden += 1
    print(f'{orden}: {persona}')