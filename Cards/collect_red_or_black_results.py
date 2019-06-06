import time
import datetime
import csv
from Cards.Red_or_black import *

start_time = time.time()

# create/open csv to write results to
results_csv = open('results.csv', mode='a')
results_writer = csv.writer(results_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
results_writer.writerow(['number of correct guesses', 'repeat number', 'time up to now'])  # create header
results_csv.close()

results = []
max_trials = 1000000  # how many cards drawn per repeat
repeats = 1000  # how many times to repeat
while len(results) < repeats:
    trials = 0
    correct = 0
    while trials <= max_trials:
        d = Deck()
        random.shuffle(d.deck)
        first_card = d.deck.pop(0)
        # guess opposite of the colour of the first card
        if first_card.colour == 'red':
            guess = 'black'
        else:
            guess = 'red'
        if red_or_black(d, guess):
            correct += 1
        del d
        trials += 1
    current_time = time.time()
    time_taken = str(datetime.timedelta(seconds=(current_time - start_time)))
    if len(results) % 100 == 0:  # check in every 100 runs by printing time taken to this point
        print(time_taken)
    results.append(correct)  # add the result to the list
    results_csv = open('results.csv', mode='a')
    results_writer = csv.writer(results_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,
                                lineterminator='\n')
    results_writer.writerow([str(correct), str(len(results)), time_taken])  # record results to csv
    results_csv.close()

# do some stats
print(f'Average = {sum(results) / len(results)}')
print(f'Results collected = {len(results)}')
print(f'Cards guesses attempted = {max_trials * repeats}')
print(f'Cards guessed correctly = {sum(results)}')

# how long has the entire program taken?
end_time = time.time()
time_diff = end_time - start_time
time_taken = datetime.timedelta(seconds=time_diff)
print(time_taken)
