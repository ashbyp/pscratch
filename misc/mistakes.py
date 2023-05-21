import pandas as pd



def csv_mistake():
    df = pd.DataFrame(
        {
            'name':    ['tom', 'dick', 'harriet'],
            'age':     [25,     30,    28],
            "gender":  ['male', 'male', 'female']
        }
    )
    print(df)
    # don't write useless indices
    df.to_csv("test.csv", index=False)


def spaces_mistake():
    df = pd.DataFrame(
        {
            'name': ['tom', 'dick', 'harriet'],
            'age': [25, 30, 28],
            'gender': ['male', 'male', 'female'],
            'job code': [10, 15, 11]
        }
    )
    print(df)
    print(df[['job code']])

    df = pd.DataFrame(
        {
            'name': ['tom', 'dick', 'harriet'],
            'age': [25, 30, 28],
            'gender': ['male', 'male', 'female'],
            'job_code': [10, 15, 11]
        }
    )
    print(df.job_code)


def mistake_not_using_query():
    df = pd.DataFrame(
        {
            'name': ['tom', 'dick', 'harriet', 'joe'],
            'age': [25, 30, 28, 51],
            'gender': ['male', 'male', 'female', 'male'],
            'job_code': [10, 15, 11, 10]
        }
    )
    x = df.loc[(df['age'] > 27) & (df['age'] < 50)]
    print(x)

    lower, upper = 27, 50
    y = df.query('age > @lower and age < @upper')
    print(y)
    print(x == y)
    print(type(x), type(y))

def mistake_not_chaining():
    df = pd.DataFrame(
        {
            'name': ['tom', 'dick', 'harriet', 'joe'],
            'age': [25, 30, 28, 51],
            'gender': ['male', 'male', 'female', 'male'],
            'job_code': [10, 15, 11, 10]
        }
    )
    df['job_code_gender'] = df['age'] + df['job_code']
    df['gcode'] = df['gender'].str.upper()[0]
    upper = 50
    x = df.query('age < @upper')
    print(x)
    y = x.groupby('gender')['age'].mean()
    print(y)


def main():
    # csv_mistake()
    # spaces_mistake()
    mistake_not_chaining()


if __name__ == '__main__':
    main()
