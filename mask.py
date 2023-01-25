import math
import matplotlib.pyplot as plt
import random
from agent import Agent


def main():
    graph()


def random_values(lower_bound, upper_bound):
    val = random.uniform(lower_bound, upper_bound)
    return val


def graph():
    count = 0
    agent_list = create_agents(100, 10, 0)
    all_clear = 0
    susceptible_list = []
    infected_list = []
    recovered_list = []
    print("\t\t\t|Susceptible\t|Infected\t|Recovered")
    print("----------------------------------------------------")
    while all_clear != 50:
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        sick_agents = 0
        susceptible_agents = 0
        recovered_agents = 0
        for a in agent_list:
            if a.get_sick_days() != 0:
                a.set_sick_days(a.get_sick_days() - 1)
            plt.scatter(a.get_x_coordinate(), a.get_y_coordinate(), c=a.get_color(), s=25)
            if a.get_health_status() == "Sick":
                sick_agents += 1
            elif a.get_health_status() == "Susceptible":
                susceptible_agents += 1
            else:
                recovered_agents += 1

            a.move()
        agent_list = check_location(agent_list)

        day = f'Day {count + 1}\t\t'
        infected = f'{sick_agents}\t\t\t\t'
        susceptible = f'{susceptible_agents}\t\t\t\t'
        recovered = f'{recovered_agents}'
        print(day + susceptible + infected + recovered)
        susceptible_list.append(susceptible_agents)
        infected_list.append(sick_agents)
        recovered_list.append(recovered_agents)
        plt.title(f'Agent movement - Day {count + 1}')
        plt.xlabel("x-coordinate")
        plt.ylabel("y-coordinate")
        plt.pause(.1)

        if sick_agents == 0:
            all_clear = False
        else:
            plt.clf()

        count += 1
        all_clear += 1

    graph2(susceptible_list, infected_list, recovered_list, count)


def graph2(susceptible_data, infected_data, recovered_data, days):
    x = []
    for a in range(days):
        x.append(a + 1)
    y = susceptible_data
    y2 = infected_data
    y3 = recovered_data

    fig, ax = plt.subplots()

    ax.plot(x, y, label='Susceptible')
    ax.plot(x, y2, label='Infected')
    ax.plot(x, y3, label='Recovered')
    pos = ax.get_position()
    ax.set_position([pos.x0, pos.y0, pos.width * 0.9, pos.height])
    ax.legend(loc='center right', bbox_to_anchor=(1.25, 0.5))
    plt.xlabel("Days")
    plt.ylabel("Agents")
    plt.title('Mask')
    plt.show()


def check_location(agent_list):
    i = 0

    while i < len(agent_list):
        j = i + 1
        while j < len(agent_list):
            x1 = agent_list[j].get_x_coordinate()
            y1 = agent_list[j].get_y_coordinate()
            x2 = agent_list[i].get_x_coordinate()
            y2 = agent_list[i].get_y_coordinate()
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            while True:
                if distance >= .03:
                    break
                else:
                    agent_list[j].set_x_coordinate(random.uniform(0, 1))
                    agent_list[j].set_y_coordinate(random.uniform(0, 1))
                    x1 = agent_list[j].get_x_coordinate()
                    y1 = agent_list[j].get_y_coordinate()
                    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            if distance <= .04:
                sick_chance = random.uniform(0, 1)
                if agent_list[i].get_color() == "red" and agent_list[j].get_color() == "green":
                    if sick_chance <= .10:
                        agent_list[j].set_health_status("Sick")

                if agent_list[i].get_color() == "green" and agent_list[j].get_color() == "red":
                    if sick_chance <= .10:
                        agent_list[i].set_health_status("Sick")

                if agent_list[i].get_color() == "purple" and agent_list[j].get_color() == "red":
                    if sick_chance <= .05:
                        agent_list[i].set_recovered(True)
                        agent_list[i].set_health_status("Sick")

                if agent_list[i].get_color() == "red" and agent_list[j].get_color() == "purple":
                    if sick_chance <= .05:
                        agent_list[j].set_recovered(True)
                        agent_list[j].set_health_status("Sick")

            j += 1
        i += 1
    return agent_list


def create_agents(size, infected, vaccinated):
    agent_list = []
    count = 0
    for a in range(size):
        agent = Agent()
        agent_list.append(agent)
        if count < infected:
            agent_list[count].set_health_status("Sick")
            count += 1
        elif vaccinated + infected > count >= infected:
            agent_list[count].set_health_status("Recovered/Vaccinated")
            count += 1
    return agent_list


if __name__ == "__main__":
    main()
