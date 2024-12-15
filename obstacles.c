#include <stdio.h>

#define MAX_ROW         10
#define MAX_COL         10
#define MAX_OBSTACLES   100
#define IN              1
#define OUT             0

typedef enum 
{
    UP = 0,    
    RIGHT,
    DOWN,
    LEFT
} Direction;

typedef struct 
{
    int row;
    int col;
} Position;

char InputArr[MAX_ROW][MAX_COL] = {
    {'.', '.', '.', '.', '#', '.', '.', '.', '.', '.'}, 
    {'.', '.', '.', '.', '.', '.', '.', '.', '.', '#'},
    {'.', '.', '.', '.', '.', '.', '.', '.', '.', '.'}, 
    {'.', '.', '#', '.', '.', '.', '.', '.', '.', '.'}, 
    {'.', '.', '.', '.', '.', '.', '.', '#', '.', '.'}, 
    {'.', '.', '.', '.', '.', '.', '.', '.', '.', '.'}, 
    {'.', '#', '.', '.', '^', '.', '.', '.', '.', '.'}, 
    {'.', '.', '.', '.', '.', '.', '.', '.', '#', '.'}, 
    {'#', '.', '.', '.', '.', '.', '.', '.', '.', '.'}, 
    {'.', '.', '.', '.', '.', '.', '#', '.', '.', '.'}
};

// 0,4  1,9  3,2  4,7  6,1  7,8  8,0  9,6  
Position Obstacles[MAX_OBSTACLES];
Direction ObstDirection[MAX_OBSTACLES];
int ObstCount = 0;
int NumOfSteps = 0;

Position NewObstacles[MAX_OBSTACLES];
int NewObstCount = 0;

int getObstacles(Position *Obstacles)
{
    int irow, icol, count = 0;

    for (irow = 0; irow < MAX_ROW; irow++)
    {
        for (icol = 0; icol < MAX_COL; icol++)
        {
            if (InputArr[irow][icol] == '#')
            {
                Obstacles[count].row = irow;
                Obstacles[count].col = icol;
                count++;
            }
        }
    }
    return count;
}

void printObstacles(Position *Obstacles, int count)
{
    int irow = 0;

    for (irow = 0; irow < count; irow++)
    {
        printf("%d,%d  ", Obstacles[irow].row, Obstacles[irow].col);
    }        
}

void getGuardPos(Position *guard)
{
    int irow, icol, count = 0;

    for (irow = 0; irow < MAX_ROW; irow++)
    {
        for (icol = 0; icol < MAX_COL; icol++)
        {
            if (InputArr[irow][icol] == '^')
            {
                guard->row = irow;
                guard->col = icol;                
            }
        }
    }
}

int IsObstacleFound(Position currentPos, Position *newPos, Direction curMove, Direction *nextMove)
{
    int irow = currentPos.row, icol = currentPos.col, count = 0;
    int status = IN;    

    switch (curMove)
    {
        case UP:            
            while (1)
            {
                if ((irow - 1) < 0)
                {
                    return OUT;
                }
                irow--;                
                if (InputArr[irow][icol] == '.')
                {
                    if (irow == 0)
                    {
                        return OUT;
                    }  
                    NumOfSteps++;                  
                    continue;                
                }
                else if (InputArr[irow][icol] == '#')
                {                   
                    Obstacles[ObstCount].row = irow;
                    Obstacles[ObstCount].col = icol;
                    ObstDirection[ObstCount] = UP;
                    ObstCount++;
                    if ((icol + 1) >= MAX_COL)
                    {
                        return OUT;
                    }
                    NumOfSteps++;
                    newPos->row = ++irow;
                    newPos->col = ++icol;
                    *nextMove = RIGHT;                    
                    return IN;
                }               
            } // end of while (1)
            break;

        case RIGHT:            
            while (1)
            {
                if ((icol + 1) >= MAX_COL)
                {
                    return OUT;
                }            
                icol++;    
                
                if (InputArr[irow][icol] == '.')
                {
                    if (icol == (MAX_COL - 1))
                    {
                        return OUT;
                    }
                    NumOfSteps++;
                    continue;                
                }
                else if (InputArr[irow][icol] == '#')
                {                   
                    Obstacles[ObstCount].row = irow;
                    Obstacles[ObstCount].col = icol;
                    ObstDirection[ObstCount] = RIGHT;
                    ObstCount++;
                    
                    if ((irow + 1) >= MAX_ROW)
                    {
                        return OUT;
                    }
                    NumOfSteps++;
                    newPos->row = ++irow;
                    newPos->col = --icol;
                    *nextMove = DOWN;                    
                    return IN;
                }               
            } // end of while (1)
            break;

        case DOWN:
            while (1)
            {
                if ((irow + 1) >= MAX_ROW)
                {
                    return OUT;
                }
                irow++;
                
                if (InputArr[irow][icol] == '.')
                {
                    if (irow == (MAX_ROW - 1))
                    {
                        return OUT;
                    }
                    NumOfSteps++;
                    continue;                
                }
                else if (InputArr[irow][icol] == '#')
                {     
                    Obstacles[ObstCount].row = irow;
                    Obstacles[ObstCount].col = icol;
                    ObstDirection[ObstCount] = DOWN;
                    ObstCount++;

                    if ((icol - 1) == 0)
                    {
                        return OUT;
                    }
                    NumOfSteps++;
                    newPos->row = --irow;
                    newPos->col = --icol;
                    *nextMove = LEFT;                    
                    return IN;
                }               
            } // end of while (1)
            break;

        case LEFT:
            while (1)
            {
                if ((icol - 1) < 0)
                {
                    return OUT;
                }            
                icol--;    
                
                if (InputArr[irow][icol] == '.')
                {
                    if (icol == 0)
                    {
                        return OUT;
                    }
                    NumOfSteps++;
                    continue;                
                }
                else if (InputArr[irow][icol] == '#')
                {                   
                    Obstacles[ObstCount].row = irow;
                    Obstacles[ObstCount].col = icol;
                    ObstDirection[ObstCount] = LEFT;
                    ObstCount++;

                    if ((irow - 1) < 0)
                    {
                        return OUT;
                    }
                    NumOfSteps++;
                    newPos->row = --irow;
                    newPos->col = ++icol;
                    *nextMove = UP;                    
                    return IN;
                }               
            } // end of while (1)
            break;

        default:
            break;
    }    
}

// 0,4  1,9  7,8  6,1  3,2  4,7  9,6  8,0  
// UP RIGHT DOWN LEFT UP DOWN RIGHT DOWN LEFT
void CreateLoop(int start)
{
    int end = start + 3;
    int firstRow  = Obstacles[start].row;
    int firstCol  = Obstacles[start].col;    
    int fourthRow = Obstacles[end].row;
    int fourthCol = Obstacles[end].col;
    int newObstCol, newObstRow;
    Direction dir = ObstDirection[start];

    switch (dir)
    {
        case UP:
            newObstCol = (firstCol - 1);
            
            if ((newObstCol >= 0) && (fourthCol != newObstCol))
            {
                NewObstacles[NewObstCount].row = fourthRow;
                NewObstacles[NewObstCount].col = newObstCol;
                
                printf("\nNewObstacle: %d,%d", NewObstacles[NewObstCount].row, NewObstacles[NewObstCount].col);

                NewObstCount++;
            }
            break;
        case LEFT:
            newObstRow = (firstRow + 1);
            
            if ((newObstRow < MAX_ROW) && (fourthRow != newObstRow))
            {
                NewObstacles[NewObstCount].row = newObstRow;
                NewObstacles[NewObstCount].col = fourthCol;
                
                printf("\nNewObstacle: %d,%d", NewObstacles[NewObstCount].row, NewObstacles[NewObstCount].col);

                NewObstCount++;
            }
            break;
        case DOWN:
            newObstCol = (firstCol + 1);
            
            if ((newObstCol < MAX_COL) && (fourthCol != newObstCol))
            {
                NewObstacles[NewObstCount].row = fourthRow;
                NewObstacles[NewObstCount].col = newObstCol;
                
                printf("\nNewObstacle: %d,%d", NewObstacles[NewObstCount].row, NewObstacles[NewObstCount].col);

                NewObstCount++;
            }
            break;

        case RIGHT:
            newObstRow = (firstRow - 1);
            
            if ((newObstRow >= 0) && (fourthRow != newObstRow))
            {
                NewObstacles[NewObstCount].row = newObstRow;
                NewObstacles[NewObstCount].col = fourthCol;
                
                printf("\nNewObstacle: %d,%d", NewObstacles[NewObstCount].row, NewObstacles[NewObstCount].col);

                NewObstCount++;
            }
            break;

        default:
            break;
    }       
        
}

int main() 
{
    Position newPos = {0, 0};
    Position currentPos = {0, 0}; 

    Direction nextMove, curMove = UP;                            
    int initObstCount = getObstacles(Obstacles);
    int totalObstCount = 0;
    int start= 0;
    int status = IN;
    
    getGuardPos(&currentPos);   

    while (status == IN)
    {
        status = IsObstacleFound(currentPos, &newPos, curMove, &nextMove);
        printf("Curr Pos: %d %d %d NewPos: %d %d %d\n",currentPos.row, currentPos.col, curMove, newPos.row, newPos.col, nextMove);
        currentPos = newPos;
        curMove = nextMove;
    }
    
    printObstacles(Obstacles, ObstCount);     

    while ((start + 4) <= ObstCount)
    {
        CreateLoop(start);
        start += 3;
    }    

    printf("\nNumber of InitialObstacles: %d ObstaclesIncurred: %d NewObstacles: %d steps: %d\n", 
            initObstCount, ObstCount, NewObstCount, (NumOfSteps - 1));
    return 0;
}