#include <stdio.h>
#include <stdlib.h>

__uint8_t getBit(__uint8_t *address, __uint8_t index);
void setBit(__uint8_t *address, __uint8_t index, __uint8_t value);
__uint16_t getCellCount();

void loadCells() {
    FILE* zFile = fopen("zFile.txt", "r");
    if (zFile == NULL) {
        printf("Could not read the files");
        return 1;
    }
    __uint16_t cellCount = getCellCount(zFile);
    for (__uint16_t i=0; i<cellCount; i++) {
        int row, col, flags;
        if (fscanf(zFile, "%d,%d,%d", &row, &col, &flags) != 3) {
            printf("zFile might be corrupted.");
            return 1;
        }
        else {
            // How the fuck do I do that!
            // I need the addres of each item in each cell in cells
            // So that is
            // cells
            //  |--cell
            //      |--row
            //      |--col
            cells[i].row = row;
            cells[i].col = col;
            cells[i].flags = flags;
        }
    }
}

struct Cell {
    __uint8_t row;
    __uint8_t col;
    __uint8_t flags;
};

// enum cellFlag {
//     // walls
//     TOP,
//     LEFT,
//     BOTTOM,
//     RIGHT,
//     // markers
//     VISITED
// };

int main()
{
    

    __uint16_t cellCount = getCellCount();
    struct Cell cells[cellCount];
    

    for (__uint16_t i=0; i<cellCount; i++) {
        printf("%d,%d,%d\n", cells[i].row, cells[i].col, cells[i].flags);
    }
    
    fclose(zFile);


    return 0;
}


__uint16_t getCellCount(FILE *zFile) {
    FILE zFile = open
    struct Cell lastCell = {255, 255, 255};
    __uint8_t row, col, walls;
    while (fscanf(zFile, "%d,%d,%d", &row, &col, &walls) == 3) {
        lastCell.row = row;
        lastCell.col = col;
    }
    fseek(zFile, 0, SEEK_SET);
    return (lastCell.row == 0) ? 0 : (lastCell.row+1)*(lastCell.col+1);
}
__uint8_t getBit(__uint8_t *address, __uint8_t index)
{
    return *address >> index & 1;
}
void setBit(__uint8_t *address, __uint8_t index, __uint8_t value)
{
    if (value == 0) * address &= ~(1 << index);
    else *address |= 1 << index;
}
