import cv2
import pytesseract

class Text_Detection:
    def __init__(self):
        self.img = cv2.imread("../source/qwerty.jpeg")
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)

    def image_to_string(self):
        print(pytesseract.image_to_string(self.img))

    def image_to_boxes(self):
        img = self.img
        height, width, channel = img.shape

        boxes = pytesseract.image_to_boxes(img)
        for b in boxes.splitlines():
            b = b.split(' ')
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            cv2.rectangle(img, (x, height-y), (w, height-h), (0, 0, 255), 3)
            cv2.putText(img, b[0], (x, height-y+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)

        cv2.imwrite("../source/image_to_boxes.jpeg", img)
        #cv2.imshow("text", img)
        #cv2.waitKey(5000)



    def image_to_data(self):
        img = self.img
        digits = r'--oem 3 --psm 6 outputbase digits'

        #data = pytesseract.image_to_data(img, config=digits)
        data = pytesseract.image_to_data(img)
        for x,b in enumerate(data.splitlines()):
            #print(b)
            if x != 0 :
                b = b.split()
                if len(b) == 12:
                    x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                    cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 3)
                    cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)

        cv2.imwrite("../source/image_data.jpeg", img)
        #cv2.waitKey(5000)



text_detection = Text_Detection()
#text_detection.image_to_string(img)
text_detection.image_to_boxes()
#text_detection.image_to_data()
