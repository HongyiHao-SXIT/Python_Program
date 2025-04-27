current_population = 307357870

birth_rate = 7

death_rate = 13

immigration_rate = 35

seconds_per_year = 365 * 24 * 60 * 60

years = int(input("Please enter the number of years (as an integer): "))

births = (seconds_per_year * years) // birth_rate

deaths = (seconds_per_year * years) // death_rate

immigrants = (seconds_per_year * years) // immigration_rate

estimated_population = current_population + births - deaths + immigrants

print(f"Estimated population after {years} years: {estimated_population} people")