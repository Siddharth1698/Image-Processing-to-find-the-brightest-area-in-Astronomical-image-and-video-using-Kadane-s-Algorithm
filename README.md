# Image Processing to find the brightest spot in Astronomical images using Kadane's Algorithm
 Using Kadane's Algorithm to find the brightest spot in Astronomical images.

The maximum subarray problem is used to identify the subarray of a two dimensional array, where the sum of
elements is maximized. In terms of image processing, the solution has been used to find the brightest region
within an image. 

We have a basic approch to this problem which is brute force and it takes O(n^2) time to execute. So we move to dynamic programming known as Kadane's Algo which solves this problem in O(n) times. This is for a 1d array.

In image processing we modify Kadanes algo to a 2d array , please refer here: https://www.geeksforgeeks.org/maximum-sum-rectangle-in-a-2d-matrix-dp-27/ 

We then use openCV to read image and do some preprocessing and pass it to Kadanes algo to find the region which has highest sum which is our brightest spot. I have also implemented this to work for a Video.

Basic Image:

![Basic Image](https://github.com/Siddharth1698/Image-Processing-to-find-the-brightest-spot-in-Astronomical-images-using-Kadane-s-Algorithm/blob/main/imgstar.jpg)



After Kadane's Algorithm:


![Kadane Image](https://github.com/Siddharth1698/Image-Processing-to-find-the-brightest-spot-in-Astronomical-images-using-Kadane-s-Algorithm/blob/main/imgkadane.png)
