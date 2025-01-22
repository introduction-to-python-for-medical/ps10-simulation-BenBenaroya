import copy

def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    grid_size = len(grid)  # נניח שהגריד הוא ריבועי
    update_grid = copy.deepcopy(grid)

    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:  # תא של עץ (1)
                # בדיקה אם יש שכן בוער (2)
                neighbors = []
                if i > 0: 
                    neighbors.append(grid[i-1][j])  # למעלה
                if i < grid_size-1: 
                    neighbors.append(grid[i+1][j])  # למטה
                if j > 0: 
                    neighbors.append(grid[i][j-1])  # שמאלה
                if j < grid_size-1: 
                    neighbors.append(grid[i][j+1])  # ימינה
                
                # אם יש שכן בוער, האש מתפשטת
                if 2 in neighbors:
                    update_grid[i][j] = 2

    return update_grid
