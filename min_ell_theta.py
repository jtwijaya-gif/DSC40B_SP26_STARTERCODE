def learn_theta(data, colors):
    '''
    Finds theta that is larger than all blue and less than all red.
    '''
    largest_blue = None

    for i in range(len(data)):
        if colors[i] == 'blue':
            if largest_blue is None or data[i] > largest_blue:
                largest_blue = data[i]

    return largest_blue


def compute_ell(data, colors, theta):
    '''
    Computes the loss function L(theta) for a given theta.
    '''
    loss = 0

    for i in range(len(data)):
        if colors[i] == 'red' and data[i] <= theta:
            loss += 1
        elif colors[i] == 'blue' and data[i] > theta:
            loss += 1

    return float(loss)


def minimize_ell(data, colors):
    '''
    Finds theta that minimizes the loss function L(theta) using quadratic time complexity.
    '''
    best_theta = data[0]
    best_loss = compute_ell(data, colors, best_theta)

    for theta in data:
        loss = compute_ell(data, colors, theta)

        if loss < best_loss:
            best_loss = loss
            best_theta = theta

    return float(best_theta)


def minimize_ell_sorted(data, colors):
    '''
    Finds theta that minimizes the loss function L(theta) in linear time.
    '''
    blue_gt_theta = 0

    for color in colors:
        if color == 'blue':
            blue_gt_theta += 1

    red_leq_theta = 0
    best_theta = data[0]
    best_loss = red_leq_theta + blue_gt_theta

    for i in range(len(data)):
        if colors[i] == 'blue':
            blue_gt_theta -= 1
        else:
            red_leq_theta += 1

        loss = red_leq_theta + blue_gt_theta

        if loss < best_loss:
            best_loss = loss
            best_theta = data[i]

    return float(best_theta)