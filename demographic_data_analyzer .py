import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv', delimiter=',')

    frame = pd.DataFrame(data=df, columns=['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status',
     'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'])

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race = frame['race']
    races = {}
    for i in race:
        if i not in races:
            races[i] = 1

        else:
            number = races[i] 
            races[i] = number + 1

    race_count = pd.Series(races)

    male_age = frame.loc[frame['sex'] == 'Male', 'age']
    ages = []
    for age in male_age:
        ages.append(age)
    age = pd.Series(ages)
    average_age_men = round(age.mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    education = frame.loc[frame['education'] == 'Bachelors']
    percentage_bachelors = round((len(education) / len(frame['age']) * 100), 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    bachelors = frame.loc[frame['education'] == 'Bachelors', 'salary']
    masters = frame.loc[frame['education'] == 'Masters', 'salary']
    doctorate = frame.loc[frame['education'] == 'Doctorate', 'salary']

    higher_education = len(bachelors) + len(masters) + len(doctorate)
    lower_education = len(frame['age']) - higher_education

    rich_educated = 0
    total = 0
    for salary in bachelors:
        total += 1
        if salary == '>50K':
            rich_educated += 1

    for salary in masters:
        total += 1
        if salary == '>50K':
            rich_educated += 1

    for salary in doctorate:
        total += 1
        if salary == '>50K':
            rich_educated += 1
        
    over_50k = len(frame.loc[frame['salary'] == '>50K'])


    # percentage with salary >50K
    higher_education_rich = round(((rich_educated / total) * 100), 1)
    lower_education_rich = round(((over_50k - rich_educated)/ lower_education) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = frame['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    min_hours_salary = frame.loc[frame['hours-per-week'] == 1, 'salary']

    num_min_workers = len(min_hours_salary)
    rich_minimum = 0
    for salary in min_hours_salary:
        if salary == '>50K':
            rich_minimum += 1

    rich_percentage = round((rich_minimum / num_min_workers) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_countries = frame.loc[frame['salary'] == '>50K', 'native-country']
    countries = {}
    for country in highest_earning_countries:
        if country not in countries:
            countries[country] = 1
        else:
            number = countries[country]
            countries[country] = number + 1
    richest_country = ''
    percentage_of_rich = 0

    for key, value in countries.items():
        if value / len(frame.loc[frame['native-country'] == key]) > percentage_of_rich:
            richest_country = key
            percentage_of_rich = value / len(frame.loc[frame['native-country'] == key])
    highest_earning_country = richest_country
    highest_earning_country_percentage = round(percentage_of_rich * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.

    india = frame.loc[frame['native-country'] == 'India', ['salary', 'occupation']]
    jobs = india.loc[india['salary'] == '>50K', 'occupation']
    job_names = {}
    for job in jobs:
        if job not in job_names:
            job_names[job] = 1
        else:
            number = job_names[job]
            job_names[job] = number + 1
    
    most = 0
    top_job = ''
    for key, value in job_names.items():
        if value > most:
            most = value
            top_job = key

    top_IN_occupation = top_job

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
