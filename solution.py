import json


def create_head_to_head(json_file: str):
    """
    Creates a table of teams' records head-to-head

    :param json_file: file containing teams' records vs every other team
    :return: 2D array
    """
    file = open(json_file)
    data = json.load(file)

    teams = ["--"] + list(data.keys())
    table = [["--" for i in range(0, len(teams))] for x in range(0, len(teams))]

    for index, value in enumerate(teams):
        table[0][index] = value
        table[index][0] = value

    for i in range(1, len(table)):
        team = table[i][0]
        record = data[team]
        for k in range(1, len(table)):
            if table[0][k] == team:
                continue
            table[i][k] = record[table[0][k]]["W"]

    return table


print(create_head_to_head("example.json"))
