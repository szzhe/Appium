from PIL import Image, ImageEnhance
import pytesseract
import os


# 截取验证码图片
def identifyingCode(driver, startx, starty, endx, endy):
    driver.get_screenshot_as_file(os.getcwd() + '\\Image\\AFirst_Original.png')
    imGetScreen = Image.open(os.getcwd() + '\\Image\\AFirst_Original.png')
    box = (startx, starty, endx, endy)
    imIndentigy = imGetScreen.crop(box)
    imIndentigy.save(os.getcwd() + '\\Image\\BSecond_Screenshot.png')

    sturdy = Image.open(os.getcwd() + '\\Image\\BSecond_Screenshot.png')
    enhancer = ImageEnhance.Color(sturdy).enhance(1.5)  # 色度增强
    enhancer = ImageEnhance.Brightness(enhancer).enhance(1.5)  # 亮度增强
    enhancer = ImageEnhance.Contrast(enhancer).enhance(1.5)  # 对比度增强
    sturdy = ImageEnhance.Sharpness(enhancer).enhance(3.0)  # 锐度增强
    sturdy.save(os.getcwd() + '\\Image\\CThird_Enhance.png')

    pic_path = os.path.dirname(os.path.abspath('CThird_Enhance.png'))
    print(pic_path)
    return pic_path

# 进阶，灰度处理-去噪点
def convert(pic_path, pic_open):
    # 先将图片进行灰度处理，也就是处理成单色，然后进行下一步单色对比
    # 灰度值：指黑白图像中点的颜色深度，范围一般从0到255，白色为255，黑色为0，故黑白图片也成灰度图像
    imgrey = pic_open.convert('L')

    xsize, ysize = imgrey.size  # 长、宽
    # 对照片里的所有像素点：如果像素色不是白色并且右边的一个像素点像素色是白色（RGB（255，255,255））或者像素色不是白色并且下方的一个像素点是白色的，统一变成白色
    for i in range(ysize - 1):
        for j in range(xsize - 1):
            if (imgrey.getpixel((j, i)) != 255 & imgrey.getpixel((j + 1, i)) != 255):
                imgrey.putpixel((j, i), 0)
            if (imgrey.getpixel((j, i)) != 255 & imgrey.getpixel((j, i + 1)) != 255):
                imgrey.putpixel((j, i), 0)
    imgrey.save(pic_path + '\\Image\\' + 'Dfourth_Size' + '.png', 'png')

    # 去除图片噪点,170是经过多次调整后,去除噪点的最佳值
    '''
    其实就是对已处理的灰度图片中,被认为可能形成验证码字符的像素进行阀值设定，如果阀值等于170,我就认为是形成验证码字符串的所需像素,然后将其添加进一个空table中,
    最后通过im.point将使用table拼成一个新验证码图片
    '''
    table = []
    threshold = 140

    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    rep = {'O': '0',
           'I': '1', 'L': '1',
           'Z': '2',
           'S': '8'
           }

    rep1 = {'0': 'O',
            '1': 'I',
            '2': 'Z',
            '8': 'S'
            }

    # 二值化，采用阈值分割法，threshold为分割点，使用table（是上面生成好的）生成图片
    out = imgrey.point(table, '1')
    out.save(pic_path + '\\Image\\' + 'FFifth_Image' + '.png', 'png')

    # 读取处理好的图片的路径
    imag1 = pic_path + '\\Image\\' + 'FFifth_Image' + '.png', 'png'
    imag2 = Image.open(imag1)

    # 将图片中的像素点识别成字符串（图片中的像素点如果没有处理好，可能在识别过程中会有误差，如多个字符少个字符，或者识别错误等）
    vcode = pytesseract.image_to_string(imag2).strip()
    vcode = vcode.upper()
    for r in rep1:
        vcode = vcode.replace(r, rep1[r])

    # vcode = pytesseract.image_to_string(imag2)
    return vcode  # 此句才是将被破解的验证码字符串返回给需要的代码的

''' 
tesseract chinese.png output -l chi_sim
tesseract chinese.png output -psm 7
'''


def tesseract(self):
    self.strCommand = 'tesseract.exe ' + os.getcwd() + '\\indent.png ' + os.getcwd() + '\\indet.txt'
    print(self.strCommand)
    os.system(self.strCommand)  # 运行其他程序或脚本，可以带参数 os.system('notepad python.txt')

    self.rfindet = open(os.getcwd() + '\\indet.txt', 'r')
    self.strIndet = self.rfindet.readline()
    return self.strIndet
