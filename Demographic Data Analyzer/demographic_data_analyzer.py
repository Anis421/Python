import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series(df['race'].value_counts())

    # What is the average age of men?
    average_age_men = df['age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    bachelor_count = df[df['education'] == 'Bachelors'].shape[0]
    total = df.shape[0]
    percentage_bachelors = bachelor_count / total * 100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    higher_education_df = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_salary_greater_than_50k = higher_education_df[higher_education_df['salary'] == '>50K'].shape[0]
    higher_education_rich = higher_education_salary_greater_than_50k / higher_education_df.shape[0] * 100

    # What percentage of people without advanced education make more than 50K?
    lower_education_df = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_salary_greater_than_50k = lower_education_df[lower_education_df['salary'] == '>50K'].shape[0]
    # percentage with salary >50
    lower_education_rich = lower_education_salary_greater_than_50k / lower_education_df.shape[0] * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / total * 100

    # What country has the highest percentage of people that earn >50K?
    salary_greater_than_50k = df[df['salary'] == '>50K']
    highest_earning_country = salary_greater_than_50k['native-country'].value_counts().idxmax()
    highest_earning_country_percentage = salary_greater_than_50k['native-country'].value_counts().max() / total * 100


    # Identify the most popular occupation for those who earn >50K in India.
    india_50k = salary_greater_than_50k[salary_greater_than_50k['native-country'] == 'India']
    top_in_occupation = india_50k['occupation'].value_counts().idxmax()
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors:.10f}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich:.10f}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich:.10f}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage:.10f}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage:.10f}%")
        print("Top occupations in India:", top_in_occupation)

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
        'top_IN_occupation': top_in_occupation
    }