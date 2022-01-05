#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

typedef uint8_t BYTE;
const int BYTE_512 = 512;

int main(int argc, char *argv[])
{
    if (argc > 2 || argc < 2)
    {
        printf("Usage: ./recover infile\n");
        return 1;
    }
    char *infile = argv[1];

    FILE *memorycard = fopen(infile, "r");
    if (memorycard == NULL)
    {
        printf("Could not open the file.\n");
        return 1;
    }

    BYTE buffer[512];
    int n = 0;
    bool jpeg = false;
    char filename[512];
    FILE *img;
    while (fread(&buffer, BYTE_512, 1, memorycard))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            jpeg = true;
            if (n == 0)
            {
                sprintf(filename, "%03i.jpg", n);
                img = fopen(filename, "w");
                if (img == NULL)
                {
                    printf("Could not open the file.\n");
                    return 1;
                }
                fwrite(&buffer, BYTE_512, 1, img);
                n++;
            }
            else
            {
                fclose(img);
                sprintf(filename, "%03i.jpg", n);
                img = fopen(filename, "w");
                if (img == NULL)
                {
                    printf("Could not open the file.\n");
                    return 1;
                }
                fwrite(&buffer, BYTE_512, 1, img);
                n++;
            }
        }
        else if (jpeg == true)
        {
            fwrite(&buffer, BYTE_512, 1, img);
        }
    }

}