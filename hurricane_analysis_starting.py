# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
conversion = {"M": 1000000,
              "B": 1000000000}

updated_damages = []
def convert_updated_damages(damages):
    for damage in damages:
        if damage[-1] == "M":
            damage = damage.split("M")[0]
            updated_damages.append(float(damage) * conversion["M"])
        elif damage[-1] == "B":
            damage = damage.split("B")[0]
            updated_damages.append(float(damage) * conversion["B"])
        else:
            updated_damages.append(damage)
    return updated_damages
updated_damages = convert_updated_damages(damages)
print(f"Updated Damages: {updated_damages}")





# write your construct hurricane dictionary function here:
hurricanes = {}
def construct_hurricane(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    for i in range(0, len(names)):
        hurricanes[names[i]] = {"Names": names[i],
                                "Months": months[i],
                                "Years": years[i],
                                "Max_sustained_winds": max_sustained_winds[i],
                                "Areas affected": areas_affected[i],
                                "Damages": updated_damages[i],
                                "Deaths": deaths[i]}
    return hurricanes
hurricanes = construct_hurricane(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(f"\nHurricanes: {hurricanes}")


# write your construct hurricane by year dictionary function here:
hurricanes_by_year = {}
def construct_hurricane_by_year(hurricanes):
    for num in hurricanes:
        current_year = hurricanes[num]["Years"]
        current_cane = hurricanes[num]
        if current_year not in hurricanes_by_year.keys():
            hurricanes_by_year[current_year] = [current_cane]
        elif current_year in hurricanes_by_year.keys():
            hurricanes_by_year[current_year].append(current_cane)
    return hurricanes_by_year
hurricanes_by_year = construct_hurricane_by_year(hurricanes)
print(f"\nHurricanes by year: {hurricanes_by_year}")


# write your count affected areas function here:
highly_affected_areas = {}
def count_affected_areas(hurricanes):
    for num in hurricanes:
        for area in hurricanes[num]["Areas affected"]:
            if area not in highly_affected_areas.keys():
                count = 1
                highly_affected_areas[area] = count
            elif area in highly_affected_areas.keys():
                count += 1
                highly_affected_areas[area] = count
    return highly_affected_areas
highly_affected_areas = count_affected_areas(hurricanes)
print(f"\nHighly affected areas count: {highly_affected_areas}")


# write your find most affected area function here:
max_area = ""
max_area_count = 0
def most_affected_area(highly_affected_areas, max_area, max_area_count):
    for key, value in highly_affected_areas.items():
        if value > max_area_count:
            max_area = key
            max_area_count = value
    return max_area, max_area_count
max_area = most_affected_area(highly_affected_areas, max_area, max_area_count)[0]
max_area_count = most_affected_area(highly_affected_areas, max_area, max_area_count)[1]
print(f"\nMost affected area: {max_area}")
print(f"Number of times affected: {max_area_count}")


# write your greatest number of deaths function here:
max_mortality_cane = ""
max_mortality = 0
def greatest_numbers_of_deaths(hurricanes, max_mortality_cane, max_mortality):
    for key, value in hurricanes.items():
        if value["Deaths"] > max_mortality:
            max_mortality_cane = key
            max_mortality = value["Deaths"]
    return max_mortality_cane, max_mortality
max_mortality_cane = greatest_numbers_of_deaths(hurricanes, max_mortality_cane, max_mortality)[0]
max_mortality = greatest_numbers_of_deaths(hurricanes, max_mortality_cane, max_mortality)[1]
print(f"\nMax mortality hurricane: {max_mortality_cane}")
print(f"Max mortality count: {max_mortality}")


# write your categorize by mortality function here:
hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
def category_by_mortality(hurricanes):
    for key, value in hurricanes.items():
        if value["Deaths"] == 0:
            hurricanes_by_mortality[0].append(key)
        elif value["Deaths"] > 0 and value["Deaths"] <= 100:
            hurricanes_by_mortality[1].append(key)
        elif value["Deaths"] > 100 and value["Deaths"] <= 500:
            hurricanes_by_mortality[2].append(key)
        elif value["Deaths"] > 500 and value["Deaths"] <= 1000:
            hurricanes_by_mortality[3].append(key)
        elif value["Deaths"] > 1000 and value["Deaths"] <= 10000:
            hurricanes_by_mortality[4].append(key)
        elif value["Deaths"] > 10000:
            hurricanes_by_mortality[5].append(key)
    return hurricanes_by_mortality
hurricanes_by_mortality = category_by_mortality(hurricanes)
print(f"\nHurricanes by Mortality Scale: {hurricanes_by_mortality}")


# write your greatest damage function here:
max_damage_cane = ""
max_damage = 0
def greatest_damages(hurricanes, max_damage_cane, max_damage):
    for key, value in hurricanes.items():
        if value["Damages"] == "Damages not recorded":
            continue
        elif value["Damages"] > max_damage:
            max_damage_cane = key
            max_damage = value["Damages"]
    return max_damage_cane, max_damage
max_damage_cane = greatest_damages(hurricanes, max_damage_cane, max_damage)[0]
max_damage = greatest_damages(hurricanes, max_damage_cane, max_damage)[1]
print(f"\nMax damage hurricane: {max_damage_cane}")
print(f"Maximum damage: {max_damage}")


# write your catgeorize by damage function here:
hurricanes_by_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
def category_by_damage(hurricanes):
    for key, value in hurricanes.items():
        if value["Damages"] == "Damages not recorded":
            continue
        elif value["Damages"] == 0:
            hurricanes_by_damage[0].append(key)
        elif value["Damages"] >0 and value["Damages"] <= 100000000:
            hurricanes_by_damage[1].append(key)
        elif value["Damages"] >100000000 and value["Damages"] <= 1000000000:
            hurricanes_by_damage[2].append(key)
        elif value["Damages"] >1000000000 and value["Damages"] <= 10000000000:
            hurricanes_by_damage[3].append(key)
        elif value["Damages"] >10000000000 and value["Damages"] <= 50000000000:
            hurricanes_by_damage[4].append(key)
        elif value["Damages"] >50000000000:
            hurricanes_by_damage[5].append(key)
    return hurricanes_by_damage
hurricanes_by_damage = category_by_damage(hurricanes)
print(f"\nHurricanes by Damage Scale: {hurricanes_by_damage}")