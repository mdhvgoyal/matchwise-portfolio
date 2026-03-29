import pandas as pd
import random

roles = ['Software Engineer', 'Data Scientist', 'DevOps'] # job titles
skills = ['Python', 'Docker', 'AWS'] # resume skills

data = []
for i in range(200): # make 5 examples
    resume = f'Exp {random.choice(roles).lower()} - {random.choice(skills)}' # creates: "exp software engineer - Docker"
    job = random.choice(roles) # random job titles
    label = 1 if random.random() > 0.5 else 0 # random match (60% yes)
    data.append({'resume' : resume, 'job' : job, 'label' : label})

df = pd.DataFrame(data)
df.to_csv('data/raw/test.csv', index=False)
print('Data created')
print(df)
