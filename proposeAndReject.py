def marry(n, manPreference, womanPreference):
    # Initialize variables
    unmarriedMan = list(range(n))
    ProposalCount = [0] * n
    manSpouse = [None] * n
    womanSpouse = [None] * n

    # While there are unmarried men
    while unmarriedMan:
        print('ManSpouse-', manSpouse)
        print('womanSpouse-', womanSpouse)

        # Get the first unmarried man
        man = unmarriedMan[0]
        # Get the woman the man wants to propose to based on his preference and proposal count
        woman = manPreference[man][ProposalCount[man]]
        # Get the current husband of the woman
        currentHusband = womanSpouse[woman]
        # Get the index of the man in the woman's preference list
        manIndex = womanPreference[woman].index(man)

        print('man-', man)
        print('woman-', woman)

        # If the woman has no current husband
        if currentHusband == None:
            # Set the man and woman as spouses
            womanSpouse[woman] = man
            manSpouse[man] = woman
            # Increment the proposal count for the man
            ProposalCount[man] += 1
            # Remove the man from the list of unmarried men
            unmarriedMan.pop(0)

        # If the man is preferred over the current husband
        elif manIndex < womanPreference[woman].index(currentHusband):
            # Set the man and woman as spouses
            womanSpouse[woman] = man
            manSpouse[man] = woman
            # Increment the proposal count for the man
            ProposalCount[man] += 1
            # Remove the man from the list of unmarried men
            unmarriedMan.pop(0)
            # Add the current husband back to the list of unmarried men
            unmarriedMan.insert(0, currentHusband)

        else:
            # Increment the proposal count for the man
            ProposalCount[man] += 1

    return manSpouse, womanSpouse


if __name__ == '__main__':
    # Test case
    man = [[0, 1, 2], [1, 0, 2], [0, 1, 2]]
    woman = [[1, 0, 2], [0, 1, 2], [0, 1, 2]]
    print(marry(3, man, woman))
