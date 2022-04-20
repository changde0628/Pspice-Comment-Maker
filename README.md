# 如何使用PSpice自動加註解工具

**Author : changde0628**

## 前提

這個工具是用Python3寫的，因此在使用前必須確定你的電腦有Python3的任何一個版本。

Python : https://www.python.org/downloads/

<img src="C:\Users\hihet\AppData\Roaming\Typora\typora-user-images\image-20220329001549153.png" alt="image-20220329001549153" style="zoom:80%;" />

## 使用

下載檔案Pspice_Comment_Maker.py，下載在任何一個位置，但我會建議放在桌面。

按下電腦的Windows鍵加R鍵，會出現以下視窗，輸入cmd，按下確定(或Enter)。

<img src="C:\Users\hihet\AppData\Roaming\Typora\typora-user-images\image-20220329001945652.png" alt="image-20220329001945652" style="zoom:80%;" />

接著打開你下載的Pspice_Comment_Maker.py，右鍵點選內容，你會看到位置，把它複製起來。

<img src="C:\Users\hihet\AppData\Roaming\Typora\typora-user-images\image-20220329002308190.png" alt="image-20220329002308190" style="zoom:80%;" />

回到cmd 輸入 : cd /d <你剛剛複製的位置>，按下Enter。

<img src="C:\Users\hihet\AppData\Roaming\Typora\typora-user-images\image-20220329002456743.png" alt="image-20220329002456743" style="zoom:80%;" />

接著你可以開始使用Pspice_Comment_Maker了，輸入 : Pspice_Comment_Maker.py <你要加上註解的程式碼(含檔名)>

例如: 將excerise1.cir加上註解，輸入 : Pspice_Comment_Maker.py excerise1.cir

![image-20220329002836113](C:\Users\hihet\AppData\Roaming\Typora\typora-user-images\image-20220329002836113.png)

## 後記

Version1.0 : Update 2022/3/28

Version1.1 : Update 2022/3/29 修正lambda偵測錯誤

Version1.2 : Updata 2022/4/20 新增方波偵測和.AC指令