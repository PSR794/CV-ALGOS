# CV-TASKS
## **CANNY EDGE DETECTION**

* **Canny edge detection is used to identify the edges in the image for further processing. Here is the code which implements Canny from scratch using Python and NumPy.**
* **Basic OpenCV functions were used just for displaying and reading the image.**
* **The algorithm is implemented in 5 steps.**
 ---
 ---

### 1.GAUSSIAN BLURRING
*  Initially a kernel is made with the ```gaussian_kernel(sigma,ksize)``` function for executing gaussian blurring, which demands two arguments: sigma for the Gaussian function and the size of kernel required, which returns the kernel
* The following formula(Gaussian) was used to make the kernel.
 ![](https://i.imgur.com/z3e4w7Y.jpg)

* The grayscale version of the image fed to the code is convoluted with the kernel which results in the gaussian blurring and the ```convolution(ks,karray, image)``` function returns the blurred image.
* Gaussian blurring is essential to eliminate the noise in the image which would result in false edges getting in.
---
---

### 2.GRADIENT DETECTION
* Once we get rid of the noise in the image, we calculate its gradient by the ```np.gradient``` (in-built NumPy function).
* Separate arrays of x and y gradient, magnitude, and gradient angle are declared to access them further in the code.
* All the angles are adjusted in the range 0 to 180.
* After calculating the gradient, we would still be left with some pixels getting identified.
* The identified pixels may or may not be the real edge
* Hence further procedure is performed to fetch exact edges.
---
---
### 3.NON-MAX SUPPRESSION
* The identified edges are thicker after gradient detection, hence we make them thinner by NMS(Non-Max suppression).
* In this we take into consideration, the pixels which are supposed to be an edge, as we have the gradient angle of that pixel, we check the intensity of the two neighborhood pixels in the gradient direction.
* If either of the pixels possesses the higher intensity, then it is preserved while the other one is assigned zero, so when we travel to the outer area of the edge, we are thinning it out higher values are maintained as it is.
![](https://i.imgur.com/z1hjrsL.jpg)
> those orange arrows show the direction of "edge angle" or say "gradient angle" so for ex: in the top one where dotted box is drawn, the highlihted pixel is darkened


* As we have to choose the neighborhood of the pixel we need the edge angle at that spot having 5 cases:(0,22.5),(22.5,67.5),(67.5,122.5),(122.5,157.5) and (157.5,180) 
* Each of the cases needs to check the intensity value of 2 pixels. Where in the first and the last one, we have the same directions, so a common condition applies to them. 
* Though NMS makes the edge thinner but on the other hand,  there are some pixels to be trashed for the desired outcome.
---
---
### 4.DOUBLE THRESHOLDING
* After performing NMS, we have some strong, weak, and moderate-intensity pixels to deal with.
* We declare a ```double_threshold``` function. It takes two user inputs for a lower and higher threshold.
* Pixels with intensity values higher than the high threshold values contribute to the edge. On the other hand, the pixels with lesser intensity than the lower threshold, assigned as zero.
* The pixels falling between these two threshold values are then examined for their connectivity with strong ones.
* Separate arrays are declared consisting of the indices of the strong and moderate pixels and are returned along with the modified image for hysteresis.
* A suitable pair of thresholds is fruitful, as picking the extremes will miss many edges while the other side of the coin is that if lower ends are chosen, unwanted edges are detected.
---
---
### 5.HYSTERISIS
* The final step is to recognize if the pixels with moderate intensity are to be considered as an edge or not.
* Every such pixel's indexed is obtained and checked if there lies a  pixel with 'strong' intensity in its 3X3 block, assuming that pixel to be at the center.
![](https://i.imgur.com/aLMS04X.jpg)
> here in the first case the weak pixel is not said to be connected, while in the second one we count that as connected one and brighten it.
* This process is known as hysteresis as it differentiates a moderate value intensity pixel into two categories and hence connecting the edge and maintaining its continuity.
* The final output is the desired image for the canny edge displayed.

**NOTE: Both the threshold inputs should be in between 1-1000 but lower values (<100) are preferred.**

Language versions:
1. Python 3.7
2. OpenCV 4.2.0
3. numpy 1.19.0


