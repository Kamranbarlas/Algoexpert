import time
def tournamentWinner(competitions, results):
    # Write your code here.
    start_time = time.time()
    winners = {}
    for i in range(len(competitions)):
        # print(competitions[i])
        print(i,"index")
        if 0 == results[i]:
            if competitions[i][1] not in winners:
                winners[competitions[i][1]] = 1
                print("1",winners,competitions[i][1])
            else:
                winners[competitions[i][1]] += 1
        elif 1 == results[i]:
            if competitions[i][0] not in winners:
                winners[competitions[i][0]] = 1
                print("2",winners,competitions[i][0] )
            else:
                winners[competitions[i][0]] += 1
            
        # else:
        #     winners[competitions[i][0]] += 1
        #     print("2 ..",winners)
    print(winners,"++++++++++++++")
    key_max = max(zip(winners.values(),winners.keys()))[1]
    end_time = time.time()
    print("Original Function Execution Time:", end_time - start_time)
    return key_max

#chatgpt answer
def tournamentWinner(competitions, results):
    winners = {}
    current_best_team = ""
    current_best_score = 0

    for i in range(len(competitions)):
        winning_team = competitions[i][1 - results[i]]

        winners[winning_team] = winners.get(winning_team, 0) + 1

        if winners[winning_team] > current_best_score:
            current_best_team = winning_team
            current_best_score = winners[winning_team]

    return current_best_team
