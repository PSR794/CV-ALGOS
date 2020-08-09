import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
def main():

    while True:
        try:
            lower=int(input('enter the lower threshold:'))
            if lower<0:
                print('invalid input')
                lower=int(input('enter the lower threshold:'))
        except Exception:
            print('inavlid input')
            main()
            break
            
        try:
            higher=int(input('enter the higher threshold:'))
        except Exception:
            print('inavlid input')
            main()
            break
            
                
    #    higher=int(input('enter the higher threshold:'))
        w=np.uint8(10)
        s=np.uint8(255)
        MAX=0
        element=0
        img=cv.imread('unknown.png',0)

        #GAUSSIAN FILTERING
        ##kernel genration
        def gaussian_kernel(sigma,ksize):
            add=0
            kernel=np.zeros((ksize,ksize),np.uint8)
            k=(ksize-1)//2
            ss=sigma**2
            for i in range(1,ksize+1):
                for j in range(1,ksize+1):
                    expo=np.exp(-(((i-k-1)**2)+((j-k-1)**2))/(2*ss))*100
                    kernel[i-1][j-1]=expo/(2*np.pi*ss)
                    add=np.sum(kernel)
                final=kernel/add
            return final

        ##convolution
        def convolution(ks,karray,image):
            z=ks//2
            black=np.zeros((image.shape[0]+ks-1,image.shape[1]+ks-1),np.uint8)
            roi=black[z:image.shape[0]+z,z:image.shape[1]+z]
            itc=roi+image
            black[z:image.shape[0]+z,z:image.shape[1]+z]=itc
         
            for L in range(black.shape[0]-ks+1):
                for M in range(black.shape[1]-ks+1):
                    matrix=black[L:L+ks,M:M+ks]
                    black[L+z][M+z]=np.sum(np.multiply(karray,matrix))
            return black[z:image.shape[0]+z,z:image.shape[1]+z]
        c=gaussian_kernel(1,5)
        
        gauss=convolution(5,c,img)
        #GRADIENT DETECTION
#        cv.imshow('conv',gauss)
        gx,gy=np.gradient(img)
        gx=np.array(gx,np.float32)
        gy=np.array(gy,np.float32)
        gmag=np.array(np.hypot(gx,gy),np.uint8)
        cv.imshow('asdf',gmag)
        
        #NON MAX SUPRESSION

        #finding the gradient angles for NMS
        angle=np.zeros((gx.shape),np.float32)
        zeroi,zeroj=np.where(gx==0)
        gx[zeroi,zeroj]=1

        angle=(np.arctan(gy/gx)*180)/np.pi
        ang1,ang2=np.where(angle<0)
        angle[ang1,ang2]+=180

        #below are 5 cases of egde angles for NMS using np.where so as to optimize the run time of code
        #np.delete is used for avoiding index errors and leaving no edge accessed.
        #each case has two subcases, 1.a and 1.b have common subcases hence named like that.
        #performing NMS            
        #1.a                
        A,B=np.where((0<=angle)&(angle<22.5))
        B=np.array(B,np.uint16)
        A=np.array(A,np.uint16)
        A=np.delete(A,np.array(np.where(B==0)))
        B=np.delete(B,np.array(np.where(B==0)))
        test=gmag[A,B]
        test1=gmag[A,B-1]
        C=np.array(np.where(test<test1))
        D=A[C]
        E=B[C]
        gmag[D,E]=0

        A,B=np.where((0<=angle)&(angle<22.5))
        B=np.array(B,np.uint16)
        A=np.array(A,np.uint16)
        A=np.delete(A,np.array(np.where(B==gx.shape[1]-1)))
        B=np.delete(B,np.array(np.where(B==gx.shape[1]-1)))
        test=gmag[A,B]
        test2=gmag[A,B+1]
        C=np.array(np.where(test<test2))
        D=A[C]
        E=B[C]
        gmag[D,E]=0
########################        
        #1.b
        A,B=np.where((157.5<=angle)&(angle<180))
        B=np.array(B,np.uint16)
        A=np.array(A,np.uint16)
        
        A=np.delete(A,np.array(np.where(B==0)))
        B=np.delete(B,np.array(np.where(B==0)))
        test=gmag[A,B]
        test1=gmag[A,B-1]
        C=np.array(np.where(test<test1))
        D=A[C]
        E=B[C]
        gmag[D,E]=0

        A,B=np.where((157.5<=angle)&(angle<180))
        B=np.array(B,np.uint16)
        A=np.array(A,np.uint16)
        A=np.delete(A,np.array(np.where(B==gx.shape[1]-1)))
        B=np.delete(B,np.array(np.where(B==gx.shape[1]-1)))
        test=gmag[A,B]
        test2=gmag[A,B+1]
        C=np.array(np.where(test<test2))
        D=A[C]
        E=B[C]
        gmag[D,E]=0
#########################        
        #2
        A,B=np.where((22.5<=angle)&(angle<67.5))
        B=np.array(B,np.uint16)
        A=np.array(A,np.uint16)

        A=np.delete(A,np.array(np.where(B==gx.shape[1]-1)))
        B=np.delete(B,np.array(np.where(A==0)))
        A=np.delete(A,np.array(np.where(A==0)))
        B=np.delete(B,np.array(np.where(B==gx.shape[1]-1)))
        test=gmag[A,B]
        test1=gmag[A-1,B+1]
        C=np.array(np.where(test<test1))
        D=A[C]
        E=B[C]
        gmag[D,E]=0

        A,B=np.where((22.5<=angle)&(angle<67.5))
        B=np.array(B,np.uint16)
        A=np.array(A,np.uint16)        
        A=np.delete(A,np.array(np.where(B==0)))
        B=np.delete(B,np.array(np.where(A==gx.shape[0]-1)))
        A=np.delete(A,np.array(np.where(A==gx.shape[0]-1)))
        B=np.delete(B,np.array(np.where(B==0)))
        test=gmag[A,B]
        test2=gmag[A+1,B-1]
        C=np.array(np.where(test<test2))
        D=A[C]
        E=B[C]
        gmag[D,E]=0
#################################
        #3
        A,B=np.where((67.5<=angle)&(angle<122.5))
        B=np.array(B,np.uint16)
        A=np.array(A,np.uint16)
        
        B=np.delete(B,np.array(np.where(A==0)))
        A=np.delete(A,np.array(np.where(A==0)))
        test=gmag[A,B]
        test1=gmag[A-1,B]
        C=np.array(np.where(test<test1))
        D=A[C]
        E=B[C]
        gmag[D,E]=0

        A,B=np.where((67.5<=angle)&(angle<122.5))
        B=np.array(B,np.uint16)
        A=np.array(A,np.uint16)
        B=np.delete(B,np.array(np.where(A==gx.shape[0]-1)))
        A=np.delete(A,np.array(np.where(A==gx.shape[0]-1)))
        test=gmag[A,B]
        test2=gmag[A+1,B]
        C=np.array(np.where(test<test2))
        D=A[C]
        E=B[C]
        gmag[D,E]=0
################################        
        #4
        A,B=np.where((122.5<=angle)&(angle<157.5))
        B=np.array(B,np.uint16)
        A=np.array(A,np.uint16)
        
        A=np.delete(A,np.array(np.where(B==0)))
        B=np.delete(B,np.array(np.where(B==0)))
        B=np.delete(B,np.array(np.where(A==0)))
        A=np.delete(A,np.array(np.where(A==0)))
        test=gmag[A,B]
        test1=gmag[A-1,B-1]
        C=np.array(np.where(test<test1))
        D=A[C]
        E=B[C]
        gmag[D,E]=0

        A,B=np.where((122.5<=angle)&(angle<157.5))
        B=np.array(B,np.uint16)
        A=np.array(A,np.uint16)
        A=np.delete(A,np.array(np.where(B==gx.shape[1]-1)))
        B=np.delete(B,np.array(np.where(B==gx.shape[1]-1)))
        B=np.delete(B,np.array(np.where(A==gx.shape[0]-1)))
        A=np.delete(A,np.array(np.where(A==gx.shape[0]-1)))
        test=gmag[A,B]
        test2=gmag[A+1,B+1]
        C=np.array(np.where(test<test2))
        D=A[C]
        E=B[C]
        gmag[D,E]=0

        cv.imshow('sdf',gmag)
        
        ##double threshold
        def double_threshold(gmag,LV,HV):
            HT=gmag.max()*HV
            LT=HT*LV
            res=np.zeros((gmag.shape),np.uint8)
            weak=np.uint8(10)
            strong=np.uint8(255)

            si,sj=np.where(gmag>=HT)
            zi,zj=np.where(gmag<LT)
            wi,wj=np.where((gmag<=HT)&(gmag>=LT))#weak pixels indices
            
            res[si,sj]=strong
            res[wi,wj]=weak      #assigning strong and weak pixels to the image
            res[zi,zj]=0
            return res,wi,wj
        d,e,f=double_threshold(gmag,float(lower/100),float(higher/100))
        
        #hysterisis
        #manually u can adjust the iteration for more blotting or continuity (not that effective)
        for i in range(0):
            #replacement of the for loop commented down for hysterisis 
            a,b=np.where(d==w)

            Y=np.delete(a,np.array(np.where(a==d.shape[0]-1)))
            Y=np.delete(Y,np.array(np.where(b==d.shape[1]-1)))
            Y=np.delete(Y,np.array(np.where(b==0)))
            Y=np.delete(Y,np.array(np.where(a==0)))
            
            Z=np.delete(b,np.array(np.where(a==d.shape[0]-1)))
            Z=np.delete(Z,np.array(np.where(b==d.shape[1]-1)))
            Z=np.delete(Z,np.array(np.where(b==0)))
            Z=np.delete(Z,np.array(np.where(a==0)))

            #as for hysterisis a 3X3 block is taken 8 cases are considered.
            e=np.where(d[Y+1,Z]==s)
            C,D=Y[e],Z[e]
            d[C,D]=s
            
            e=np.where(d[Y,Z+1]==s)
            C,D=Y[e],Z[e]
            d[C,D]=s
            
            e=np.where(d[Y+1,Z+1]==s)
            C,D=Y[e],Z[e]
            d[C,D]=s
            
            e=np.where(d[Y-1,Z]==s)
            C,D=Y[e],Z[e]
            d[C,D]=s
            
            e=np.where(d[Y,Z-1]==s)
            C,D=Y[e],Z[e]
            d[C,D]=s
            
            e=np.where(d[Y-1,Z-1]==s)
            C,D=Y[e],Z[e]
            d[C,D]=s
            
            e=np.where(d[Y+1,Z-1]==s)
            C,D=Y[e],Z[e]
            d[C,D]=s
            
            e=np.where(d[Y-1,Z+1]==s)
            C,D=Y[e],Z[e]
            d[C,D]=s
        
        '''
        for i in range(e.shape[0]):
            if s in d[e[i]-1:e[i]+2,f[i]-1:f[i]+2]:
                d[e[i],f[i]]=s    
        ''' 
        #cv.imshow('cyanny',cv.Canny(img,100,200))
        cv.imshow('FINAL',d)
        cv.waitKey()
        cv.destroyAllWindows()
        break
    
if __name__ == '__main__':
    main()



