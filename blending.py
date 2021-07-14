import cv2

cap=cv2.VideoCapture(0)



while cap.isOpened():
  while True:  
   
   print("Which background would u love to see? \n 1-GOKU \n 2-APPLE \n 3-ORANGE \n 4-PEAR \n 5-PINEAPPLE \n 6-STARRYSKY ")
   x=int(input("PPlease enter a number")) 
   if x==1:
       flag, frame= cap.read()
       if flag:
           
           image1=cv2.imread('goku.jpg')
           image1=cv2.resize(image1,(frame.shape[1],frame.shape[0]))
           blended_frame=cv2.addWeighted(frame, 0.7, image1, 0.3, gamma=0.1)
           cv2.imshow("Blended Frame", blended_frame)
           if not flag:
             print("Couldnt access")
             break 
           k=cv2.waitKey(0)
           if k & 0xff==ord('q'):
                break
       
       
       

   elif x==2:

       if flag:
           image2=cv2.imread('orange.jpg')
           image2=cv2.resize(image2,(frame.shape[1],frame.shape[0]))
           blended_frame=cv2.addWeighted(frame, 0.7, image2, 0.3, gamma=0.1)
           cv2.imshow("Blended Frame", blended_frame)
           if not flag:
             print("Couldnt access")
             break
           k=cv2.waitKey(0)
           if k & 0xff==ord('q'):
                break
       
  
       

   elif x==3:
       if flag:
           image3=cv2.imread('apple.jpg')
           image3=cv2.resize(image3,(frame.shape[1],frame.shape[0]))
           blended_frame=cv2.addWeighted(frame, 0.7, image3, 0.3, gamma=0.1)
           cv2.imshow("Blended Frame", blended_frame)
           if not flag:
             print("Couldnt access")
             break
           k=cv2.waitKey(0)
           if k & 0xff==ord('q'):
                break
       
       

   elif x==4:
       if flag:
           image4=cv2.imread('pear.jpg')
           image4=cv2.resize(image4,(frame.shape[1],frame.shape[0]))
           blended_frame=cv2.addWeighted(frame, 0.7, image4, 0.3, gamma=0.1)
           cv2.imshow("Blended Frame", blended_frame)
           if not flag:
             print("Couldnt access")
             break
           k=cv2.waitKey(0)
           if k & 0xff==ord('q'):
                break
       

   elif x==5:
       if flag:
           image5=cv2.imread('pineapple.jpg')
           image5=cv2.resize(image5,(frame.shape[1],frame.shape[0]))
           blended_frame=cv2.addWeighted(frame, 0.7, image5, 0.3, gamma=0.1)
           cv2.imshow("Blended Frame", blended_frame)
           if not flag:
             print("Couldnt access")
             break
           k=cv2.waitKey(0)
           if k & 0xff==ord('q'):
                break
           
   
           
       

   else:
        break

   

    
cap.release()
cv2.destroyAllWindows()
   


"""newimage2=cv2.resize(image2, (image1.shape[1],image1.shape[0]))
added_image=image1+newimage2
blended_image=cv2.addWeighted(image1, 0.3, newimage2, 0.7, 0.4)


cv2.imshow("Final Image",added_image)
cv2.imshow("Blended Image",blended_image)

cv2.waitKey(0)"""


