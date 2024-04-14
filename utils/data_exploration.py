import pandas as pd
from datetime import datetime
pd.options.mode.chained_assignment = None

seven_dwarfs = pd.read_csv("./dataset/7_dwarfs_train.csv")
alien_saurcers = pd.read_csv("./dataset/alien_saucers.csv")
dinosaur = pd.read_csv("./dataset/dinosaur.csv")
everest = pd.read_csv("./dataset/expedition_everest.csv")
flight_of_passage = pd.read_csv("./dataset/kilimanjaro_safaris.csv")
kilimanjaro = pd.read_csv("./dataset/kilimanjaro_safaris.csv")
navi_river = pd.read_csv("./dataset/navi_river.csv")
pirates_carribean = pd.read_csv("./dataset/pirates_of_caribbean.csv")
rock_n_roller = pd.read_csv("./dataset/rock_n_rollercoaster.csv")
slinky_dog = pd.read_csv("./dataset/slinky_dog.csv")
soarin = pd.read_csv("./dataset/soarin.csv")
spaceship = pd.read_csv("./dataset/spaceship_earth.csv")
splash_mount = pd.read_csv("./dataset/splash_mountain.csv")
toy_story = pd.read_csv("./dataset/toy_story_mania.csv")

def date_to_integer(date):
    current_date = pd.to_datetime(date)
    start_date = datetime(2024, 1, 1)
    delta = current_date - start_date
    return delta.days + 1

def average_wait_time(df):
    df = df.dropna(subset = ['SPOSTMIN'])
    df = df[df['SPOSTMIN'] != -999]
    df['datetime'] = pd.to_datetime(df['datetime'])
    df['hour'] = df['datetime'].dt.hour
    df['month'] = df['datetime'].dt.month
    df['day'] = df['datetime'].dt.day
    
    result = df.groupby(['month','day', 'hour'])["SPOSTMIN"].mean().reset_index()
    result['year'] = 2024
    result['date'] = result['year'].astype(str) + '-' + result['month'].astype(str).str.zfill(2) + '-' + result['day'].astype(str).str.zfill(2)
    result['date'] = result['date'].apply(date_to_integer)
    result = result.drop(['year', 'month', 'day'], axis = 1)
    result.columns = ['hour', 'avg_wait_time', 'date']

    return result

seven_dwarfs = average_wait_time(seven_dwarfs)
alien_saurcers = average_wait_time(alien_saurcers)
dinosaur = average_wait_time(dinosaur)
everest = average_wait_time(everest)
flight_of_passage = average_wait_time(flight_of_passage)
kilimanjaro = average_wait_time(kilimanjaro)
navi_river = average_wait_time(navi_river)
pirates_carribean = average_wait_time(pirates_carribean)
rock_n_roller = average_wait_time(rock_n_roller)
slinky_dog = average_wait_time(slinky_dog)
soarin = average_wait_time(soarin)
spaceship = average_wait_time(spaceship)
splash_mount = average_wait_time(splash_mount)
toy_story = average_wait_time(toy_story)

seven_dwarfs.loc[:, 'ride'] = "seven_dwarfs"
alien_saurcers.loc[:, 'ride'] = "alien_saurcers"
dinosaur.loc[:, 'ride'] = "dinosaur"
everest.loc[:, 'ride'] = "everest"
flight_of_passage.loc[:, 'ride'] = "flight_of_passage"
kilimanjaro.loc[:, 'ride'] = "kilimanjaro"
navi_river.loc[:, 'ride'] = "navi_river"
pirates_carribean.loc[:, 'ride'] = "pirates_carribean"
rock_n_roller.loc[:, 'ride'] = "rock_n_roller"
slinky_dog.loc[:, 'ride'] = "slinky_dog"
soarin.loc[:, 'ride'] = "soarin"
spaceship.loc[:, 'ride'] = "spaceship"
splash_mount.loc[:, 'ride'] = "splash_mount"
toy_story.loc[:, 'ride'] = "toy_story"

rides = [seven_dwarfs,
        alien_saurcers,
        dinosaur, 
        everest, 
        flight_of_passage, 
        kilimanjaro, 
        navi_river,
        pirates_carribean, 
        rock_n_roller, 
        slinky_dog, 
        soarin,
        spaceship,
        splash_mount,
        toy_story]


disney_rides = pd.concat(rides, ignore_index = True)
disney_rides.to_csv('./dataset/disney_rides.csv', index = False)