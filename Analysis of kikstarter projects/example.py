import argparse
import cPickle
import datetime
import numpy as np
import csv
from datetime import datetime
import pandas as pd

def load_binary(file_name):
    with open(file_name, 'rb') as f:
        return cPickle.load(f)


def load_data(args):
    print 'Loading projects...'
    projects = np.load('%s/projects.npy' % (args.data_dir, ))
    print 'Loading statuses...'
    statuses = load_binary('%s/statuses.pkl' % (args.data_dir, ))
    print 'Loading tweets...'
    tweets = np.load('%s/tweets.npy' % (args.data_dir, ))
    print 'Loading graph...'
    graph = np.load('%s/graph.pkl' % (args.data_dir, ))

    # conver to numpy arrays if needed
    statuses = np.array(statuses)

    return projects, tweets, statuses, graph


def print_example(args):
    projects, tweets,statuses, graph = load_data(args)

    print '%d projects loaded.' % (len(projects))

    print '#' * 10

    print 'First project:'
    print '\tId:', projects[0, 0]
    print '\tGoal:', projects[0, 1]
    print '\tState:', 'successful' if projects[0, 2] == 1 else 'failed'
    print '\tLaunch:', projects[0, 3] # unix timestamp
    print '\tDeadline:', projects[0, 4] # unix timestamp


    with open('projects.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';')
        spamwriter.writerow(['Id', 'Goal', 'State', 'Launch', 'Deadline'])
        for i in range(0, len(projects)):
            project_id = projects[i, 0]
            goal = projects[i, 1]
            state = 'successful' if projects[i, 2] == 1 else 'failed'
            launch = datetime.fromtimestamp(projects[i, 3]).strftime('%d.%m.%Y, %H:%M:%S')
            deadline = datetime.fromtimestamp(projects[i, 4]).strftime('%d.%m.%Y, %H:%M:%S')
            spamwriter.writerow([project_id, goal, state, launch, deadline])

    print '#' * 10

    print '10th status of the first project:'
    print '\tTime:', statuses[0, 9, 0]
    print '\tTrue time:', statuses[0, 0, 0] * (projects[0, 4] - projects[0, 3]) \
            + projects[0, 3]
    print '\tPledged money:', statuses[0, 9, 1]
    print '\tNumber of backers:', statuses[0, 9, 2]

    with open('statuses.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';')
        spamwriter.writerow(['Id', 'Time', 'True time', 'Pledged money', 'Number of backers'])
        for i in range(0, len(projects)):
            for j in range(0, len(statuses[i])):
                project_id = i
                time = statuses[i, j, 0]
                true_time = datetime.fromtimestamp(statuses[0, 0, 0] * (projects[i, 4] - projects[i, 3]) + projects[i, 3]).strftime('%d.%m.%Y, %H:%M:%S')
                pledged_money = statuses[i, j, 1]
                backers = statuses[i, j, 2]
                spamwriter.writerow([project_id, time, true_time, pledged_money, backers])
    print '#' * 10

    print '200th sample of tweets of the 20th project:'
    print '\tTime:', tweets[19, 199, 0]
    print '\tNumber of tweets:', tweets[19, 199, 1]
    print '\tNumber of replies:', tweets[19, 199, 2]
    print '\tNumber of retweets:', tweets[19, 199, 3]
    print '\tEstimated number of backers:', tweets[19, 199, 4]
    print '\tNumber of users who tweeted:', tweets[19, 199, 5]

    print '#' * 10

    project_id = projects[0, 0]
    print 'Backers of project %d:' % (project_id, )
    print graph[project_id]

    backer_id = graph[project_id][0]
    print 'Projects backed by user %d:' % (backer_id, )
    print graph[backer_id]




if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('data_dir',
            help="Folder where the data files are located")

    args = parser.parse_args()
    
    print_example(args)
