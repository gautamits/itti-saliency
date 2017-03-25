import cv2
import numpy as np
import math
def Saliency(rgb):# I is color image
	#convert I to grayscale
	b,g,r = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
	#gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
	gray=0.33*b+0.33*g+0.33*r
	#Extract RGB and Y color channels
	R=r-0.5*g-0.5*b
	G=g-0.5*r-0.5*b
	B=b-0.5*g-0.5*r
	Y=0.5*r+0.5*g-np.absolute(r+g)/2-b
	#till this point channel extraction extraction is successfull
	
	#calculation of intensity maps I(c,s)=|I(c)-I(s)| where c={2,3,4}, s=c+d and d={3,4}
	intensity_1 = np.absolute(pyramid(gray,2)-pyramid(gray,5))
	intensity_2 = np.absolute(pyramid(gray,2)-pyramid(gray,6))
	intensity_3 = np.absolute(pyramid(gray,3)-pyramid(gray,6))
	intensity_4 = np.absolute(pyramid(gray,3)-pyramid(gray,7))
	intensity_5 = np.absolute(pyramid(gray,4)-pyramid(gray,7))
	intensity_6 = np.absolute(pyramid(gray,4)-pyramid(gray,8))
	
	#calculation of double opponency color maps 
	
	red_green_1 = np.absolute((pyramid(R,2)-pyramid(G,2)) - (pyramid(G,5)-pyramid(R,5)))
	red_green_2 = np.absolute((pyramid(R,2)-pyramid(G,2)) - (pyramid(G,6)-pyramid(R,6)))
	red_green_3 = np.absolute((pyramid(R,3)-pyramid(G,3)) - (pyramid(G,6)-pyramid(R,6)))
	red_green_4 = np.absolute((pyramid(R,3)-pyramid(G,3)) - (pyramid(G,7)-pyramid(R,7)))
	red_green_5 = np.absolute((pyramid(R,4)-pyramid(G,4)) - (pyramid(G,7)-pyramid(R,7)))
	red_green_6 = np.absolute((pyramid(R,4)-pyramid(G,4)) - (pyramid(G,8)-pyramid(R,8)))
	
	blue_yellow_1 = np.absolute((pyramid(B,2)-pyramid(Y,2)) - (pyramid(Y,5)-pyramid(B,5)))
	blue_yellow_2 = np.absolute((pyramid(B,2)-pyramid(Y,2)) - (pyramid(Y,6)-pyramid(B,6)))
	blue_yellow_3 = np.absolute((pyramid(B,3)-pyramid(Y,3)) - (pyramid(Y,6)-pyramid(B,6)))
	blue_yellow_4 = np.absolute((pyramid(B,3)-pyramid(Y,3)) - (pyramid(Y,7)-pyramid(B,7)))
	blue_yellow_5 = np.absolute((pyramid(B,4)-pyramid(Y,4)) - (pyramid(Y,7)-pyramid(B,7)))
	blue_yellow_6 = np.absolute((pyramid(B,4)-pyramid(Y,4)) - (pyramid(Y,8)-pyramid(B,8)))
	
	
	
	
	
	cv2.imshow("RGBY",np.hstack((R,G,B,Y)))
	cv2.waitKey(0)
	return np.array(gray,np.uint8)
i=cv2.imread("color.png")
i=cv2.resize(i,(240,240))
r=Saliency(i)
g=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
print g
r=np.hstack((r,g))
cv2.imshow("saliency",r)
cv2.waitKey(0)
