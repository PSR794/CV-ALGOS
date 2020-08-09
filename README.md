# CV-TASKS
## **CANNY EDGE DETECTION**
* **Canny edge detection is used to identify the edges in the image for further processing.Here is the code which implements Canny from scratch using Python and numpy.**
* **OpenCV functions were used just for displaying and reading image.**
* **The algorithm is implemented in 5 steps.**

### GAUSSIAN BLURRING
* For executing gaussian blurring, initially a kernel is made from the ```gaussian_kernel(sigma,ksize)``` function which demands two arguments: sigma for the gaussian function and the size of kernel required, which returns the kernel
* The following formula was used in a for loop to make the kernel.
* The gray scale version of the image feeded to the code is convoluted with the kernel which results in the gaussian blurring of itby ```convolution(ks,karray,image)``` function
* Gaussian blurring is essential so as to eliminate the noise in the image which would result in false edges getting in.
* The kernel generation and convolution were carried out by simple for loops.

### GRADIENT DETECTION
* Once w get rid of the noise in the image we calculate its gradient by the ```np.gradient``` in-built numpy function.
* Separate arrays of x and y gradient, magnitude and gradient angle are made to access them further in the code.
* All the angles are made to fit in the range 0 to 180.
* Because of calculating the gradient we still have some pixels getting identifies which may or may not be the real edge.
* Hence further procedure is performed to get exact edges.

### NON-MAX SUPPRESSION
* The edges identified are thicker after gradient detection so we make them thinner by using NMS(Non-Max suppression).
* In this we reach to each of the pixels which is considered to be an edge, as we have the gradient angle of that pixel, we check the intensity of the neighbourhood pixels in the gradient direction,
* If either of the pixel has more intensity than the pixel we have accessed to, then that higher intensity pixel is kept as it is and the one which we have to process is assigned to zero, so when we travel to the outer area to the edge we are basically thinning out the that edge as the higher values are preserved.
* As we have to choose the neighbourhood of the pixel we need the edge angle at that spot having 5 cases:(0,22.5),(22.5,67.5),(67.5,122.5),(122.5,157.5) and (157.5,180) 
* Each of the case needs to check the intensity value of 2 pixels. Where 1st and last case are the same direction so common condition is applied them. 
* NMS makes the edge thinner but simultaneously there are some pixels which are to be trashed for the edge detection.

### DOUBLE THRESHOLDING
* After performing NMS we have some strong,weak and moderate intensity pixels to deal with.
* We declare a ```double_threshold``` function which takes two user inputs for lower and higher threshold.
* Pixels with intensity values higher than the high threshold values are considered to contribute to the edge and on the other hand the pixels with lesser intensity than the lower threshold are assigned zero.
* The pixels falling between these two threshold values are then examined for their connectivity with the strong pixels.
* Separate arrays are declared consisting the indexes of strong and moderate pixels and are returned along with modified image for hysterisis.

### HYSTERISIS
* The final step is to recognize if the pixels with moderate intensity are to be considered as an edge or not.
* Every such pixel's indexed is obtained and checked if there lies a strong pixel in its 3X3 block,assuming that pixel to be at the centre.
* This process is known as hysterisis which differentiates a moderate value intensity pixel into two categories and hence connecting the edge and maintaining its continuity.

* The final output is the desired image for the canny edge displayed.


## HOUGH LINE TRANSFORM
* **This algorithm is used to detect lines in the image** 
* **2nd code implements hough line from scratch by numpy module and python**
the procedure is as follows:
### GRADIENT DETECTION
* Edge pixels are determined using ```np.gradient``` and the image is thresholded to convert it to a binary image.
* Sepearate arrays for x-gradient,y-gradient are defined for further calculation.
* This avoids unnecesary iterations to occur as we deal only with the strong edge pixels and not with the whole image.

### HOUGH SPACE
* We know that euqation of a line is y=mx+c. If m and c are defined then we can have infinte points on the line, and can plot it. 
* On the other hand if we are provided with a specific point then we can pass infinite lines through it.
* So for a certain slope we need a certain intercept to fulfill the condition, given we have the point fixed.
* If we plot m and c on y and x axes respectively then we will get a line having the equation m=(-c/x)+y/x.
* This space generated is called the hough space. Every line would have some certain equation if we consider a point on the image as the origin and proceed further.
* Now to identify a line we need to fetch the data of each bright pixel obtained after thresholding.
* Each pixel will represent a line in the hough space. So if we n lines if we have n pixels.
* These lines would produce some intersection points and by them we can identify if those accessed set of points belong to a line or not.
* The difference is instead of using the slope-intercept form we use the normal equation ```D=(x*cos(theta))+(y*sin(theta))``` and do the necessary calculations to fetch enough data of a pixel to wide range of values of 'd' that is distance of line from the origin.
* As we have two parametres 'd' and 'theta' we choose a range of thetas with equal difference between them and hence calculate corresponding 'd' values and store them in a two 2-D array.
* For each pixel we have the set of both the parametres. What we need to find is the intersection of all these lines.

### HOUGH ACCUMALTOR ARRAY
* We define a 2-D array for 'D' and 'theta' the size of array is the no. of bins we want and we distribute the 'D' and 'theta' values evenly.
* Now we convert the values of the D and theta into their bin numbers with the formula ```(x*(no.of bins))/x_max``` where x is the variable.
* This results in 2 2-D arrays with the bin numbers alloted w.r.t to the values in it.
* Both these arrays are flatten to make an 1-D array and then iterated to fetch couple of numbers from their respective indexes.
* A 2-D hough accumalator array having the shape of these two bin numbers is incremented as the iteration hit a certain position of that array.
* A threshold value is set up so as to avoid arbitrary lines getting detected.
* Another feature of minimum distance required is demanded by the code from the user.
* The values of D having difference less than the required value are omitted.

### DRAWING THE LINES 
* Now we know the indices of the point where intersection is maximum which is the bin number of corresponding parametres.
* After recognizing such points we calculate the values required to draw on the image.
* From the obtained values of parametres we acquire the intercepts and use the ```cv.line``` drawing function by feeding both the intercepts resulting in the ouput image.

NOTE: **The top left corner of the image is considered as origin and hence the image is in 4th quadrant. Assuming 'D' vary from +d to -d where d is the length of the diagonal of the image with theta restricting from -90 to +90** 
 

