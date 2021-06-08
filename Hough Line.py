import numpy as np
import cv2 as cv
def main():
        #should be 0 to around 1000 (try lower values)
        while True:
            try:
                MIN_V=int(input('enter the min threshold:'))
                if MIN_V<0:
                    print('invalid input')
                    MIN_V=int(input('enter the lower threshold:'))
            except Exception:
                print('inavlid input')
                main()
                break
                
            try:
                DBL=int(input('enter the min distance betwenn two lines:'))
            except Exception:
                print('inavlid input')
                main()
                break

            #reading the images
            img=cv.imread('sudoku.png',0)
            img1=cv.imread('sudoku.png')

            #getting the edges
            gx,gy=np.gradient(img)
            gx=np.array(gx,np.float32)
            gy=np.array(gy,np.float32)
            gmag=np.array(np.hypot(gx,gy),np.uint8)
            max_D= ((img.shape[0]**2) + (img.shape[1]**2))**0.5
            max_D=int(max_D)
            #thresholding
            ret,BINARY_PIC=cv.threshold(gmag,25,255,cv.THRESH_BINARY)

            #fetching the edge pixels in the binary image
            y,x=np.where(BINARY_PIC==255)

            #eliminating the zero division error for calculation
#            mul=np.array(np.hypot(x,y),np.uint16)
#            if BINARY_PIC[0,0]==255:
#                y[0]=1
#                x[0]=1
#            denom=np.array(np.hypot(x,y),np.uint16)

            #calculating sine angle of a location
            HAR=np.zeros((2*max_D+1,250))
            #choosing suitable values thetas
            n_thetas=180/250
            theta=np.arange(-90,90,step=n_thetas)
            THETA=np.arange(0,250)
            for c,i in enumerate(y):
                    d= (x[c]*np.cos(np.radians(theta))) + (i*np.sin(np.radians(theta)))
                    D= np.int16(d)+max_D
#                    print(THETA)
                    HAR[D,THETA]+=1
            a,b=np.where(HAR>MIN_V)
            
#            angle=np.array(([sine,]*theta.shape[0])).transpose()
#            th=np.array(([theta,]*sine.shape[0]))

            #getting all the possibilites of angles of the line for a pixel(coordinate)
#            angle+=th

            #getting the all possible normal distances for a pixel(coordinate)

            dis=np.arange(-max_D,max_D+1)
            t=np.arange(-90,90,step=180/250)
            print(t)
            d_line=dis[a]
            t_line=t[b]
            d=int(np.hypot(img.shape[0],img.shape[1]))
            dsort=np.sort(d_line)
            for i in range(dsort.shape[0]-1):
                if abs(dsort[i+1]-dsort[i])<DBL:
                    d_line[np.where((d_line==dsort[i]))]=d+1
                    

            #setting the coordinate arrays for drawing
            w=np.cos((t_line*np.pi)/180)
            v=np.sin((t_line*np.pi)/180)
            Xo=w*d_line
            Yo=v*d_line
            x1=(Xo+1000*(-v))
            x1=np.array(x1,np.int16)
            y1=(Yo+1000*(w))
            y1=np.array(y1,np.int16)
            x2=(Xo-1000*(-v))
            x2=np.array(x2,np.int16)
            y2=(Yo-1000*(w))
            y2=np.array(y2,np.int16)
#            cv.line(img1,(x1,y1),(x2,y2),(0,255,0),2)
            #drawing the lines
            for i in range(x1.shape[0]):
                cv.line(img1,(x1[i],y1[i]),(x2[i],y2[i]),(0,255,0),2)

            #image display
            cv.imshow('LINES',img1)

            cv.waitKey()
            cv.destroyAllWindows()
            break

if __name__ == '__main__':
    main()
'''
            D=np.sin((angle*np.pi)/180)
            mul=np.array(([mul,]*D.shape[1])).transpose()
            D*=mul

            #max D possible in any case


            #for no. of bins inthe hough accumaltor array
            d_lim=(2*d)/400
            t_lim=180/400

            #setting the bin values for accessing them for drawing lines ahead in code


            #the hough accumalator array
            acc=np.zeros((400,400),np.uint16)
            D=D+d
            D_pos=np.array((D*400)/(2*d),np.int16)
            ANGLE_pos=np.array((((th+90)*400)/180),np.int16)

            w=D_pos.flatten()
            v=ANGLE_pos.flatten()

            #assigning values in the bins for the hotspots made due to intersection of curves
            for c,i in enumerate(w):
                acc[i,v[c]]+=1

'''
