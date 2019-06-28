#Import modules
import os
import csv

# #Define path to data file
employee_csv = os.path.join('.', 'employee_data.csv')

#Open data file and pass to csvreader obtain list of first name
with open(employee_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    first_name = [row[1].split()[0] for row in csvreader]

#Open data file and pass to csvreader obtain list of last name
with open(employee_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    last_name = [row[1].split()[1] for row in csvreader]

#Open data file and pass to csvreader obtain list of DOB
with open(employee_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    DOB = [row[2] for row in csvreader]

#Open data file and pass to csvreader obtain list of EMP ID
with open(employee_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    emp_id = [row[0] for row in csvreader]

#Open data file and pass to csvreader obtain list of revised SSN
with open(employee_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    ssn = ['***-**-' + row[3].split('-')[2] for row in csvreader]

#Dictionary of State names to Abbrev, taken form external py file but I was not able to figure out how to utilize that file so copied and pasted in the dictionary.
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#Open data file and pass to csvreader obtain list of State abbreviations

with open(employee_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    state = [us_state_abbrev.get(row[4]) for row in csvreader]

#zip previously created lists into 'rows'
rows = zip(emp_id, first_name, last_name, DOB, ssn, state)

#write headers and 'rows' to csv file
with open('employee_cleaned.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
            for row in rows:
                writer.writerow(row)




