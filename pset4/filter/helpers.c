#include "helpers.h"
#include <math.h>
#include <stdio.h>

#define MAXBLUR 9

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            double red = image[i][j].rgbtRed;
            double green = image[i][j].rgbtGreen;
            double blue = image[i][j].rgbtBlue;
            float averagefloat = (red + green + blue) / 3;
            double average = round(averagefloat);
            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int originalRed = image[i][j].rgbtRed;
            int originalGreen = image[i][j].rgbtGreen;
            int originalBlue = image[i][j].rgbtBlue;
            float fsepiaRed = (.393 * originalRed) + (.769 * originalGreen) + (.189 * originalBlue);
            int sepiaRed = round(fsepiaRed);
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            float fsepiaGreen = (.349 * originalRed) + (.686 * originalGreen) + (.168 * originalBlue);
            int sepiaGreen = round(fsepiaGreen);
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            float fsepiaBlue = (.272 * originalRed) + (.534 * originalGreen) + (.131 * originalBlue);
            int sepiaBlue = round(fsepiaBlue);
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE imageBuffer[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            imageBuffer[i][j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = imageBuffer[i][width - (j + 1)];
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE imageBuffer[height][width];
    double arrRed[MAXBLUR];
    double arrGreen[MAXBLUR];
    double arrBlue[MAXBLUR];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            imageBuffer[i][j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int r = 0;
            int g = 0;
            int b = 0;
            int n = 9;

            for (int h = -1; h <= 1; h++)
            {
                for (int w = -1; w <= 1; w++, r++, g++, b++)
                {
                    if ((i + h) > height - 1 || (i + h) < 0 || (j + w) > width - 1 || (j + w) < 0)
                    {
                        n = n - 1;
                        arrRed[r] = 0;
                        arrGreen[g] = 0;
                        arrBlue[b] = 0;
                    }
                    else
                    {
                        arrRed[r] = imageBuffer[i + h][j + w].rgbtRed;
                        arrGreen[g] = imageBuffer[i + h][j + w].rgbtGreen;
                        arrBlue[b] = imageBuffer[i + h][j + w].rgbtBlue;
                    }
                }
            }
            float faverageRed = (arrRed[0] + arrRed[1] + arrRed[2] + arrRed[3] + arrRed[4] + arrRed[5] + arrRed[6] + arrRed[7] + arrRed[8]) / n;
            double averageRed = round(faverageRed);
            image[i][j].rgbtRed = averageRed;

            float faverageGreen = (arrGreen[0] + arrGreen[1] + arrGreen[2] + arrGreen[3] + arrGreen[4] + arrGreen[5] + arrGreen[6] + arrGreen[7]
                                   + arrGreen[8]) / n;
            double averageGreen = round(faverageGreen);
            image[i][j].rgbtGreen = averageGreen;

            float faverageBlue = (arrBlue[0] + arrBlue[1] + arrBlue[2] + arrBlue[3] + arrBlue[4] + arrBlue[5] + arrBlue[6] + arrBlue[7]
                                  + arrBlue[8]) / n;
            double averageBlue = round(faverageBlue);
            image[i][j].rgbtBlue = averageBlue;
        }
    }

    return;
}
